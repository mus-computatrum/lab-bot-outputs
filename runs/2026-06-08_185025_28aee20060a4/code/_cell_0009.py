# add full-peak coordinates + conservation from binary table to var
for col in ['Chr','Start','End','MeanCons','MinCons','MaxCons']:
    atac.var[col]=binr[col].reindex(atac.var.index).values
# prefer full coords; keep GRE-specific annotation columns too
atac.var=atac.var.rename(columns={'Chr':'chr','Start':'start','End':'end'})
# drop the now-redundant GRE coord cols (Chr_/Start_/End_ from gres were same name->already 'Chr'? they were 'Chr','Start','End' -> overwritten). 
print(atac.var.columns.tolist())
print(atac.var.head(3))
print("\npeaks with coords:", atac.var['chr'].notna().sum(),"/",atac.n_vars)
atac.write('/work/gse136802_atac.h5ad')
print("ATAC re-saved")
