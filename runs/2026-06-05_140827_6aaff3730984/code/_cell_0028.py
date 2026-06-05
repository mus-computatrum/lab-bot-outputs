
# C2: Structural analysis — synapse count vs distance for proofread neurons
# Build a comprehensive pairwise structural DataFrame for close pairs

struct_pairs_df = close_pairs_df.copy()
struct_pairs_df['log_syn_total'] = np.log1p(struct_pairs_df['syn_total'])

# Bin distances
dist_bins_struct = [0, 20, 40, 60, 80, 100]
struct_by_bin = []
for d_lo, d_hi in zip(dist_bins_struct[:-1], dist_bins_struct[1:]):
    mask_b = (struct_pairs_df['dist_um'] >= d_lo) & (struct_pairs_df['dist_um'] < d_hi)
    sub = struct_pairs_df[mask_b]
    struct_by_bin.append({
        'dist_lo': d_lo, 'dist_hi': d_hi,
        'n_pairs': len(sub),
        'frac_connected': (sub['syn_total'] > 0).mean(),
        'mean_syn': sub['syn_total'].mean(),
        'frac_zero_syn': (sub['syn_total'] == 0).mean(),
        'frac_bilateral': ((sub['syn_ab'] > 0) & (sub['syn_ba'] > 0)).mean(),
    })
    print(f"d={d_lo}-{d_hi}µm: n={len(sub):,}, "
          f"connected={100*(sub['syn_total']>0).mean():.1f}%, "
          f"zero-syn={100*(sub['syn_total']==0).mean():.1f}%, "
          f"bilateral={100*((sub['syn_ab']>0)&(sub['syn_ba']>0)).mean():.2f}%")

struct_bins_df = pd.DataFrame(struct_by_bin)
struct_bins_df.to_csv('/work/structural_by_distance_bin.csv', index=False)

# C3: Effect size — compare high-NC pairs vs surrogate in the short-distance regime
short_dist_nc = pair_nc[short_dist_mask]
nc_null_short = nc_null  # same null regardless of distance (circular shift)
cohen_d = (short_dist_nc.mean() - nc_null.mean()) / np.sqrt(
    (short_dist_nc.std()**2 + nc_null.std()**2) / 2)
print(f"\nEffect size (Cohen's d) for NC in short-distance pairs vs surrogate: {cohen_d:.3f}")
print(f"Short-dist NC mean: {short_dist_nc.mean():.4f}, surrogate mean: {nc_null.mean():.4f}")

# Mannwhitney test
stat, pval = stats.mannwhitneyu(short_dist_nc, nc_null, alternative='greater')
print(f"Mann-Whitney U (short-dist NC > surrogate): p={pval:.2e}")
