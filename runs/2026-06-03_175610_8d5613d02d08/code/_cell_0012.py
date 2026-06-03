
# ── 7. Dotplot ────────────────────────────────────────────────────────────────
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
from matplotlib.colors import Normalize

GENE_ORDER = ['CHRM1','CHRM2','CHRM3','CHRM4','CHRNA2','CHRNA4','CHRNA5','CHRNA7']
SPECIES = ['mouse', 'marmoset']
COLORS = {'mouse': '#2196F3', 'marmoset': '#FF7043'}  # blue vs orange-red
YPOS   = {'mouse': 1.0, 'marmoset': 0.0}

# Normalize color scale per species separately using mean_expr
vmin, vmax = 0, 9.5  # log1p(10k+1) ≈ 9.21

fig, ax = plt.subplots(figsize=(10, 3.5))

for si, species in enumerate(SPECIES):
    sp_df = out_df[out_df['species'] == species].set_index('gene').reindex(GENE_ORDER)
    y_base = YPOS[species]
    
    for xi, gene in enumerate(GENE_ORDER):
        row = sp_df.loc[gene]
        mean_e = row['mean_expr_log1p_cpm10k']
        pct    = row['pct_expressing']
        
        if pd.isna(mean_e):
            # Draw X marker for missing gene
            ax.scatter(xi, y_base, marker='x', s=120, color='grey', linewidths=2, zorder=5)
            continue
        
        # Dot size ∝ % expressing (max radius = 0.38 in data units → scale)
        max_size = 600  # pt²
        dot_size = (pct / 100) * max_size
        
        # Color ∝ mean expression (use same colormap for both species)
        cmap = cm.Blues if species == 'mouse' else cm.Oranges
        norm = Normalize(vmin=vmin, vmax=vmax)
        color = cmap(norm(mean_e))
        
        ax.scatter(xi, y_base, s=dot_size, c=[color], edgecolors='k',
                   linewidths=0.5, zorder=5)

# Axes styling
ax.set_xticks(range(len(GENE_ORDER)))
ax.set_xticklabels(GENE_ORDER, rotation=40, ha='right', fontsize=11)
ax.set_yticks([0, 1])
ax.set_yticklabels(['Marmoset\n(MTG, n=3474)', 'Mouse V1\n(n=1567)'], fontsize=11)
ax.set_xlim(-0.6, len(GENE_ORDER) - 0.4)
ax.set_ylim(-0.55, 1.55)
ax.set_title('Acetylcholine receptor expression in SST interneurons\nMouse V1 vs. Marmoset MTG', fontsize=13, fontweight='bold')
ax.grid(axis='x', linestyle=':', alpha=0.4)

# Legend: dot size = % expressing
for pct_ex in [10, 25, 50, 75, 100]:
    ax.scatter([], [], s=(pct_ex/100)*max_size, c='grey', edgecolors='k',
               linewidths=0.5, label=f'{pct_ex}%')
size_leg = ax.legend(title='% expressing', bbox_to_anchor=(1.01, 1.0),
                     loc='upper left', frameon=True, fontsize=9, title_fontsize=9)
ax.add_artist(size_leg)

# Color bar mouse
from matplotlib.colorbar import ColorbarBase
ax_cb_m = fig.add_axes([1.17, 0.55, 0.025, 0.35])
cb_m = ColorbarBase(ax_cb_m, cmap=cm.Blues, norm=Normalize(vmin=vmin, vmax=vmax), orientation='vertical')
cb_m.set_label('Mouse\nmean expr\n(log1p CPM10k)', fontsize=8)

# Color bar marmoset
ax_cb_r = fig.add_axes([1.17, 0.12, 0.025, 0.35])
cb_r = ColorbarBase(ax_cb_r, cmap=cm.Oranges, norm=Normalize(vmin=vmin, vmax=vmax), orientation='vertical')
cb_r.set_label('Marmoset\nmean expr\n(log1p CPM10k)', fontsize=8)

# Mark missing gene
ax.text(GENE_ORDER.index('CHRM4'), YPOS['marmoset'] - 0.22,
        'not in\npanel', ha='center', va='top', fontsize=7, color='grey', style='italic')

# Separator line
ax.axhline(0.5, color='lightgrey', linewidth=0.8, linestyle='--')

plt.tight_layout(rect=[0, 0, 1.15, 1])
plt.savefig('/work/chrm_dotplot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved /work/chrm_dotplot.png")
