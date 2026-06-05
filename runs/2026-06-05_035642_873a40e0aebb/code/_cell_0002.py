
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad

adata = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad")
print("Shape:", adata.shape)
print("\nObs columns:", adata.obs.columns.tolist())
print("\nFirst few obs rows:")
print(adata.obs.head(3))
