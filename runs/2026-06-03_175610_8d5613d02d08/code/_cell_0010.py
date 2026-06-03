
# Check what assay the marmoset data uses
print("Marmoset assay term:", adata_mar.obs['assay_ontology_term_id'].unique().tolist())
# EFO:0009899 = 10x 3' v2; EFO:0009922 = 10x 3' v3; EFO:0030003 = SMART-seq v4 etc.
if 'assay' in adata_mar.obs.columns:
    print("Assay:", adata_mar.obs['assay'].unique().tolist())
