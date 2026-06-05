
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad
import scanpy as sc
import pandas as pd

print("Loading data...")
adata = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad")
print(f"Loaded: {adata.shape}")
sst = adata[adata.obs['cell_subclass'] == 'Sst'].copy()
print(f"SST cells: {sst.shape}")

target_clusters = ['Sst Chrna2 Glra3', 'Sst Chrna2 Ptgdr']
group_name = 'Sst_Chrna2'
sst.obs['group'] = sst.obs['cell_cluster'].apply(
    lambda x: group_name if x in target_clusters else 'other_sst')

print(sst.obs['group'].value_counts())
