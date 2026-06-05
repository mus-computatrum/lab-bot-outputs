
# ─── FIGURE 6: Skeleton morphology visualization for top candidates
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Pick 3 most interesting skeleton pairs (closest dd, 0 synapses)
top_sk_pairs = candidates_dd.sort_values('dendrite_dendrite_dist_um').head(3)

def plot_skeleton_pair(ax, rid_a, rid_b, label, view='xy'):
    """Plot two skeletons in 2D projection, colored by compartment."""
    da = skel_data[rid_a]
    db = skel_data[rid_b]
    
    comp_colors = {1: OI['orange'], 2: OI['sky'], 3: OI['green']}
    comp_labels = {1: 'Soma', 2: 'Axon', 3: 'Dendrite'}
    
    def get_xy(verts, view):
        v = verts / 1000.0  # nm → µm
        if view == 'xy': return v[:,0], v[:,1]
        if view == 'xz': return v[:,0], v[:,2]
        return v[:,1], v[:,2]
    
    for rid, d, marker in [(rid_a, da, 'o'), (rid_b, db, 's')]:
        for comp in [3, 2, 1]:  # dendrite first, soma last
            verts = d['vertices_nm'][np.array(d['compartment']) == comp]
            if len(verts) == 0: continue
            xx, yy = get_xy(verts, view)
            sz = 1 if comp != 1 else 80
            a = 0.3 if comp != 1 else 1.0
            ax.scatter(xx, yy, s=sz, alpha=a, color=comp_colors[comp], 
                       marker=marker, rasterized=True)
    
    # Draw soma markers
    for rid, d, label_suf in [(rid_a, da, 'A'), (rid_b, db, 'B')]:
        soma = np.array(d['soma_nm']) / 1000.0
        if view == 'xy': sx, sy = soma[0], soma[1]
        elif view == 'xz': sx, sy = soma[0], soma[2]
        else: sx, sy = soma[1], soma[2]
        ax.scatter(sx, sy, s=200, color=OI['red'], marker='*', zorder=10)
        ax.annotate(label_suf, (sx, sy), fontsize=8, ha='center', va='bottom',
                    xytext=(0, 8), textcoords='offset points', fontweight='bold')
    
    # Add compartment legend once
    if label.startswith('Pair 1'):
        from matplotlib.patches import Patch
        leg = [Patch(facecolor=comp_colors[c], label=comp_labels[c]) for c in [1,2,3]]
        ax.legend(handles=leg, fontsize=6, loc='upper right', handlelength=1)

for i, (_, row) in enumerate(top_sk_pairs.iterrows()):
    rid_a, rid_b = row.root_id_a, row.root_id_b
    soma_d = row.soma_dist_um
    dd_d = row.dendrite_dendrite_dist_um
    n_syn = int(row.syn_total)
    
    label_top = f"Pair {i+1}: dd={dd_d:.2f}µm, soma={soma_d:.0f}µm, syn={n_syn}"
    
    # XY projection (top row)
    ax_xy = axes[0, i]
    plot_skeleton_pair(ax_xy, rid_a, rid_b, f"Pair {i+1}", view='xy')
    ax_xy.set_title(f"{label_top}\n(x-y view)", fontsize=8)
    ax_xy.set_xlabel('x (µm)'); ax_xy.set_ylabel('y (µm)')
    
    # XZ projection (bottom row)
    ax_xz = axes[1, i]
    plot_skeleton_pair(ax_xz, rid_a, rid_b, "", view='xz')
    ax_xz.set_title(f"Pair {i+1} (x-z view)", fontsize=8)
    ax_xz.set_xlabel('x (µm)'); ax_xz.set_ylabel('z (µm)')

fig.suptitle('Top 3 skeleton GJ candidates: dendrite-dendrite apposition, 0 chemical synapses\n'
             '(Orange=soma, Sky=axon, Green=dendrite; Red star=soma; ○=neuron A, □=neuron B)',
             fontweight='bold', fontsize=10)
fig.tight_layout()
fig.savefig('/work/fig6_skeleton_morphology.png')
plt.close()
print("Figure 6 saved.")
