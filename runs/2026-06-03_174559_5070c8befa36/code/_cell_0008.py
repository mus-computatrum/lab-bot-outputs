
import pandas as pd

markers = ['Calb2', 'Crh', 'Hpse', 'Nos1', 'Pdyn', 'Chrna2']
marker_idx = [list(sst.var_names).index(m) for m in markers]

# Pull obs metadata
obs = sst.obs[['cell_cluster', 'dissected_region']].copy()

# Extract marker expression (cells x markers)
X_markers = X_log[:, marker_idx]  # shape (2551, 6)

# Build per-cell DataFrame
expr_df = pd.DataFrame(X_markers, columns=markers, index=obs.index)
expr_df['cell_cluster'] = obs['cell_cluster'].values
expr_df['region'] = obs['dissected_region'].values

# Compute per (cluster x region) mean and fraction_expressing
rows = []
for (cluster, region), grp in expr_df.groupby(['cell_cluster', 'region'], observed=True):
    n = len(grp)
    row = {'cell_cluster': cluster, 'region': region, 'n_cells': n}
    for m in markers:
        vals = grp[m].values
        row[f'mean_log_{m}'] = vals.mean()
        row[f'frac_{m}'] = (vals > 0).mean()
    rows.append(row)

summary = pd.DataFrame(rows)
summary = summary.sort_values(['cell_cluster', 'region']).reset_index(drop=True)
print(f"Summary shape: {summary.shape}")
print("\nFirst 6 rows:")
print(summary.head(6).to_string())
print("\nClusters present per region:")
print(summary.groupby('region')['cell_cluster'].count())
