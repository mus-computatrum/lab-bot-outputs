
# Step 3: Count by supertype, compute fractions, rank, take top 10
supertype_counts = (
    sst_vis_merged
    .groupby('supertype')
    .size()
    .reset_index(name='n_cells_in_visp')
    .sort_values('n_cells_in_visp', ascending=False)
    .reset_index(drop=True)
)

total_sst = supertype_counts['n_cells_in_visp'].sum()
supertype_counts['fraction_of_visp_sst'] = (supertype_counts['n_cells_in_visp'] / total_sst).round(4)

print(f"Total SST cells in VIS/VISp: {total_sst}")
print(f"Total supertypes: {len(supertype_counts)}")
print("\nAll supertypes ranked:")
print(supertype_counts.to_string())
