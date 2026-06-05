import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import pandas as pd
import anndata as ad

# Load the full h5ad and filter to VISp only
adata = ad.read_h5ad("/data/tasic2018-v1/tasic2018_full_counts.h5ad")
print("Full shape:", adata.shape)
print("Obs columns:", list(adata.obs.columns))
print("dissected_region values:", adata.obs["dissected_region"].value_counts().to_dict())
