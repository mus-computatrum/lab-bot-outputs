import numpy as np, scipy.sparse as sp
# --- normalized layer for scRNA (raw counts kept in X and layers['counts']) ---
rna.layers['counts']=rna.X.copy()
counts=np.asarray(rna.X.sum(1)).ravel(); counts[counts==0]=1
norm=sp.diags(1e4/counts).dot(rna.X).tocsr()
norm.data=np.log1p(norm.data)
rna.layers['lognorm']=norm
rna.uns['normalization']='layers[counts]=raw; layers[lognorm]=log1p(CP10k); X=raw counts'
rna.write('/work/gse136802_scrna.h5ad')
print("scRNA re-saved with counts+lognorm layers", rna.shape)

# --- ATAC pseudobulk h5ad ---
import pandas as pd, gzip, anndata as ad
base='/work/staged/hrvatin-2019-pesca-interneuron'
cnt=pd.read_csv(gzip.open(base+'/GSE136802_atac_master_counts.csv.gz','rt'), index_col=0)
binr=pd.read_csv(gzip.open(base+'/GSE136802_atac_master_binary_peak_table.csv.gz','rt'), index_col=0)
gres=pd.read_csv(gzip.open(base+'/GSE136802_S2_annotated_gres.csv.gz','rt'), index_col=0)
print("counts:",cnt.shape,"binary:",binr.shape,"gres:",gres.shape)
print("counts cols:",list(cnt.columns))
print("binary aligns:", binr.shape==cnt.shape and (binr.index==cnt.index).all())

# AnnData: obs = 6 pseudobulk samples, var = peaks
X=cnt.T.values.astype(np.float32)            # 6 samples x Npeaks
obs=pd.DataFrame(index=cnt.columns)
obs['celltype']=[c.split('_')[1] for c in obs.index]
obs['replicate']=[c.split('_')[2] for c in obs.index]
obs['region']=[c.split('_')[0] for c in obs.index]
var=pd.DataFrame(index=cnt.index)
# attach GRE annotations to the subset of peaks that are annotated enhancers
for col in ['Chr','Start','End','Annotation','Gene Name','Name','ATAC_Specificity','PESCA_Specificity']:
    var[col.replace(' ','_')]=gres[col].reindex(var.index)
var['is_annotated_GRE']=var.index.isin(gres.index)
atac=ad.AnnData(sp.csr_matrix(X), obs=obs, var=var)
atac.layers['binary']=sp.csr_matrix(binr.T.reindex(index=cnt.columns)[cnt.index].values.astype(np.float32))
atac.uns['description']='Pseudobulk ATAC master peak x sample count matrix (PESCA, Hrvatin 2019). X=fragment counts; layers[binary]=binary peak calls.'
atac.write('/work/gse136802_atac.h5ad')
print("\nATAC saved:",atac.shape,"| GREs annotated:",int(atac.var['is_annotated_GRE'].sum()))
print(atac.obs)
