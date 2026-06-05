
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad

adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print(adata)
print("\nobs columns:", list(adata.obs.columns))
print("n_obs:", adata.n_obs)
