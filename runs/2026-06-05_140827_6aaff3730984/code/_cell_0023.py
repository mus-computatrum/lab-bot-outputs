
# Step A4: Compute signal and noise correlations
# Signal correlation: corr of mean-trial responses (stimulus-driven)
# Noise correlation:  corr of trial residuals (what remains after removing signal)

# Normalize each ROI by its overall mean/std (z-score across full session)
# to make correlations comparable
traces_zscore = (traces - traces.mean(0)) / (traces.std(0) + 1e-8)

# Z-score the trial matrix too
signal = trial_matrix.mean(0)  # (T_trial, N_rois) — mean across repeats = signal
noise  = trial_matrix - signal[np.newaxis, :, :]  # (n_repeats, T_trial, N_rois) residuals

# Flatten time within trial for correlation
# Signal correlation: (N_rois,) per frame → flatten to (T_trial * N_rois,)
signal_flat = signal.T  # (N_rois, T_trial)
noise_flat  = noise.reshape(n_repeats, -1).T   # wrong shape; need (N_rois, n_repeats*T_trial)
# Correctly: for each ROI, concatenate all trial residuals
# noise shape: (n_repeats, T_trial, N_rois) → reshape to (N_rois, n_repeats*T_trial)
noise_flat  = noise.transpose(2, 0, 1).reshape(N_rois, -1)  # (N_rois, n_repeats*T_trial)
signal_flat = signal.T  # (N_rois, T_trial)

print(f"Signal flat shape: {signal_flat.shape}")
print(f"Noise flat shape: {noise_flat.shape}")

# Compute pairwise noise correlation matrix (fast with numpy)
# Normalize each row
def row_corr(X):
    """Compute pairwise Pearson correlation matrix of rows."""
    Xc = X - X.mean(1, keepdims=True)
    norms = np.linalg.norm(Xc, axis=1, keepdims=True) + 1e-10
    Xn = Xc / norms
    return Xn @ Xn.T

print("Computing noise correlation matrix...")
noise_corr = row_corr(noise_flat.astype(np.float32))   # (N_rois, N_rois)
print(f"Noise correlation matrix: shape={noise_corr.shape}, "
      f"off-diag range={noise_corr[np.triu_indices(N_rois,1)].min():.3f} to "
      f"{noise_corr[np.triu_indices(N_rois,1)].max():.3f}")

print("Computing signal correlation matrix...")
signal_corr = row_corr(signal_flat.astype(np.float32))
print(f"Signal correlation matrix: off-diag range={signal_corr[np.triu_indices(N_rois,1)].min():.3f} to "
      f"{signal_corr[np.triu_indices(N_rois,1)].max():.3f}")

print("Computing total correlation on full trace (z-scored)...")
total_corr = row_corr(traces_zscore.T.astype(np.float32))
print(f"Total correlation: off-diag range={total_corr[np.triu_indices(N_rois,1)].min():.3f} to "
      f"{total_corr[np.triu_indices(N_rois,1)].max():.3f}")
