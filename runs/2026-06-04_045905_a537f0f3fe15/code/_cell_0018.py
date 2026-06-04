# Examine drifting gratings stimulus in detail for one experiment
with h5py.File(nwb_path, 'r') as f:
    dg = f['stimulus/presentation/drifting_gratings_stimulus']
    data = dg['data'][:]       # (n_trials, 3): [TF, orientation, blank]
    fd   = dg['frame_duration'][:]  # (n_trials, 2): [start, end] frames

features = [b'temporal_frequency', b'orientation', b'blank_sweep']
tf_col, ori_col, blank_col = 0, 1, 2

# Non-blank trials
mask = data[:, blank_col] == 0
print(f"Total trials: {len(data)}, non-blank: {mask.sum()}")
print("Unique orientations:", sorted(set(data[mask, ori_col].astype(int))))
print("Unique TFs:", sorted(set(data[mask, tf_col].astype(int))))
print("Typical trial duration (frames):", (fd[mask, 1] - fd[mask, 0]).mean().round(1))
print("Inter-trial interval (frames):", (fd[1:, 0] - fd[:-1, 1]).mean().round(1))
