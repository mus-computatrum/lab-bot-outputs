import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ─── OSI computation helper ───────────────────────────────────────────────────
def compute_osi_for_experiment(nwb_path):
    """
    Returns a DataFrame with columns:
      ophys_experiment_id, cell_specimen_id, osi
    Uses drifting-grating trials: baseline-subtracted mean DF/F over [start, end] frames,
    averaged per (orientation, TF); OSI = (Rpref - Rorth) / (Rpref + Rorth) at preferred TF.
    Negative baselines are clipped at 0 for the denominator.
    """
    exp_id = int(os.path.basename(nwb_path).replace('.nwb',''))
    
    with h5py.File(nwb_path, 'r') as f:
        # ── Cell specimen IDs ──────────────────────────────────────────────
        seg = f['processing/brain_observatory_pipeline/ImageSegmentation']
        cell_ids = seg['cell_specimen_ids'][:]          # shape (n_cells,)
        
        # ── DF/F traces ────────────────────────────────────────────────────
        dff_data = f['processing/brain_observatory_pipeline/DfOverF/imaging_plane_1/data'][:]
        # shape: (n_cells, n_frames)
        n_cells, n_frames = dff_data.shape
        
        # ── Drifting grating stimulus ──────────────────────────────────────
        dg = f['stimulus/presentation/drifting_gratings_stimulus']
        stim_data = dg['data'][:]         # (n_trials, 3): [TF, ori, blank]
        frame_dur = dg['frame_duration'][:]  # (n_trials, 2): [start, end]
    
    # Non-blank trials only
    blank_mask = stim_data[:, 2] == 0
    stim_data  = stim_data[blank_mask]
    frame_dur  = frame_dur[blank_mask]
    
    tfs   = stim_data[:, 0].astype(int)
    oris  = stim_data[:, 1].astype(int)
    starts = frame_dur[:, 0].astype(int)
    ends   = frame_dur[:, 1].astype(int)
    
    n_trials = len(stim_data)
    baseline_win = 30   # frames (~1 s at 30 Hz) before stimulus onset
    
    # ── Compute per-trial mean response (baseline-subtracted) ─────────────
    # shape: (n_cells, n_trials)
    resp = np.zeros((n_cells, n_trials), dtype=np.float32)
    
    for t in range(n_trials):
        s, e = starts[t], ends[t]
        # baseline: 30 frames before stimulus onset, clamp at 0
        b_start = max(0, s - baseline_win)
        b_end   = s
        if b_end > b_start:
            baseline = dff_data[:, b_start:b_end].mean(axis=1)
        else:
            baseline = np.zeros(n_cells, dtype=np.float32)
        
        # stimulus window
        stim_mean = dff_data[:, s:e].mean(axis=1)
        resp[:, t] = stim_mean - baseline
    
    # ── Compute mean response per cell × (ori, TF) ────────────────────────
    unique_oris = np.sort(np.unique(oris))    # [0,45,90,135,180,225,270,315]
    unique_tfs  = np.sort(np.unique(tfs))
    
    # mean_resp[cell, ori_idx, tf_idx]
    mean_resp = np.full((n_cells, len(unique_oris), len(unique_tfs)), np.nan, dtype=np.float32)
    for oi, ori in enumerate(unique_oris):
        for ti, tf in enumerate(unique_tfs):
            mask = (oris == ori) & (tfs == tf)
            if mask.sum() > 0:
                mean_resp[:, oi, ti] = resp[:, mask].mean(axis=1)
    
    # ── OSI: preferred TF approach ────────────────────────────────────────
    # For each cell: find (ori, TF) with max mean response
    # Then compute tuning over directions at that preferred TF
    # OSI = (Rpref - Rorth) / (Rpref + Rorth)
    #
    # Map directions to orientations (0/180 → 0, 45/225 → 45, 90/270 → 90, 135/315 → 135)
    # For OSI we use all 8 directions; preferred direction → orthogonal is ±90°
    
    records = []
    for ci in range(n_cells):
        # Preferred direction × TF
        flat_idx = np.nanargmax(mean_resp[ci])
        pref_oi, pref_ti = np.unravel_index(flat_idx, (len(unique_oris), len(unique_tfs)))
        pref_ori = unique_oris[pref_oi]   # preferred direction (0-315)
        pref_tf  = unique_tfs[pref_ti]
        
        # Tuning curve at preferred TF across all 8 directions
        tc = mean_resp[ci, :, pref_ti]    # shape (8,)
        
        Rpref = tc[pref_oi]
        
        # Orthogonal directions: pref ± 90 degrees
        orth_dirs = [(pref_ori + 90) % 360, (pref_ori - 90) % 360]
        orth_resps = []
        for od in orth_dirs:
            if od in unique_oris:
                oi2 = np.where(unique_oris == od)[0]
                if len(oi2):
                    orth_resps.append(tc[oi2[0]])
        
        if orth_resps:
            Rorth = np.mean(orth_resps)
        else:
            Rorth = np.nan
        
        denom = Rpref + Rorth
        if np.isnan(denom) or denom <= 0:
            osi = np.nan
        else:
            osi = (Rpref - Rorth) / denom
        
        records.append({
            'ophys_experiment_id': exp_id,
            'cell_specimen_id': int(cell_ids[ci]),
            'osi': float(osi)
        })
    
    return pd.DataFrame(records)

# ── Test on first experiment ──────────────────────────────────────────────────
df_test = compute_osi_for_experiment(sst_visp_nwbs[0])
print(f"Experiment {sst_visp_nwbs[0].split('/')[-1]}:")
print(df_test)
print(f"\nOSI stats: mean={df_test.osi.mean():.3f}, median={df_test.osi.median():.3f}, "
      f"nan={df_test.osi.isna().sum()}")
