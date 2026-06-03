
# Deeper look: per-cluster differences for Hpse (most similar) and Pdyn (most different)
print("=== Hpse per-cluster VISp vs ALM ===")
for clust in sorted(both):
    v = visp_summary.loc[clust, 'mean_log_Hpse']
    a = alm_summary.loc[clust, 'mean_log_Hpse']
    vf = visp_summary.loc[clust, 'frac_Hpse']
    af = alm_summary.loc[clust, 'frac_Hpse']
    print(f"  {clust:30s}  VISp={v:.3f} ({vf:.2f})  ALM={a:.3f} ({af:.2f})  Δmean={abs(v-a):.3f}")

print("\n=== Pdyn per-cluster VISp vs ALM ===")
for clust in sorted(both):
    v = visp_summary.loc[clust, 'mean_log_Pdyn']
    a = alm_summary.loc[clust, 'mean_log_Pdyn']
    vf = visp_summary.loc[clust, 'frac_Pdyn']
    af = alm_summary.loc[clust, 'frac_Pdyn']
    print(f"  {clust:30s}  VISp={v:.3f} ({vf:.2f})  ALM={a:.3f} ({af:.2f})  Δmean={abs(v-a):.3f}")
