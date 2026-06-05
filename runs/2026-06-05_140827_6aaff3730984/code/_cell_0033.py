
# ─── FIGURE 3: Skeleton dendrodendritic analysis
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel A: Skeleton soma positions (3D projected) with pair connections
ax = axes[0]
# Plot soma positions for all 10 skeletons
soma_pts = np.array([skel_data[rid]['soma_nm'] / 1000.0 for rid in skel_ids])  # µm

# Color by skeleton index
cmap = plt.cm.tab10
for i, (rid, pt) in enumerate(zip(skel_ids, soma_pts)):
    ax.scatter(pt[0], pt[1], s=100, color=cmap(i), zorder=5, 
               label=f"#{i}: {rid[:6]}...", edgecolors='black', lw=0.5)

# Draw lines between pairs with dd < 5µm and 0 synapses (candidates)
for _, row in candidates_dd.iterrows():
    ia = skel_ids.index(row['root_id_a'])
    ib = skel_ids.index(row['root_id_b'])
    pa = soma_pts[ia]
    pb = soma_pts[ib]
    ax.plot([pa[0], pb[0]], [pa[1], pb[1]], 'r-', lw=1.5, alpha=0.6)

# Draw lines for bilateral pairs
for _, row in bilat.iterrows():
    ia = skel_ids.index(row['root_id_a'])
    ib = skel_ids.index(row['root_id_b'])
    pa = soma_pts[ia]
    pb = soma_pts[ib]
    ax.plot([pa[0], pb[0]], [pa[1], pb[1]], 'b-', lw=2.5, alpha=0.7)

from matplotlib.lines import Line2D
legend_handles = [
    Line2D([0],[0], color='red', lw=1.5, label='dd<5µm, 0 synapses (GJ cand.)'),
    Line2D([0],[0], color='blue', lw=2.5, label='Bilateral synapses + close dd'),
]
ax.legend(handles=legend_handles, fontsize=7, loc='upper left')
ax.set_xlabel('x (µm)')
ax.set_ylabel('y (µm)')
ax.set_title('A: Skeleton soma positions\n(10 proofread neurons, x-y projection)')

# Panel B: Dendrite-dendrite distance vs soma distance (all 45 pairs)
ax = axes[1]
# Color: 0 syn = red, >0 syn = blue
colors_dd = [OI['red'] if r.syn_total == 0 else OI['blue'] for _, r in dd_df.iterrows()]
sizes_dd  = [max(20, r.syn_total * 15 + 20) for _, r in dd_df.iterrows()]

sc = ax.scatter(dd_df['soma_dist_um'], dd_df['dendrite_dendrite_dist_um'],
                c=colors_dd, s=sizes_dd, alpha=0.8, edgecolors='black', lw=0.5)

# Add threshold lines
ax.axhline(5, color=OI['red'], ls='--', lw=1.5, label='5µm dd threshold')
ax.axvline(50, color='gray', ls=':', lw=1, label='50µm soma threshold')

# Label the key candidates
for _, row in candidates_dd[candidates_dd['dendrite_dendrite_dist_um'] < 2].iterrows():
    ax.annotate(f"dd={row['dendrite_dendrite_dist_um']:.1f}µm\n0 syn",
                (row['soma_dist_um'], row['dendrite_dendrite_dist_um']),
                fontsize=6, ha='center', va='bottom', color=OI['red'],
                xytext=(0, 8), textcoords='offset points')

# Legend patches
from matplotlib.patches import Patch
leg_elems = [
    Patch(facecolor=OI['red'], label='0 chemical synapses', alpha=0.8),
    Patch(facecolor=OI['blue'], label='>0 chemical synapses', alpha=0.8),
    Line2D([0],[0], color=OI['red'], ls='--', lw=1.5, label='5µm dd threshold'),
]
ax.legend(handles=leg_elems, fontsize=7)
ax.set_xlabel('Soma–soma distance (µm)')
ax.set_ylabel('Dendrite–dendrite min. distance (µm)')
ax.set_title('B: Dendrite proximity vs soma distance\n(10 skeleton neurons, 45 pairs)')
ax.set_ylim(-10, 300)

# Panel C: Ranked skeleton candidates table
ax = axes[2]
ax.axis('off')

# Build a ranked table with all evidence
all_sk_evidence = dd_df.sort_values('dendrite_dendrite_dist_um').copy()
all_sk_evidence['GJ score'] = (
    (1 / (all_sk_evidence['dendrite_dendrite_dist_um'] + 0.1)) * 
    np.exp(-all_sk_evidence['syn_total'])
)
top_cands = all_sk_evidence.head(12)

table_data = []
for _, r in top_cands.iterrows():
    table_data.append([
        f"{str(r.root_id_a)[:8]}…",
        f"{str(r.root_id_b)[:8]}…",
        f"{r.soma_dist_um:.0f}",
        f"{r.dendrite_dendrite_dist_um:.2f}",
        f"{int(r.syn_total)}",
        "★" if (r.syn_total == 0 and r.dendrite_dendrite_dist_um < 3) else ""
    ])

cols = ['Root A', 'Root B', 'Soma d\n(µm)', 'dd min\n(µm)', 'N syn', 'Top\ncand.']
tbl = ax.table(cellText=table_data, colLabels=cols,
               loc='center', cellLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(7)
tbl.scale(1.1, 1.4)

# Highlight zero-syn rows
for i, (_, r) in enumerate(top_cands.iterrows()):
    for j in range(6):
        cell = tbl[i+1, j]
        if r.syn_total == 0:
            cell.set_facecolor('#ffe0e0')
        if r.dendrite_dendrite_dist_um < 2 and r.syn_total == 0:
            cell.set_facecolor('#ff9999')
ax.set_title('C: Ranked skeleton candidates\n(by dendrite-dendrite distance)',
             pad=10, fontsize=10)

fig.suptitle('Structural evidence for gap-junction apposition\n'
             '(10 proofread EM neurons with skeletons)', fontweight='bold', fontsize=10)
fig.tight_layout()
fig.savefig('/work/fig3_skeleton_analysis.png')
plt.close()
print("Figure 3 saved.")
