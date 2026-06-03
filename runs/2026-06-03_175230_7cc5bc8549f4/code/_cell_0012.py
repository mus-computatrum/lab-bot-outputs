
import anndata as ad
import numpy as np
import os

fpath = "/work/staged/marmoset-cortical-atlas/marmoset_MTG_Jorstad2023.h5ad"
print(f"File size: {os.path.getsize(fpath)/1e9:.3f} GB")
adata = ad.read_h5ad(fpath, backed='r')  # backed mode to avoid loading all into RAM
print(f"\n=== AnnData Shape ===")
print(f"  Cells (obs):  {adata.n_obs:,}")
print(f"  Genes (vars): {adata.n_vars:,}")
print(f"\n=== obs columns ===")
print(list(adata.obs.columns))
print(f"\n=== var columns ===")
print(list(adata.var.columns))
print(f"\n=== uns keys ===")
print(list(adata.uns.keys()))
print(f"\n=== obsm keys ===")
print(list(adata.obsm.keys()))
