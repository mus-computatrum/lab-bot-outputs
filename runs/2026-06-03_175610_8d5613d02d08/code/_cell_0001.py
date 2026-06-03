
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

import anndata as ad
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── 1. Load Tasic 2018 (mouse VISp only) ──────────────────────────────────────
print("Loading Tasic 2018...")
adata_m = ad.read_h5ad("/data/tasic2018-v1/tasic2018_full_counts.h5ad")
print(f"Mouse: {adata_m.shape}, obs cols: {list(adata_m.obs.columns[:10])}")
print(f"var_names sample: {list(adata_m.var_names[:5])}")
print(f"Cell subclass values: {adata_m.obs['cell_subclass'].unique()[:8]}")
