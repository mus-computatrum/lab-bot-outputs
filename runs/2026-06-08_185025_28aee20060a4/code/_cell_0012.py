import numpy as np, scipy.sparse as sp, pandas as pd, anndata as ad, h5py, gzip

def decode(arr): return np.array([x.decode() if isinstance(x,bytes) else str(x) for x in arr])

def build_biorep(f, label, sc_csv):
    bd_name=decode(np.array(f['BD/name']))
    nbar=len(bd_name)
    idx=f['PM/idx'][:].astype(np.int64)-1   # cell (0-based)
    idy=f['PM/idy'][:].astype(np.int64)-1   # peak (0-based)
    cnt=f['PM/count'][:]
    npeak=f['PM/peakStart'].shape[0]
    assert idx.max()<nbar and idy.max()<npeak, (idx.max(),nbar,idy.max(),npeak)
    X=sp.coo_matrix((cnt,(idx,idy)), shape=(nbar,npeak)).tocsr()
    # obs from BD QC fields
    obs=pd.DataFrame(index=[f"{label}|{b}" for b in bd_name])
    for k in ['TN','UM','PP','UQ','SE','SA','PE','PL','US','CM']:
        if f'BD/{k}' in f: obs[k]=f[f'BD/{k}'][:]
    obs['barcode']=bd_name; obs['biorep']=label
    # join singlecell.csv QC (on barcode)
    sc=sc_csv.set_index('barcode')
    keep=['passed_filters','peak_region_fragments','TSS_fragments','promoter_region_fragments',
          'enhancer_region_fragments','is__cell_barcode','cell_id']
    j=sc.reindex(bd_name)[keep]; j.index=obs.index
    obs=pd.concat([obs,j],axis=1)
    return X,obs

f1=h5py.File('/work/GSM7317753_biorep1.snap','r')
f2=h5py.File('/work/GSM7317754_biorep2.snap','r')
sc1=pd.read_csv(gzip.open(base+'/GSM7317753_biorep1_singlecell.csv.gz','rt'))
sc2=pd.read_csv(gzip.open(base+'/GSM7317754_biorep2_singlecell.csv.gz','rt'))

X1,o1=build_biorep(f1,'biorep1',sc1)
X2,o2=build_biorep(f2,'biorep2',sc2)
print("biorep1:",X1.shape,"nnz",X1.nnz,"| biorep2:",X2.shape,"nnz",X2.nnz)

# var from biorep1 peaks (identical across reps)
chrom=decode(np.array(f1['PM/peakChrom'])); st=f1['PM/peakStart'][:]; en=f1['PM/peakEnd'][:]
var=pd.DataFrame({'chr':chrom,'start':st,'end':en})
var.index=[f"{c}:{s}-{e}" for c,s,e in zip(chrom,st,en)]

X=sp.vstack([X1,X2]).tocsr()
obs=pd.concat([o1,o2])
atac=ad.AnnData(X.astype(np.float32), obs=obs, var=var)
atac.uns['description']='Green et al 2023 (GSE232200) snATAC-seq of cortical (PPC) Gad2+ inhibitory neurons; peak x cell matrix from SnapATAC .snap PM group, 2 bioreps merged.'
atac.uns['gsm']={'biorep1':'GSM7317753','biorep2':'GSM7317754'}
print("\nMerged:",atac.shape,"nnz",atac.X.nnz)
print(atac.obs[['biorep','passed_filters','peak_region_fragments','UQ']].groupby(atac.obs['biorep']).median())
atac.write('/work/gse232200_snapatac.h5ad')
print("saved /work/gse232200_snapatac.h5ad")
