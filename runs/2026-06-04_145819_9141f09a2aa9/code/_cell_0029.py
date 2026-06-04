
# Conclusion: 'VIS' is the finest visual cortex ROI available on disk; 
# it maps to the "VISp dissection region" in the Isocortex subset context.
# 
# Strategy:
# 1. Load VIS partition from parquet (fast)
# 2. Get SST cluster_aliases from pivoted taxonomy (subclass '053 Sst Gaba' 
#    and '056 Sst Chodl Gaba' within the CTX-MGE class)
# 3. Merge and count by supertype

# Step 1: SST cluster aliases from Isocortex-relevant subclasses
# Keep only CTX-MGE Sst (Isocortex Sst interneurons)
sst_pivoted = pivoted[
    pivoted['subclass'].isin(['053 Sst Gaba', '056 Sst Chodl Gaba'])
].copy()
print(f"SST cluster aliases (CTX-MGE): {len(sst_pivoted)}")
print(sst_pivoted['subclass'].value_counts())
print(f"\nUnique supertypes: {sst_pivoted['supertype'].nunique()}")
print(sst_pivoted['supertype'].value_counts().head(10))
