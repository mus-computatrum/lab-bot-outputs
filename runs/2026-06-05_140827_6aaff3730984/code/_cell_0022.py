
# Step A3: Extract per-trial trace segments for the repeated clip
# ~10s clip at 6.3 Hz ≈ 63 frames per trial

FRAME_RATE = 6.30  # Hz (measured)

def time_to_frame(t, timestamps):
    """Find nearest frame index to time t."""
    return np.searchsorted(timestamps, t)

# Get frame indices for each repeat
trial_frames = []
for t_start, t_stop in zip(repeat_starts, repeat_stops):
    f_start = time_to_frame(t_start, timestamps)
    f_stop  = time_to_frame(t_stop, timestamps)
    trial_frames.append((f_start, f_stop))

# Find minimum trial length (should be nearly identical)
trial_lengths = [fs - f for f, fs in trial_frames]
print(f"Trial lengths (frames): {trial_lengths}")
T_trial = min(trial_lengths)
print(f"Using {T_trial} frames per trial (~{T_trial/FRAME_RATE:.1f} s)")

# Build trial matrix: (n_repeats, T_trial, N_rois)
trial_matrix = np.stack([
    traces[f_start:f_start+T_trial, :]
    for f_start, _ in trial_frames
], axis=0)  # (n_repeats, T_trial, N_rois)

print(f"\nTrial matrix shape: {trial_matrix.shape} (repeats x frames x rois)")
print(f"Trace range: {trial_matrix.min():.3f} – {trial_matrix.max():.3f}")
print(f"Mean DF/F: {trial_matrix.mean():.4f}")
