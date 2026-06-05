
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

import anndata as ad

adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print(f"Shape: {adata.shape}")
print(f"\nobs columns:\n{list(adata.obs.columns)}")
