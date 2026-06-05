
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"

import anndata as ad
import scanpy as sc
import pandas as pd
import numpy as np

# backed='r': only reads metadata at open time; .to_memory() on the SST slice only
adata_b = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad", backed='r')
sst_mask = adata_b.obs['cell_subclass'] == 'Sst'
sst = adata_b[sst_mask].to_memory()
adata_b.file.close()  # release the file handle

print("SST shape:", sst.shape)
print("Clusters:\n", sst.obs['cell_cluster'].value_counts())
