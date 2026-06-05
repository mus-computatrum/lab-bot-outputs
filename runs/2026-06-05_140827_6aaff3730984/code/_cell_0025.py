
# Step A7: Identify high-noise-correlation short-distance pairs ("functional candidates")
# Threshold: exceed 99th percentile of surrogate AND distance < 50 µm

nc_null_99 = np.percentile(nc_null, 99)
print(f"Surrogate 99th percentile threshold: {nc_null_99:.4f}")

short_dist_mask = pair_dist_rois < 50.0
high_nc_mask    = pair_nc > nc_null_99

# Functional candidates: close AND high NC
func_cand_mask = short_dist_mask & high_nc_mask

# Also flag pairs with >median signal correlation (shared stimulus drive)
med_sc = np.median(pair_sc[short_dist_mask])
low_sc_mask = pair_sc < med_sc  # noise correlation NOT explained by shared stimulus drive

# "Pure noise" candidates: close + high NC + low SC
pure_noise_mask = short_dist_mask & high_nc_mask & low_sc_mask

print(f"\nShort-distance pairs (d < 50µm): {short_dist_mask.sum():,}")
print(f"High NC pairs above 99th pct:    {high_nc_mask.sum():,}")
print(f"Close + High NC (functional candidates): {func_cand_mask.sum():,}")
print(f"  of which Low SC (not explained by shared stimulus): {pure_noise_mask.sum():,}")

# Build a DataFrame of functional candidates
# We need ROI indices from upper triangle
iu_i, iu_j = iu  # source indices into the 1323-ROI array
func_cand_df = pd.DataFrame({
    'roi_a_idx': iu_i[func_cand_mask],
    'roi_b_idx': iu_j[func_cand_mask],
    'dist_um':   pair_dist_rois[func_cand_mask],
    'noise_corr': pair_nc[func_cand_mask],
    'signal_corr': pair_sc[func_cand_mask],
    'total_corr': pair_tc[func_cand_mask],
    'cx_a': cx[iu_i[func_cand_mask]],
    'cy_a': cy[iu_i[func_cand_mask]],
    'cx_b': cx[iu_j[func_cand_mask]],
    'cy_b': cy[iu_j[func_cand_mask]],
}).sort_values('noise_corr', ascending=False)

func_cand_df.to_csv('/work/functional_candidates.csv', index=False)
print(f"\nTop functional candidates:")
print(func_cand_df.head(20).to_string(index=False))
