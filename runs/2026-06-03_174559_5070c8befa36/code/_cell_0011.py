
# ── Indistinguishability test (shared clusters only) ─────────────────────────
# For each marker: across all shared clusters, compute max |VISp_mean - ALM_mean|
# and max |VISp_frac - ALM_frac|
# Thresholds: mean diff < 0.2 AND frac diff < 0.05 → "indistinguishable"

indist_results = {}
for marker in markers:
    diffs_mean = []
    diffs_frac = []
    for clust in sorted(both):
        v_mean = visp_summary.loc[clust, f'mean_log_{marker}']
        a_mean = alm_summary.loc[clust, f'mean_log_{marker}']
        v_frac = visp_summary.loc[clust, f'frac_{marker}']
        a_frac = alm_summary.loc[clust, f'frac_{marker}']
        diffs_mean.append(abs(v_mean - a_mean))
        diffs_frac.append(abs(v_frac - a_frac))

    max_mean_diff = max(diffs_mean)
    max_frac_diff = max(diffs_frac)
    avg_mean_diff = np.mean(diffs_mean)
    avg_frac_diff = np.mean(diffs_frac)
    flag = (max_mean_diff < 0.2) and (max_frac_diff < 0.05)
    indist_results[marker] = {
        'max_mean_diff': max_mean_diff,
        'avg_mean_diff': avg_mean_diff,
        'max_frac_diff': max_frac_diff,
        'avg_frac_diff': avg_frac_diff,
        'indistinguishable': flag
    }
    print(f"{marker:8s}  max_Δmean={max_mean_diff:.3f}  avg_Δmean={avg_mean_diff:.3f}"
          f"  max_Δfrac={max_frac_diff:.3f}  avg_Δfrac={avg_frac_diff:.3f}"
          f"  → {'INDISTINGUISHABLE' if flag else 'DISTINGUISHABLE'}")
