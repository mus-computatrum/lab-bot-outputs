import pandas as pd
import numpy as np

# Build ttype array aligned to cells
cell_ttypes = np.array([id2ttype[c] for c in common_cells])
unique_ttypes = sorted(set(cell_ttypes))
gene_names = counts.index.tolist()

print(f"Unique t-types: {len(unique_ttypes)}")

# For each t-type: cell count + mean log1p expression → top 3 genes
records = []
for ttype in unique_ttypes:
    mask = cell_ttypes == ttype
    n_cells = mask.sum()
    mean_expr = log1p_counts[:, mask].mean(axis=1)          # shape (genes,)
    top3_idx = np.argpartition(mean_expr, -3)[-3:]
    top3_idx = top3_idx[np.argsort(mean_expr[top3_idx])[::-1]]  # descending
    records.append({
        'ttype': ttype,
        'n_cells': int(n_cells),
        'marker1': gene_names[top3_idx[0]],
        'marker2': gene_names[top3_idx[1]],
        'marker3': gene_names[top3_idx[2]],
    })

df_out = pd.DataFrame(records)
print(df_out.to_string(index=False))
