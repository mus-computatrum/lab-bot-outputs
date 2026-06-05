
# Load the V1-only processed object (as specified by dataset card access snippet)
adata_v1 = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print("V1 shape:", adata_v1.shape)
print("Obs columns:", list(adata_v1.obs.columns))
# Preview cluster field
if "cell_cluster" in adata_v1.obs.columns:
    print("\ncell_cluster sample:", adata_v1.obs["cell_cluster"].value_counts().head(5))
