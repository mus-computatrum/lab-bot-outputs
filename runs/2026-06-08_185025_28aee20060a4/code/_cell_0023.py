import anndata as ad, scanpy as sc
for p in ['/work/gse232200_snapatac.h5ad','/work/gse136802_scrna.h5ad','/work/gse136802_atac.h5ad']:
    a=ad.read_h5ad(p, backed='r')
    print(f"{p}\n   shape={a.shape} obs={list(a.obs.columns)[:6]}... layers={list(a.layers.keys())}")
    a.file.close()
