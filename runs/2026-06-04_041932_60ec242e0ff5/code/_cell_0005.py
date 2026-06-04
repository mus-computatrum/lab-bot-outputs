import pandas as pd

# Compute per-cell means (avoid records with 0 frames)
cell_means = []
for r in records:
    if r['run_n'] > 0 and r['stat_n'] > 0:
        cell_means.append({
            'ttype':     r['ttype'],
            'run_mean':  r['run_sum'] / r['run_n'],
            'stat_mean': r['stat_sum'] / r['stat_n'],
        })

df_cells = pd.DataFrame(cell_means)

# Aggregate by ttype: mean of per-cell means + cell count
agg = df_cells.groupby('ttype').agg(
    n_cells=('run_mean', 'count'),
    mean_run=('run_mean', 'mean'),
    mean_stat=('stat_mean', 'mean'),
).reset_index()

agg['delta'] = agg['mean_run'] - agg['mean_stat']
agg = agg.sort_values('delta', key=abs, ascending=False).reset_index(drop=True)

print("All SST t-types by |delta| (run - stat-desync):")
print(agg.to_string(float_format='%.4f'))

# Save CSV (top 10 or all if < 10)
top10 = agg.head(10).copy()
top10.to_csv('/work/sst_state_modulation.csv', index=False)
print(f"\nSaved /work/sst_state_modulation.csv ({len(top10)} rows)")
