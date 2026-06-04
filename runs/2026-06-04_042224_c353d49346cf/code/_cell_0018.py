# Compute per-ttype: cell count + top 3 genes by mean log1p expression
records = []
for ttype in unique_ttypes:
    mask = cell_ttypes_arr == ttype
    n_cells = int(mask.sum())
    mean_expr = log1p_mat[:, mask].mean(axis=1)              # shape (n_genes,)
    top3_idx = np.argpartition(mean_expr, -3)[-3:]
    top3_idx = top3_idx[np.argsort(mean_expr[top3_idx])[::-1]]  # rank descending
    records.append({
        'ttype': ttype,
        'n_cells': n_cells,
        'marker1': gene_names[top3_idx[0]],
        'marker2': gene_names[top3_idx[1]],
        'marker3': gene_names[top3_idx[2]],
        '_m1_val': round(float(mean_expr[top3_idx[0]]), 3),
        '_m2_val': round(float(mean_expr[top3_idx[1]]), 3),
        '_m3_val': round(float(mean_expr[top3_idx[2]]), 3),
    })

df_out = pd.DataFrame(records)
print(df_out.to_string(index=False))