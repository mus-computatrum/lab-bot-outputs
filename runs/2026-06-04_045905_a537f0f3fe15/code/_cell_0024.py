# Quick summary table per experiment
summary = full_df.groupby('ophys_experiment_id').agg(
    n_cells=('osi','count'),
    osi_mean=('osi', 'mean'),
    osi_median=('osi', 'median'),
    osi_std=('osi', 'std')
).round(3).reset_index()

print("Per-experiment summary:")
print(summary.to_string(index=False))
