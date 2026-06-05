
# ═══════════════════════════════════════════════════════════════
# PHASE C — INTEGRATION + STATISTICAL RIGOR
# ═══════════════════════════════════════════════════════════════

# C1: Quantify NC vs distance with bootstrap CIs
import scipy.stats as stats

# Bin distances (µm)
dist_bins = [0, 20, 40, 60, 80, 100, 150, 200, 300, 500, 1000]
bin_labels = [10, 30, 50, 70, 90, 125, 175, 250, 400, 750]

nc_by_bin = []
tc_by_bin = []
for d_lo, d_hi in zip(dist_bins[:-1], dist_bins[1:]):
    mask = (pair_dist_rois >= d_lo) & (pair_dist_rois < d_hi)
    nc_vals = pair_nc[mask]
    tc_vals = pair_tc[mask]
    
    # Bootstrap CI
    boot_means_nc = [np.random.choice(nc_vals, size=min(len(nc_vals), 5000), replace=True).mean() 
                     for _ in range(500)] if len(nc_vals) > 0 else [np.nan]
    boot_means_tc = [np.random.choice(tc_vals, size=min(len(tc_vals), 5000), replace=True).mean() 
                     for _ in range(500)] if len(tc_vals) > 0 else [np.nan]
    
    nc_by_bin.append({
        'dist_center': (d_lo + d_hi) / 2,
        'dist_lo': d_lo, 'dist_hi': d_hi,
        'n_pairs': mask.sum(),
        'nc_mean': nc_vals.mean() if len(nc_vals) > 0 else np.nan,
        'nc_ci_lo': np.percentile(boot_means_nc, 2.5),
        'nc_ci_hi': np.percentile(boot_means_nc, 97.5),
        'tc_mean': tc_vals.mean() if len(tc_vals) > 0 else np.nan,
        'tc_ci_lo': np.percentile(boot_means_tc, 2.5),
        'tc_ci_hi': np.percentile(boot_means_tc, 97.5),
    })
    print(f"d={d_lo}-{d_hi}µm: n={mask.sum():6,}, NC={nc_vals.mean():.4f} [{np.percentile(boot_means_nc, 2.5):.4f}, {np.percentile(boot_means_nc, 97.5):.4f}]")

nc_bins_df = pd.DataFrame(nc_by_bin)
nc_bins_df.to_csv('/work/nc_by_distance_bin.csv', index=False)
