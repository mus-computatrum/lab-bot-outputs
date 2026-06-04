
# Fix the chained indexing warning - use proper boolean mask
mask_sst_ctx = (piv["class"] == "07 CTX-MGE GABA") & (piv["subclass"].str.contains("Sst", na=False))
sst_cortex_piv = piv[mask_sst_ctx].copy()
print(f"Cortical Sst clusters: {len(sst_cortex_piv)}")

# Build alias → supertype dict
alias_to_supertype = sst_cortex_piv.set_index("cluster_alias")["supertype"].to_dict()
alias_to_subclass  = sst_cortex_piv.set_index("cluster_alias")["subclass"].to_dict()

# Step 2: filter cells for VIS region + Sst cortical clusters
# VIS = visual areas (closest to VISp in this metadata)
visp_cells = cells[cells["region_of_interest_acronym"] == "VIS"].copy()
print(f"\nAll VIS cells: {len(visp_cells):,}")

# Keep only cells whose cluster_alias is a cortical Sst alias
sst_aliases = set(alias_to_supertype.keys())
visp_sst = visp_cells[visp_cells["cluster_alias"].isin(sst_aliases)].copy()
print(f"VIS Sst cells: {len(visp_sst):,}")

# Attach supertype and subclass labels
visp_sst["supertype"] = visp_sst["cluster_alias"].map(alias_to_supertype)
visp_sst["subclass"]  = visp_sst["cluster_alias"].map(alias_to_subclass)
print("\nSubclass breakdown:")
print(visp_sst["subclass"].value_counts())
