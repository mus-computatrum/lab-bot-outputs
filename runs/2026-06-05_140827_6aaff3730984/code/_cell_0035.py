
# ─── FIGURE 5: Phase C Integration — evidence summary figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Panel A: Effect size summary — NC elevation at short distance
ax = axes[0, 0]
dist_centers = nc_bins_df['dist_center'].values
nc_means = nc_bins_df['nc_mean'].values
nc_ci_lo = nc_bins_df['nc_ci_lo'].values
nc_ci_hi = nc_bins_df['nc_ci_hi'].values

ax.fill_between(dist_centers, nc_ci_lo, nc_ci_hi, alpha=0.25, color=OI['blue'])
ax.plot(dist_centers, nc_means, 'o-', color=OI['blue'], ms=7, lw=2, label='Noise corr. (binned mean)')

tc_means = nc_bins_df['tc_mean'].values
tc_ci_lo = nc_bins_df['tc_ci_lo'].values
tc_ci_hi = nc_bins_df['tc_ci_hi'].values
ax.fill_between(dist_centers, tc_ci_lo, tc_ci_hi, alpha=0.15, color=OI['green'])
ax.plot(dist_centers, tc_means, 's--', color=OI['green'], ms=7, lw=2, label='Total corr. (binned mean)')

ax.axhline(nc_null.mean(), color=OI['red'], ls='--', lw=1.5, label='Surrogate null mean')
ax.fill_between([0, 750],
                [np.percentile(nc_null, 2.5)]*2,
                [np.percentile(nc_null, 97.5)]*2,
                alpha=0.15, color=OI['red'], label='Surrogate 95% CI')

ax.set_xscale('log')
ax.set_xlabel('Inter-soma distance (µm, log scale)')
ax.set_ylabel('Correlation coefficient (r)')
ax.set_title('A: Functional: NC & TC vs distance\n(95% bootstrap CI, n=1,323 ROIs)')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(8, 700)

# Panel B: Structural — fraction unconnected (zero-syn) by distance bin
ax = axes[0, 1]
d_bins_centers = (struct_bins_df['dist_lo'] + struct_bins_df['dist_hi']) / 2
frac_zero = struct_bins_df['frac_zero_syn'].values * 100
frac_bil  = struct_bins_df['frac_bilateral'].values * 100

bars = ax.bar(d_bins_centers, frac_zero, width=15, color=OI['orange'], alpha=0.8, label='No chemical synapse')
ax.bar(d_bins_centers, -frac_bil, width=15, color=OI['blue'], alpha=0.8, label='Bilateral (reciprocal)')
ax.axhline(0, color='black', lw=0.5)
ax.set_xlabel('Soma–soma distance (µm)')
ax.set_ylabel('Fraction of pairs (%)')
ax.set_title('B: Structural: connectivity vs distance\n(2316 proofread neurons, N=378k synapses)')
ax.legend(fontsize=8)
ax.set_ylim(-12, 90)

# Panel C: Number of structural GJ candidates per distance threshold
ax = axes[1, 0]
d_thresholds = np.arange(5, 55, 5)
n_gj_cands = []
for dt in d_thresholds:
    n = ((close_pairs_df['dist_um'] < dt) & (close_pairs_df['syn_total'] == 0)).sum()
    n_gj_cands.append(n)
ax.plot(d_thresholds, n_gj_cands, 'o-', color=OI['orange'], ms=7, lw=2)
ax.set_xlabel('Soma distance threshold (µm)')
ax.set_ylabel('Number of 0-synapse pairs')
ax.set_title('C: Structural GJ candidates vs distance cutoff\n(soma distance, zero chemical synapses)')
ax.grid(True, alpha=0.3)
for dt, n in zip(d_thresholds, n_gj_cands):
    ax.annotate(str(n), (dt, n), textcoords='offset points', xytext=(0, 6), 
                ha='center', fontsize=7)

# Panel D: Summary statistics table
ax = axes[1, 1]
ax.axis('off')

summary_data = [
    ['Dataset', 'MICrONS minnie65 + functional (ses 4-scan-9)'],
    ['', ''],
    ['─── Phase A (Functional) ───', ''],
    ['Recording', 'GCaMP6, 6.3 Hz, 8 planes, 8,548 ROIs'],
    ['Analysis plane', 'Plane 3: 1,323 soma ROIs'],
    ['Stimulus repeats', '10× "Mad Max: Fury Road" clip (9.8 s)'],
    ['NC at d<20µm', '0.112 ± 0.178 (mean ± SD)'],
    ['NC at d>300µm', '0.005 ± 0.163'],
    ['Surrogate null', '0.001 ± 0.126'],
    ['Effect size (Cohen d)', '0.68 (short vs null, p<<0.001)'],
    ['Functional candidates', '710 pairs (d<50µm, NC>99th pct null)'],
    ['  Low-SC subset', '224 pairs (not via shared stimulus)'],
    ['', ''],
    ['─── Phase B (Structural) ───', ''],
    ['Proofread neurons', '2,316'],
    ['Within-proofread synapses', '378,090'],
    ['Pairs d<20µm, 0 synapses', '3,243 (GJ structural candidates)'],
    ['Skeletons analyzed', '10 (pre-downloaded)'],
    ['SK pairs dd<5µm, 0 syn', '11 / 45 pairs (24%)'],
    ['SK bilateral + dd<5µm', '2 / 45 pairs (4.4%)'],
    ['', ''],
    ['─── Key Caveat ───', ''],
    ['Cell types', 'UNKNOWN — no coreg table (CAVE req.)'],
    ['Functional↔EM linkage', 'IMPOSSIBLE without CAVE token'],
]

y = 0.98
for row in summary_data:
    if row[0].startswith('───'):
        ax.text(0.02, y, row[0], transform=ax.transAxes,
                fontsize=8, fontweight='bold', color=OI['blue'], va='top')
    elif row[0] == '':
        pass
    else:
        ax.text(0.02, y, row[0], transform=ax.transAxes,
                fontsize=7.5, va='top', color='black')
        ax.text(0.48, y, row[1], transform=ax.transAxes,
                fontsize=7.5, va='top', color='#333333')
    y -= 0.046
ax.set_title('D: Analysis summary statistics', fontsize=10, pad=8)

fig.suptitle('Phase C Integration: Gap-junction coupling evidence in MICrONS\n'
             '(CANDIDATE signatures only — not confirmed)', fontweight='bold', fontsize=11)
fig.tight_layout()
fig.savefig('/work/fig5_integration_summary.png')
plt.close()
print("Figure 5 saved.")
