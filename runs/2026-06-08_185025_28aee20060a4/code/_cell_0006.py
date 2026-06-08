import scanpy as sc, anndata as ad, numpy as np, scipy.sparse as sp, pandas as pd, gzip, io, tarfile, os
base='/work/staged/hrvatin-2019-pesca-interneuron'
t=tarfile.open(os.path.join(base,'GSE136802_RAW.tar'))
rna_members=[n for n in t.getnames() if n.endswith('.counts.tsv.gz')]

adatas=[]
for m in sorted(rna_members):
    raw=gzip.decompress(t.extractfile(m).read())
    df=pd.read_csv(io.BytesIO(raw), sep='\t', index_col=0)
    lane=m.split('_WITH')[0].replace('GSM4058339_','')
    df.index=[f"{lane}|{bc}" for bc in df.index]
    a=ad.AnnData(sp.csr_matrix(df.values.astype(np.float32)),
                 obs=pd.DataFrame({'lane':lane}, index=df.index),
                 var=pd.DataFrame(index=df.columns.astype(str)))
    adatas.append(a)
    print(m.split('_WITH')[0], df.shape)

rna = ad.concat(adatas, join='outer', fill_value=0)
rna.obs['gsm']='GSM4058339'; rna.obs['assay']='scRNA-seq (INTACT cortical interneurons)'
print("\nMerged scRNA:", rna.shape, "genes:", rna.n_vars)
print("counts dtype, max:", rna.X.dtype, rna.X.max())
rna.write('/work/gse136802_scrna.h5ad')
print("saved gse136802_scrna.h5ad")
