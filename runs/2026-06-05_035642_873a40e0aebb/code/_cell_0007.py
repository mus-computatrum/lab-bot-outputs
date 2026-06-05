
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
import anndata as ad
import scanpy as sc
import pandas as pd

adata = ad.read_h5ad("/data/tasic2018-v1/v1_neurons_proc.h5ad")
sst = adata[adata.obs['cell_subclass'] == 'Sst'].copy()

target_clusters = ['Sst Chrna2 Glra3', 'Sst Chrna2 Ptgdr']
group_name = 'Sst_Chrna2'
sst.obs['group'] = sst.obs['cell_cluster'].apply(
    lambda x: group_name if x in target_clusters else 'other_sst')

sc.tl.rank_genes_groups(sst, groupby='group', groups=[group_name],
                         reference='other_sst', method='wilcoxon',
                         key_added='markers', n_genes=20)

result = sc.get.rank_genes_groups_df(sst, group=group_name, key='markers')
top5 = result.head(5)[['names', 'scores', 'pvals_adj']].copy()
top5.columns = ['gene', 'score', 'pval_adj']
top5['subclass'] = group_name
print(top5.to_csv(index=False))
