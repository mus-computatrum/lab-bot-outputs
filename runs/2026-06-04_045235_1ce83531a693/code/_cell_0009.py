
# NOTE: In WMB taxonomy, "Sst" sits at the *subclass* level (not class).
# The cortical Sst subclasses are:
#   "053 Sst Gaba"      (CTX-MGE GABA class = "07 CTX-MGE GABA")
#   "056 Sst Chodl Gaba"(CTX-MGE GABA class)
# The ROI for primary visual cortex is "VIS" (finest granularity in this dataset).

# Step 1: Build cluster_alias → supertype map for Sst subclasses only
# Restrict to CTX-MGE GABA class (cortical Sst) — "265 PB Sst" is pons/hindbrain
sst_cortex_piv = piv[piv["class"] == "07 CTX-MGE GABA"][piv["subclass"].str.contains("Sst", na=False)].copy()
print(f"Cortical Sst clusters in taxonomy: {len(sst_cortex_piv)}")
print("Unique supertypes:", sorted(sst_cortex_piv["supertype"].unique()))
