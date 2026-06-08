import numpy as np, scipy.sparse as sp, pandas as pd, anndata as ad, h5py, gzip
NPK=459912

def dec(arr):
    out=[]
    for x in arr[:]:
        out.append(x.decode() if hasattr(x,'decode') else str(x))
    return np.array(out)

def build_biorep(f, label, sc_csv):
    bd_name=dec(f['BD/name']); nbar=len(bd_name)
    idx=f['PM/idx'][:].astype(np.int64)-1
    idy=f['PM/idy'][:].astype(np.int64)-1
    cnt=f['PM/count'][:]
    keep=idy<NPK
    dropped=(~keep).sum()
    idx,idy,cnt=idx[keep],idy[keep],cnt[keep]
    X=sp.coo_matrix((cnt,(idx,idy)), shape=(nbar,NPK)).tocsr()
    obs=pd.DataFrame(index=[f"{label}|{b}" for b in bd_name])
    for k in ['TN','UM','PP','UQ','SE','SA','PE','PL','US','CM']:
        if f'BD/{k}' in f: obs[k]=f[f'BD/{k}'][:]
    obs['barcode']=bd_name; obs['biorep']=label
    sc=sc_csv.drop_duplicates('barcode').set_index('barcode')
    cols=['passed_filters','peak_region_fragments','TSS_fragments','promoter_region_fragments',
          'enhancer_region_fragments','is__cell_barcode','cell_id']
    j=sc.reindex(bd_name)[cols]; j.index=obs.index
    obs=pd.concat([obs,j],axis=1)
    print(f"{label}: {X.shape} nnz={X.nnz} dropped_orphan_nnz={dropped}")
    return X,obs

X1,o1=build_biorep(f1,'biorep1',sc1)
X2,o2=build_biorep(f2,'biorep2',sc2)

chrom=dec(f1['PM/peakChrom']); st=f1['PM/peakStart'][:]; en=f1['PM/peakEnd'][:]
var=pd.DataFrame({'chr':chrom,'start':st,'end':en})
var.index=[f"{c}:{s}-{e}" for c,s,e in zip(chrom,st,en)]
print("var sample idx:", var.index[:2].tolist(), "| unique chroms:", var['chr'].nunique())

X=sp.vstack([X1,X2]).tocsr()
obs=pd.concat([o1,o2])
atac=ad.AnnData(X.astype(np.float32), obs=obs, var=var)
atac.uns['title']='Green et al 2023 (GSE232200) snATAC-seq of cortical Gad2+ inhibitory neurons (PPC) — peak x cell'
atac.uns['gsm']={'biorep1':'GSM7317753','biorep2':'GSM7317754'}
atac.uns['note']='Built from SnapATAC v1 .snap PM (peak) group, bin/genome mm10. 63 orphan peak indices without stored coords dropped.'
atac.write('/work/gse232200_snapatac.h5ad')
print("\nMERGED:",atac.shape,"nnz",atac.X.nnz)
print(atac.obs.groupby('biorep')[['passed_filters','peak_region_fragments','UQ']].median())
print("saved /work/gse232200_snapatac.h5ad")
