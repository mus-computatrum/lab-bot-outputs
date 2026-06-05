import anndata as ad

adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print(adata)
print("\n--- obs columns ---")
print(list(adata.obs.columns))
print("\n--- first few rows ---")
print(adata.obs.head(3))
