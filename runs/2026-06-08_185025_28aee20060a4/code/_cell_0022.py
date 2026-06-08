import anndata as ad, gc
atac=ad.AnnData(X, obs=obs, var=var)
atac.uns['title']='Green et al 2023 (GSE232200) snATAC-seq of cortical Gad2+ inhibitory neurons (mouse PPC) — peak x cell'
atac.uns['gsm']={'biorep1':'GSM7317753','biorep2':'GSM7317754'}
atac.uns['genome']='mm10'
atac.uns['source']='SnapATAC v1 .snap PM (peak) group; X = peak fragment counts (uint8 origin, stored float32).'
atac.uns['note']='63 orphan peak indices (idy 459913-459975) lacked stored coordinates and were dropped (~0.008% of nnz).'
print(atac)
print("\nQC medians by biorep:")
print(atac.obs.groupby('biorep')[['UQ','passed_filters','peak_region_fragments']].median())
print("\nis__cell_barcode counts:", atac.obs['is__cell_barcode'].value_counts(dropna=False).to_dict())
atac.write('/work/gse232200_snapatac.h5ad')
import os; print("\nsaved:", os.path.getsize('/work/gse232200_snapatac.h5ad')/1e9,"GB")
del X; gc.collect()
