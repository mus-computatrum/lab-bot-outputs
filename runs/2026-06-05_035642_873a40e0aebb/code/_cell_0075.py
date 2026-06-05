
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

import anndata as ad
import scipy.sparse
import numpy as np

# Load backed (lazy), slice SST only, then pull to memory — ~1.5 GB instead of ~14 GB
adata_backed = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad", backed='r')
print("Full shape:", adata_backed.shape)
print("Obs cols:", list(adata_backed.obs.columns[:5]))

sst_mask = adata_backed.obs['cell_subclass'] == 'Sst'
sst = adata_backed[sst_mask].to_memory()
print("\nSST shape:", sst.shape)
print("X type:", type(sst.X))
print("Sparse?", scipy.sparse.issparse(sst.X))
print("X min/max:", sst.X.min(), sst.X.max())
print("Cluster counts:\n", sst.obs['cell_cluster'].value_counts().head(10))
