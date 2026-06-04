
# Rank supertypes by cell count
supertype_counts = (
    vis_sst.groupby('supertype')
    .size()
    .reset_index(name='n_cells_in_visp')
    .sort_values('n_cells_in_visp', ascending=False)
    .reset_index(drop=True)
)
total_sst = len(vis_sst)
supertype_counts['fraction_of_visp_sst'] = supertype_counts['n_cells_in_visp'] / total_sst

print(f"Total Sst cells in VIS: {total_sst:,}")
print(f"Number of supertypes: {len(supertype_counts)}")
print("\nAll supertypes ranked:")
print(supertype_counts.to_string(index=False))
