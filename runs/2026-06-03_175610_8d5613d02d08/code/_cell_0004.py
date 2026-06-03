
# Search for any CHRM4-like entries in marmoset var
import re
chrm4_candidates = adata_mar.var[adata_mar.var['feature_name'].str.contains('CHRM4', case=False, na=False)]
print("CHRM4 candidates in marmoset:", chrm4_candidates[['feature_name','gene']].to_string())

# Also check gene column
chrm4_gene_col = adata_mar.var[adata_mar.var['gene'].str.contains('CHRM4', case=False, na=False)]
print("CHRM4 gene col candidates:", chrm4_gene_col[['feature_name','gene']].head(10))
