
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

import anndata as ad
import pandas as pd

# Load full h5ad, filter to VISp only
adata = ad.read_h5ad("/data/tasic2018-v1/tasic2018_full_counts.h5ad")
print("Full shape:", adata.shape)
print("obs cols:", list(adata.obs.columns))
print("dissected_region values:", adata.obs["dissected_region"].unique())
