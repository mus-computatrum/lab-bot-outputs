
# Good - both are int64. Filter VIS cells to SST only, then merge with supertype labels
sst_vis_cells = vis_cells[vis_cells['cluster_alias'].isin(sst_pivoted['cluster_alias'])]
print(f"SST cells in VIS region: {len(sst_vis_cells)}")

# Merge to get supertype labels
sst_alias_to_supertype = sst_pivoted[['cluster_alias', 'supertype', 'subclass']].drop_duplicates()
sst_vis_merged = sst_vis_cells.merge(sst_alias_to_supertype, on='cluster_alias', how='left')
print(f"After merge: {len(sst_vis_merged)}")
print(sst_vis_merged.head(5))
