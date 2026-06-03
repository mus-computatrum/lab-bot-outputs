
# Final verification: confirm we can load from the registered read-only path
import anndata as ad

adata_check = ad.read_h5ad("/data/marmoset-cortical-atlas/marmoset_MTG_Jorstad2023.h5ad", backed='r')
print(f"✓ Registered dataset loads OK from /data/marmoset-cortical-atlas/")
print(f"  Shape: {adata_check.n_obs:,} cells × {adata_check.n_vars:,} genes")
print(f"  Organism: {adata_check.uns.get('organism','?')}")
print(f"  Tissue: {adata_check.obs['tissue'].unique().tolist()}")
print(f"\n  First 10 cluster labels:")
for c in sorted(adata_check.obs['Cluster'].unique())[:10]:
    n = (adata_check.obs['Cluster'] == c).sum()
    print(f"    {c}: {n:,} cells")
    
print(f"\n  All subclasses:")
for s, n in adata_check.obs['Subclass'].value_counts().items():
    print(f"    {s}: {n:,}")
adata_check.file.close()
