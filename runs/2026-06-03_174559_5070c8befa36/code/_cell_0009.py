
# Save CSV
summary.to_csv('/work/sst_subtype_markers_v1_vs_alm.csv', index=False)
print("Saved /work/sst_subtype_markers_v1_vs_alm.csv")

# Which clusters are in both regions vs region-exclusive?
both = set(summary[summary['region']=='VISp']['cell_cluster']) & set(summary[summary['region']=='ALM']['cell_cluster'])
visp_only = set(summary[summary['region']=='VISp']['cell_cluster']) - both
alm_only = set(summary[summary['region']=='ALM']['cell_cluster']) - both
print(f"\nClusters in BOTH regions: {len(both)}")
print(sorted(both))
print(f"\nVISp-only clusters ({len(visp_only)}): {sorted(visp_only)}")
print(f"\nALM-only clusters ({len(alm_only)}): {sorted(alm_only)}")
