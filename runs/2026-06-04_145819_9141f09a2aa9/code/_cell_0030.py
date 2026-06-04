
# Step 2: Load VIS cells from parquet and merge with SST taxonomy
vis_cells = vis_part[['cell_label', 'cluster_alias']].copy()
print(f"VIS cells: {len(vis_cells)}")

# SST cluster aliases set
sst_aliases = set(sst_pivoted['cluster_alias'].astype(str))
print(f"SST cluster_aliases (as strings): {sorted(list(sst_aliases))[:10]}")

# Check type
print(f"\nvis_cells cluster_alias dtype: {vis_cells['cluster_alias'].dtype}")
print(f"sst_pivoted cluster_alias dtype: {sst_pivoted['cluster_alias'].dtype}")
print(f"\nSample vis cluster_alias: {vis_cells['cluster_alias'].head(5).tolist()}")
print(f"Sample sst cluster_alias: {sst_pivoted['cluster_alias'].head(5).tolist()}")
