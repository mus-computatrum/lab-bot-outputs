
# ── 3. Define target genes and find them in each dataset ──────────────────────
MOUSE_GENES = ['Chrm1','Chrm2','Chrm3','Chrm4','Chrna2','Chrna4','Chrna5','Chrna7']
# Human orthologues (uppercase for marmoset dataset which uses human symbols)
HUMAN_GENES = ['CHRM1','CHRM2','CHRM3','CHRM4','CHRNA2','CHRNA4','CHRNA5','CHRNA7']

# Mouse var_names are gene symbols - check presence
mouse_found = [g for g in MOUSE_GENES if g in adata_m.var_names]
mouse_missing = [g for g in MOUSE_GENES if g not in adata_m.var_names]
print("Mouse found:", mouse_found)
print("Mouse missing:", mouse_missing)

# Marmoset: build symbol -> ensembl map
mar_sym2ens = dict(zip(adata_mar.var['feature_name'], adata_mar.var_names))
mar_found_syms = [g for g in HUMAN_GENES if g in mar_sym2ens]
mar_missing_syms = [g for g in HUMAN_GENES if g not in mar_sym2ens]
print("\nMarmoset found (by human symbol):", mar_found_syms)
print("Marmoset missing:", mar_missing_syms)

# For missing, try case-insensitive search in feature_name
if mar_missing_syms:
    fn_lower = adata_mar.var['feature_name'].str.upper()
    for g in mar_missing_syms:
        matches = adata_mar.var.loc[fn_lower == g.upper(), 'feature_name'].tolist()
        print(f"  Case-insensitive match for {g}: {matches}")
