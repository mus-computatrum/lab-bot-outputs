import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

fig, ax = plt.subplots(figsize=(9, 5))

# Plot in ascending order so the longest bar is at the top
df_plot = result.sort_values('n_outgoing_syn', ascending=True)
labels = [str(rid) for rid in df_plot['pre_pt_root_id']]
values = df_plot['n_outgoing_syn'].values

colors = plt.cm.viridis_r([v / max(values) for v in values])

bars = ax.barh(labels, values, color=colors, edgecolor='white', linewidth=0.5)

# Value labels on bars
for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 80, bar.get_y() + bar.get_height() / 2,
            f'{val:,}', va='center', ha='left', fontsize=9)

ax.set_xlabel('Number of outgoing synapses', fontsize=11)
ax.set_title('Top 10 axon-proofread V1DD cells by outgoing synapse count', fontsize=12, fontweight='bold')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax.set_xlim(0, max(values) * 1.12)
ax.tick_params(axis='y', labelsize=7.5)
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('/work/v1dd_top_synapse_counts.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved /work/v1dd_top_synapse_counts.png")
