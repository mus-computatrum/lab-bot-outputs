
# ── 4. Subset to SST cells ────────────────────────────────────────────────────
import scipy.sparse as sp

# Mouse SST (VISp only, consistent with prior analyses)
mask_m = (adata_m.obs['cell_subclass'] == 'Sst') & (adata_m.obs['dissected_region'] == 'VISp')
sst_m = adata_m[mask_m, mouse_found].copy()
print(f"Mouse SST VISp: {sst_m.shape}")

# Marmoset SST (includes 'Sst' and 'Sst Chodl' subclasses)
subclasses_sst_mar = [s for s in adata_mar.obs['Subclass'].cat.categories if 'Sst' in s]
print(f"Marmoset SST subclasses: {subclasses_sst_mar}")
mask_mar = adata_mar.obs['Subclass'].isin(subclasses_sst_mar)
# Get ensembl IDs for found human genes
mar_ensembl_ids = [mar_sym2ens[g] for g in mar_found_syms]
sst_mar = adata_mar[mask_mar, mar_ensembl_ids].copy()
print(f"Marmoset SST: {sst_mar.shape}")
print(f"Marmoset SST subclass breakdown:\n{adata_mar.obs.loc[mask_mar, 'Subclass'].value_counts()}")
