
# ── 6. Build merged CSV ──────────────────────────────────────────────────────
# Add CHRM4 as NaN row for marmoset (not in panel)
chrm4_row = pd.DataFrame({
    'gene': ['CHRM4'], 'species': ['marmoset'],
    'mean_expr': [np.nan], 'pct_expr': [np.nan],
    'n_cells': [3474], 'gene_upper': ['CHRM4']
})
summary_mar_full = pd.concat([summary_mar, chrm4_row], ignore_index=True)

# Merge on unified gene symbol
merged = pd.merge(
    summary_mouse[['gene_upper','species','mean_expr','pct_expr','n_cells']].rename(columns={'mean_expr':'mean_expr_mouse','pct_expr':'pct_expr_mouse','n_cells':'n_cells_mouse'}),
    summary_mar_full[['gene_upper','mean_expr','pct_expr','n_cells']].rename(columns={'mean_expr':'mean_expr_marmoset','pct_expr':'pct_expr_marmoset','n_cells':'n_cells_marmoset'}),
    on='gene_upper', how='outer'
)
merged = merged.rename(columns={'gene_upper': 'gene'}).drop(columns=['species'])
merged = merged.sort_values('gene')

# Also produce long-form CSV for flexibility
rows = []
for _, r in summary_mouse.iterrows():
    rows.append({'gene': r['gene_upper'], 'species': 'mouse', 'mean_expr_log1p_cpm10k': r['mean_expr'], 'pct_expressing': r['pct_expr'], 'n_cells': int(r['n_cells']), 'mouse_gene_symbol': r['gene'], 'marmoset_gene_symbol': r['gene']})
for _, r in summary_mar_full.iterrows():
    rows.append({'gene': r['gene_upper'], 'species': 'marmoset', 'mean_expr_log1p_cpm10k': r['mean_expr'], 'pct_expressing': r['pct_expr'], 'n_cells': int(r['n_cells']), 'mouse_gene_symbol': r['gene'].capitalize() if pd.notna(r['gene']) else np.nan, 'marmoset_gene_symbol': r['gene']})

out_df = pd.DataFrame(rows).sort_values(['gene','species'])
out_df.to_csv('/work/chrm_mouse_marmoset.csv', index=False)
print("Saved /work/chrm_mouse_marmoset.csv")
print(out_df.to_string(index=False))
