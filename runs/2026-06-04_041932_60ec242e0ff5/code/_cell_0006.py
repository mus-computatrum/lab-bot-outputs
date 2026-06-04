import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

df = agg.copy()

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(df))
width = 0.35

bars_run  = ax.bar(x - width/2, df['mean_run'],  width, label='Running (state 0)',
                   color='#2196F3', edgecolor='white', linewidth=0.5)
bars_stat = ax.bar(x + width/2, df['mean_stat'], width, label='Stat-Desync (state 1)',
                   color='#FF9800', edgecolor='white', linewidth=0.5)

# Annotate delta on top of each pair
for i, (_, row) in enumerate(df.iterrows()):
    ymax = max(row['mean_run'], row['mean_stat']) + 3
    delta_str = f"Δ={row['delta']:+.1f}"
    color = '#1565C0' if row['delta'] > 0 else '#B71C1C'
    ax.text(i, ymax, delta_str, ha='center', va='bottom', fontsize=7.5,
            color=color, fontweight='bold')

# n_cells annotation below x-axis
ax.set_xticks(x)
ax.set_xticklabels(
    [f"{t}\n(n={n})" for t, n in zip(df['ttype'], df['n_cells'])],
    rotation=30, ha='right', fontsize=8.5
)

ax.set_ylabel('Mean Neural Activity (ΔF, a.u.)', fontsize=11)
ax.set_title('SST t-type State Modulation: Running vs. Stationary-Desynchronized\n'
             'Bugeon et al. 2022 — V1 mouse, all sessions pooled',
             fontsize=11, pad=10)
ax.legend(fontsize=10)
ax.set_xlim(-0.6, len(df) - 0.4)
ax.set_ylim(0, df[['mean_run', 'mean_stat']].max().max() * 1.18)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Subtitle: sorted by |delta|
ax.text(0.5, -0.22, 'Sorted by |Δ| = |mean_run − mean_stat|, descending',
        transform=ax.transAxes, ha='center', fontsize=8.5, color='gray')

plt.tight_layout()
plt.savefig('/work/sst_state_modulation_bar.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved /work/sst_state_modulation_bar.png")
