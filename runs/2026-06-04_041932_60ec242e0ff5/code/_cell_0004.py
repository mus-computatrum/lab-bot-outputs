import numpy as np
import os
from collections import defaultdict

base = '/data/bugeon2022-v1'

# Accumulators: per (session, cell_idx) -> {run_sum, run_n, stat_sum, stat_n}
# We store (ttype, run_sum, run_n, stat_sum, stat_n) per cell-observation

records = []  # list of dicts: {ttype, run_sum, run_n, stat_sum, stat_n}

for mouse in sorted(os.listdir(base)):
    mouse_path = os.path.join(base, mouse)
    if not os.path.isdir(mouse_path):
        continue
    for session in sorted(os.listdir(mouse_path)):
        sess_path = os.path.join(mouse_path, session)
        ttype_file = os.path.join(sess_path, 'neuron.ttype.txt')
        if not os.path.exists(ttype_file):
            continue
        
        ttypes = np.array(open(ttype_file).read().splitlines())
        n_neurons = len(ttypes)
        
        # Find SST neuron indices for this session
        sst_mask = np.array([t.startswith('Sst') for t in ttypes])
        sst_idx = np.where(sst_mask)[0]
        if len(sst_idx) == 0:
            continue
        
        # Accumulators per SST cell for this session
        run_sum = np.zeros(len(sst_idx), dtype=np.float64)
        run_n   = np.zeros(len(sst_idx), dtype=np.int64)
        stat_sum = np.zeros(len(sst_idx), dtype=np.float64)
        stat_n   = np.zeros(len(sst_idx), dtype=np.int64)
        
        # Walk all stimulus sub-recordings for this session
        for stim_type in os.listdir(sess_path):
            stim_path = os.path.join(sess_path, stim_type)
            if not os.path.isdir(stim_path):
                continue
            for run_num in os.listdir(stim_path):
                run_path = os.path.join(stim_path, run_num)
                act_file = os.path.join(run_path, 'frame.neuralActivity.npy')
                st_file  = os.path.join(run_path, 'frame.states.npy')
                if not (os.path.exists(act_file) and os.path.exists(st_file)):
                    continue
                
                activity = np.load(act_file)  # (frames, neurons)
                states   = np.load(st_file).squeeze()  # (frames,)
                
                # Validate shape
                if activity.shape[1] != n_neurons:
                    print(f"  WARNING: shape mismatch {mouse}/{session}/{stim_type}/{run_num}: "
                          f"activity={activity.shape}, n_neurons={n_neurons}")
                    continue
                
                # Extract SST columns
                sst_act = activity[:, sst_idx]  # (frames, n_sst)
                
                # Mask by state
                run_mask  = (states == 0)
                stat_mask = (states == 1)
                
                if run_mask.sum() > 0:
                    run_sum  += sst_act[run_mask].sum(axis=0)
                    run_n    += run_mask.sum()
                if stat_mask.sum() > 0:
                    stat_sum += sst_act[stat_mask].sum(axis=0)
                    stat_n   += stat_mask.sum()
        
        # Store per-cell records for this session
        for i, cidx in enumerate(sst_idx):
            records.append({
                'ttype':    ttypes[cidx],
                'run_sum':  run_sum[i],
                'run_n':    run_n[i],
                'stat_sum': stat_sum[i],
                'stat_n':   stat_n[i],
            })

print(f"Total SST cell-session records: {len(records)}")

# Quick sanity: count records with 0 frames in either state
bad = sum(1 for r in records if r['run_n'] == 0 or r['stat_n'] == 0)
print(f"Records with missing frames for a state: {bad}")

# Show ttype distribution
from collections import Counter
tc = Counter(r['ttype'] for r in records)
print("\nSST t-type counts (cell-session records):")
for k, v in sorted(tc.items()):
    print(f"  {k}: {v}")
