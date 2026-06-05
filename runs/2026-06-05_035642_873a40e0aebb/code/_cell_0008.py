
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad
import scanpy as sc
import pandas as pd

print("imports done")

adata = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad")
print("loaded adata:", adata.shape)
