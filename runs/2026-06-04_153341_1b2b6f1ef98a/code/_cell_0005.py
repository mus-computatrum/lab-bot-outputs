
# Filter to VIS region
vis_cells = meta[meta['region_of_interest_acronym'] == 'VIS'].copy()
print(f"VIS cells: {len(vis_cells):,}")

# Filter to Sst clusters (cortical)
vis_sst = vis_cells[vis_cells['cluster_alias'].isin(sst_aliases)].copy()
print(f"VIS Sst cells: {len(vis_sst):,}")

# Map cluster_alias -> supertype
vis_sst['supertype'] = vis_sst['cluster_alias'].map(alias_to_supertype)
print(f"Any unmapped? {vis_sst['supertype'].isna().sum()}")
