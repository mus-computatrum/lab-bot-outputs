
# ── 2. Load Marmoset MTG ──────────────────────────────────────────────────────
print("Loading Marmoset MTG...")
adata_mar = ad.read_h5ad("/data/marmoset-cortical-atlas/marmoset_MTG_Jorstad2023.h5ad")
print(f"Marmoset: {adata_mar.shape}")
print(f"obs cols: {list(adata_mar.obs.columns[:10])}")
print(f"Subclass values: {adata_mar.obs['Subclass'].unique()}")
print(f"var cols: {list(adata_mar.var.columns)}")
print(f"var_names sample: {list(adata_mar.var_names[:5])}")
if 'feature_name' in adata_mar.var.columns:
    print(f"feature_name sample: {list(adata_mar.var['feature_name'][:5])}")
