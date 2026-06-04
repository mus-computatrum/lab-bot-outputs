
# The cell_metadata_with_cluster_annotation is a view file not on disk
# Check cell_metadata for any dissection region info
# Also look at the Isocortex h5ad obs metadata for region labels
import anndata as ad

# Load one small h5ad to inspect obs columns
adata1 = ad.read_h5ad(
    "/data/yao2023-wmb-10x/_abc_cache/expression_matrices/WMB-10Xv2/20230630/WMB-10Xv2-Isocortex-1-log2.h5ad",
    backed='r'
)
print("adata1 shape:", adata1.shape)
print("obs columns:", adata1.obs.columns.tolist())
print(adata1.obs.head(3))
