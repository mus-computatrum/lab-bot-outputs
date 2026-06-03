import anndata as ad
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load the V1-only processed object (recommended by dataset card)
adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print(f"Shape: {adata.shape}")
print(f"obs columns: {list(adata.obs.columns)}")
print(f"\nSample 'cluster' values:")
# Try both possible column names
for col in ["cluster", "cell_cluster", "cell_type"]:
    if col in adata.obs.columns:
        print(f"  Found column '{col}': {adata.obs[col].nunique()} unique values")
        print(f"  Example: {adata.obs[col].value_counts().head(3).to_dict()}")
