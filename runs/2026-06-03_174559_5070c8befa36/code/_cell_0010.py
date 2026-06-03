
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np

markers = ['Calb2', 'Crh', 'Hpse', 'Nos1', 'Pdyn', 'Chrna2']

# ── Build ordered cluster list ───────────────────────────────────────────────
# Sort by total Calb2 mean in VISp for a sensible Y ordering
visp_summary = summary[summary['region'] == 'VISp'].set_index('cell_cluster')
alm_summary  = summary[summary['region'] == 'ALM'].set_index('cell_cluster')

# All clusters that appear in either region, sorted by VISp Calb2 (descending)
all_clusters = sorted(both | visp_only | alm_only,
                      key=lambda c: visp_summary.loc[c, 'mean_log_Calb2']
                                    if c in visp_summary.index else 0,
                      reverse=True)

# ── Layout ───────────────────────────────────────────────────────────────────
n_clusters = len(all_clusters)   # 21
n_markers  = len(markers)        # 6

# Two panels side by side (VISp left, ALM right)
fig, axes = plt.subplots(1, 2, figsize=(14, 10), sharey=True,
                         gridspec_kw={'wspace': 0.08})

# Colour map and normalisation shared across both panels
vmin, vmax = 0.0, 3.5
cmap = plt.get_cmap('Reds')
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

def draw_panel(ax, region_summary, region_name, clusters, draw_colorbar=False):
    ax.set_facecolor('#f8f8f8')
    ax.set_title(region_name, fontsize=13, fontweight='bold', pad=8)

    for ci, clust in enumerate(clusters):
        y = n_clusters - 1 - ci   # top-to-bottom
        for mi, marker in enumerate(markers):
            if clust in region_summary.index:
                mean_val = region_summary.loc[clust, f'mean_log_{marker}']
                frac_val = region_summary.loc[clust, f'frac_{marker}']
            else:
                # cluster absent in this region → grey hollow circle
                mean_val = np.nan
                frac_val = 0.0

            if np.isnan(mean_val):
                ax.scatter(mi, y, s=70, facecolors='none',
                           edgecolors='#bbbbbb', linewidths=0.8, zorder=3)
            else:
                size = frac_val ** 0.5 * 300   # scale by sqrt(fraction)
                color = cmap(norm(mean_val))
                ax.scatter(mi, y, s=size, color=color, zorder=3,
                           edgecolors='#444444', linewidths=0.4)

    # Axes formatting
    ax.set_xlim(-0.6, n_markers - 0.4)
    ax.set_ylim(-0.6, n_clusters - 0.4)
    ax.set_xticks(range(n_markers))
    ax.set_xticklabels(markers, rotation=45, ha='right', fontsize=10)
    ax.set_yticks(range(n_clusters))
    ax.set_yticklabels([clusters[n_clusters - 1 - i] for i in range(n_clusters)],
                       fontsize=8.5)
    ax.grid(True, color='white', linewidth=0.8)
    for spine in ax.spines.values():
        spine.set_visible(False)

draw_panel(axes[0], visp_summary, 'VISp', all_clusters)
draw_panel(axes[1], alm_summary,  'ALM',  all_clusters)
axes[1].set_yticklabels([])  # shared y axis; labels only on left

# ── Legend for dot size ──────────────────────────────────────────────────────
fracs  = [0.25, 0.50, 0.75, 1.00]
labels = ['25 %', '50 %', '75 %', '100 %']
legend_handles = [
    plt.scatter([], [], s=f**0.5*300, color='#888888',
                edgecolors='#444', linewidths=0.5, label=l)
    for f, l in zip(fracs, labels)
]
axes[1].legend(handles=legend_handles, title='Fraction\nexpressing',
               bbox_to_anchor=(1.02, 0.55), loc='upper left',
               frameon=True, fontsize=8, title_fontsize=8.5)

# ── Colour bar ───────────────────────────────────────────────────────────────
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=axes[1], shrink=0.35, aspect=15,
                    location='right', pad=0.22)
cbar.set_label('Mean log\n(CPM+1)', fontsize=8.5)
cbar.ax.tick_params(labelsize=7.5)

fig.suptitle(
    'SST interneuron subtypes — 6 marker genes\nVISp vs. ALM (Tasic 2018, log CPM+1)',
    fontsize=12, y=1.01
)

plt.savefig('/work/sst_subtype_dotplot.png', dpi=160, bbox_inches='tight')
plt.close()
print("Saved /work/sst_subtype_dotplot.png")
