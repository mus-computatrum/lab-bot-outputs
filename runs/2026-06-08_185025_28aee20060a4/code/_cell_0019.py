import numpy as np, scipy.sparse as sp, pandas as pd, anndata as ad, h5py, gzip, gc
NPK=459912
base='/work/staged/green-2023-ppc-inhibitory-snatac'

def dec(arr):
    return np.array([x.decode() if hasattr(x,'decode') else str(x) for x in arr[:]])

def build_one(path, label, sc_path):
    f=h5py.File(path,'r')
    bd=dec(f['BD/name']); nbar=len(bd)
    idx=f['PM/idx'][:].astype(np.int32)-1
    idy=f['PM/idy'][:].astype(np.int32)-1
    cnt=f['PM/count'][:]                      # uint8
    keep=idy<NPK; ndrop=int((~keep).sum())
    idx=idx[keep]; idy=idy[keep]; cnt=cnt[keep]
    X=sp.csr_matrix((cnt.astype(np.float32),(idx,idy)), shape=(nbar,NPK))
    del idx,idy,cnt; gc.collect()
    obs=pd.DataFrame(index=[f"{label}|{b}" for b in bd])
    for k in ['TN','UM','PP','UQ','SE','SA','PE','PL','US','CM']:
        if f'BD/{k}' in f: obs[k]=f[f'BD/{k}'][:]
    obs['barcode']=bd; obs['biorep']=label
    sc=pd.read_csv(gzip.open(sc_path,'rt')).drop_duplicates('barcode').set_index('barcode')
    cols=['passed_filters','peak_region_fragments','TSS_fragments','promoter_region_fragments',
          'enhancer_region_fragments','is__cell_barcode','cell_id']
    j=sc.reindex(bd)[cols]; j.index=obs.index
    obs=pd.concat([obs,j],axis=1); del sc; gc.collect()
    # peaks (only from first file)
    var=None
    if label=='biorep1':
        var=pd.DataFrame({'chr':dec(f['PM/peakChrom']),'start':f['PM/peakStart'][:],'end':f['PM/peakEnd'][:]})
        var.index=[f"{c}:{s}-{e}" for c,s,e in zip(var['chr'],var['start'],var['end'])]
    f.close()
    print(f"{label}: X={X.shape} nnz={X.nnz} orphan_nnz_dropped={ndrop}")
    return X,obs,var

X1,o1,var=build_one(f'{base}/GSM7317753_biorep1.snap','biorep1',f'{base}/GSM7317753_biorep1_singlecell.csv.gz')
gc.collect()
X2,o2,_=build_one(f'{base}/GSM7317754_biorep2.snap','biorep2',f'{base}/GSM7317754_biorep2_singlecell.csv.gz')
gc.collect()
X=sp.vstack([X1,X2]).tocsr(); del X1,X2; gc.collect()
obs=pd.concat([o1,o2])
print("merged X:",X.shape,"nnz",X.nnz,"dtype",X.dtype)
