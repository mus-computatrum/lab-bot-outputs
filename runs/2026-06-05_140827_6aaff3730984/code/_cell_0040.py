
# Quick sanity checks on key results
print("=== SANITY CHECKS ===\n")

# 1. NC at d<20um should exceed surrogate 99th pct for some pairs
nc_thresh_99 = np.percentile(nc_null, 99)
n_d20_above = ((pair_dist_rois < 20) & (pair_nc > nc_thresh_99)).sum()
n_d20_total = (pair_dist_rois < 20).sum()
print(f"1. NC > 99th pct null among d<20µm pairs: {n_d20_above}/{n_d20_total} = {n_d20_above/n_d20_total*100:.1f}%")

# 2. Effect size is in expected range
assert 0.5 < cohen_d < 1.5, f"Unexpected Cohen's d: {cohen_d}"
print(f"2. Cohen's d = {cohen_d:.3f} ✓ (expected medium effect)")

# 3. Synapse counts look right (mean should be ~2 for within-proofread pairs)
assert 1.5 < counts.mean() < 3.0, f"Unexpected mean synapse count: {counts.mean()}"
print(f"3. Mean within-proofread synapse count: {counts.mean():.2f} ✓")

# 4. Connectivity density is in plausible range for cortex (~1-10%)
density = conn_matrix.nnz / (N * N) * 100
assert 1.0 < density < 15.0, f"Unexpected density: {density}"
print(f"4. Connectivity density: {density:.2f}% ✓")

# 5. Top functional candidates are in reasonable NC range
top_nc_val = func_cand_df['noise_corr'].max()
assert 0.5 < top_nc_val < 1.0, f"NC out of range: {top_nc_val}"
print(f"5. Max functional candidate NC: {top_nc_val:.3f} ✓")

# 6. Skeleton dd distances are plausible (nm scale converted to µm)
min_dd = dd_df['dendrite_dendrite_dist_um'].min()
assert 0.5 < min_dd < 5.0, f"Unexpected dd distance: {min_dd}"
print(f"6. Minimum skeleton dd distance: {min_dd:.3f} µm ✓")

print("\n✅ All sanity checks passed.")
