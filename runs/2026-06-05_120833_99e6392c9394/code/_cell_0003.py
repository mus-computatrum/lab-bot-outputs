
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import matplotlib
matplotlib.use("Agg")
import anndata as ad
import pandas as pd
import matplotlib.pyplot as plt

# Load V1-only object (the recommended access point per dataset card)
adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print("Shape:", adata.shape)
print("obs cols:", list(adata.obs.columns))
