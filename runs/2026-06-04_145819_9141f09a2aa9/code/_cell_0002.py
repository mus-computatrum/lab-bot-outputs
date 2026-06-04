
import pandas as pd
import numpy as np

base = "/data/yao2023-wmb-10x/_abc_cache"

# Load cell metadata
cell_meta = pd.read_csv(f"{base}/metadata/WMB-10X/20241115/cell_metadata.csv", index_col=0)
print("cell_meta shape:", cell_meta.shape)
print("columns:", cell_meta.columns.tolist())
print("\nFirst few rows:")
print(cell_meta.head(2))
