
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

# Load the V1-only, analysis-ready object
adata_v1 = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")
print("V1 shape:", adata_v1.shape)
print("obs cols:", list(adata_v1.obs.columns))
