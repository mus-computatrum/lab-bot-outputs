
# ─── FIGURE 4: Comprehensive ranked candidate table (structural GJ candidates, d<20µm, 0 syn)
# + synapse count distribution to show the null

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel A: Synapse count distribution for close pairs
ax = axes[0]
d20_connected = close_pairs_df[close_pairs_df['dist_um'] < 20]
ax.hist(d20_connected['syn_total'],
        bins=range(0, 30), color=OI['blue'], alpha=0.8, edgecolor='white', lw=0.5)
ax.axvline(0.5, color=OI['red'], ls='--', lw=2, 
           label=f"Zero-syn: {(d20_connected['syn_total']==0).mean()*100:.0f}%")
ax.set_xlabel('Total chemical synapses (both directions)')
ax.set_ylabel('Number of neuron pairs')
ax.set_title(f'A: Synapse count for pairs with\nsoma d < 20 µm (n={len(d20_connected):,} pairs)')
ax.set_yscale('log')
ax.legend(fontsize=8)

# Panel B: Soma distance distribution — all pairs vs zero-syn pairs
ax = axes[1]
all_close = close_pairs_df[close_pairs_df['dist_um'] < 100]['dist_um']
zero_close = close_pairs_df[(close_pairs_df['dist_um'] < 100) & (close_pairs_df['syn_total']==0)]['dist_um']
conn_close = close_pairs_df[(close_pairs_df['dist_um'] < 100) & (close_pairs_df['syn_total']>0)]['dist_um']

ax.hist(all_close, bins=20, color=OI['blue'], alpha=0.4, density=True, label='All pairs')
ax.hist(zero_close, bins=20, color=OI['orange'], alpha=0.6, density=True, label='0 synapses (GJ cand.)')
ax.hist(conn_close, bins=20, color=OI['green'], alpha=0.6, density=True, label='>0 synapses (ctrl)')
ax.set_xlabel('Soma–soma distance (µm)')
ax.set_ylabel('Density')
ax.set_title('B: Distance distributions\nzero-syn vs connected pairs (d<100µm)')
ax.legend(fontsize=7)

# Panel C: Top structural GJ candidates ranked table
ax = axes[2]
ax.axis('off')
top_struct = struct_gj_cands.sort_values('dist_um').head(15)

table_data_s = []
for _, r in top_struct.iterrows():
    table_data_s.append([
        f"{str(r.root_id_a)[:10]}…",
        f"{str(r.root_id_b)[:10]}…",
        f"{r.dist_um:.2f}",
        f"{int(r.syn_total)}",
        f"{int(r.syn_ab)}↑/{int(r.syn_ba)}↓"
    ])

cols_s = ['Root ID A', 'Root ID B', 'Soma d\n(µm)', 'N syn\ntotal', 'Directionality']
tbl_s = ax.table(cellText=table_data_s, colLabels=cols_s,
                 loc='center', cellLoc='center')
tbl_s.auto_set_font_size(False)
tbl_s.set_fontsize(7)
tbl_s.scale(1.2, 1.5)
for i in range(1, len(table_data_s)+1):
    for j in range(5):
        tbl_s[i, j].set_facecolor('#e8f4fd')
ax.set_title(f'C: Top structural GJ candidates\n(soma d<20µm, 0 chemical synapses, n={len(struct_gj_cands):,} total)',
             pad=10, fontsize=9)

fig.suptitle('Structural gap-junction candidates: 2316 proofread EM neurons\n'
             '(MICrONS minnie65, N=378,090 within-proofread synapses identified)',
             fontweight='bold', fontsize=10)
fig.tight_layout()
fig.savefig('/work/fig4_structural_candidates.png')
plt.close()
print("Figure 4 saved.")
