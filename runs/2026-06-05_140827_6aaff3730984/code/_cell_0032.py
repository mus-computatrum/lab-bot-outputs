
# ─── FIGURE 2: Candidate pair analysis (functional candidates vs controls)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Panel A: NC vs signal correlation for short-distance pairs
ax = axes[0]
close_mask_f = pair_dist_rois < 50
cand_mask_f  = func_cand_mask  # high NC + close distance

# All close pairs (background)
ax.scatter(pair_sc[close_mask_f & ~cand_mask_f],
           pair_nc[close_mask_f & ~cand_mask_f],
           s=2, alpha=0.2, color=OI['blue'], label='Close pairs (non-candidate)', rasterized=True)

# Functional candidates (highlighted)
ax.scatter(pair_sc[cand_mask_f],
           pair_nc[cand_mask_f],
           s=10, alpha=0.8, color=OI['orange'], label=f'Func. candidates (n={cand_mask_f.sum()})', zorder=5)

# Low-SC candidates (purple)
pure_mask_f = pure_noise_mask
ax.scatter(pair_sc[pure_mask_f],
           pair_nc[pure_mask_f],
           s=10, alpha=0.9, color=OI['purple'], label=f'Low-SC subset (n={pure_mask_f.sum()})', zorder=6)

ax.axhline(nc_null_99, color=OI['red'], ls='--', lw=1.5, label='99th pct null')
ax.set_xlabel('Signal correlation (r)')
ax.set_ylabel('Noise correlation (r)')
ax.set_title('A: NC vs SC for short-distance pairs\n(d < 50 µm)')
ax.legend(fontsize=7)

# Panel B: NC box comparison at close distance — high vs low NC candidates
ax = axes[1]
groups = {
    'Surrogate\nnull': nc_null[::10],
    'All pairs\n(d<50µm)': pair_nc[close_mask_f],
    'Func.\ncandidates': pair_nc[cand_mask_f],
    'Pure-noise\ncandidates': pair_nc[pure_mask_f],
}
colors = [OI['red'], OI['blue'], OI['orange'], OI['purple']]
positions = list(range(len(groups)))
bplot = ax.boxplot([g for g in groups.values()],
                   positions=positions, widths=0.5,
                   patch_artist=True, showfliers=False,
                   medianprops=dict(color='black', lw=2))
for patch, c in zip(bplot['boxes'], colors):
    patch.set_facecolor(c)
    patch.set_alpha(0.7)
ax.set_xticks(positions)
ax.set_xticklabels(list(groups.keys()), fontsize=8)
ax.set_ylabel('Noise correlation (r)')
ax.set_title('B: NC distributions\n(box = IQR, no outliers)')
ax.axhline(nc_null_99, color=OI['red'], ls='--', lw=1, label='99th pct null')
ax.legend(fontsize=7)

# Panel C: Structural analysis — fraction unconnected vs distance bin
ax = axes[2]
bins_s = struct_bins_df
ax.bar(range(len(bins_s)), bins_s['frac_zero_syn'] * 100,
       color=OI['blue'], alpha=0.8, label='Zero chemical synapses')
ax.bar(range(len(bins_s)),
       bins_s['frac_bilateral'] * 100,
       bottom=bins_s['frac_zero_syn'] * 100,
       color=OI['orange'], alpha=0.8, label='Bilateral synapses')
bin_labels_x = [f"{int(r.dist_lo)}–{int(r.dist_hi)}" for _, r in bins_s.iterrows()]
ax.set_xticks(range(len(bins_s)))
ax.set_xticklabels(bin_labels_x, fontsize=8, rotation=15)
ax.set_xlabel('Soma–soma distance (µm)')
ax.set_ylabel('Fraction of pairs (%)')
ax.set_title('C: Proofread pairs — connectivity\n(N=2316 EM neurons)')
ax.legend(fontsize=7)

fig.suptitle('Gap-junction candidate analysis: functional + structural evidence',
             fontsize=10, fontweight='bold')
fig.tight_layout()
fig.savefig('/work/fig2_candidate_analysis.png')
plt.close()
print("Figure 2 saved.")
