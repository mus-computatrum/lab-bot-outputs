
import anndata as ad
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

print("Loading tasic2018_full_counts.h5ad …")
full = ad.read_h5ad("/data/tasic2018-v1/tasic2018_full_counts.h5ad")
print(full)
print("\n--- .obs columns ---")
print(full.obs.columns.tolist())
print("\n--- .obs head ---")
print(full.obs.head(3))
print("\n--- .var head ---")
print(full.var.head(3))
