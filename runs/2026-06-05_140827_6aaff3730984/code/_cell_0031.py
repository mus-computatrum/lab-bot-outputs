
# ─── FIGURE 1: Noise Correlation vs Distance (functional analysis)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Panel A: NC vs distance scatter (thinned) + binned mean ± CI
ax = axes[0]
# Thin scatter (sample to avoid overplotting)
rng = np.random.default_rng(0)
samp_idx = rng.choice(len(pair_dist_rois), size=30000, replace=False)
ax.scatter(pair_dist_rois[samp_idx], pair_nc[samp_idx],
           s=0.5, alpha=0.08, color=OI['blue'], rasterized=True)

# Binned means with CI
for _, row in nc_bins_df.iterrows():
    dc = row['dist_center']
    ax.errorbar(dc, row['nc_mean'],
                yerr=[[row['nc_mean'] - row['nc_ci_lo']],
                      [row['nc_ci_hi'] - row['nc_mean']]],
                fmt='o', color=OI['orange'], ms=6, lw=2, capsize=3)

# Surrogate mean ± 95th pct
ax.axhline(nc_null.mean(), color=OI['red'], ls='--', lw=1.5, label='Surrogate mean')
ax.axhline(np.percentile(nc_null, 95), color=OI['red'], ls=':', lw=1, label='Surrogate 95th pct')
ax.axhline(np.percentile(nc_null, 99), color=OI['red'], ls='-.', lw=1, label='Surrogate 99th pct')
ax.set_xlabel('Inter-soma distance (µm)')
ax.set_ylabel('Noise correlation (r)')
ax.set_title('A: Noise correlation vs distance\n(Plane 3, n=1,323 ROIs)')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(0, 600)
ax.set_ylim(-0.25, 0.45)

# Panel B: Total correlation vs distance (binned mean)
ax = axes[1]
ax.scatter(pair_dist_rois[samp_idx], pair_tc[samp_idx],
           s=0.5, alpha=0.08, color=OI['green'], rasterized=True)

for _, row in nc_bins_df.iterrows():
    dc = row['dist_center']
    ax.errorbar(dc, row['tc_mean'],
                yerr=[[row['tc_mean'] - row['tc_ci_lo']],
                      [row['tc_ci_hi'] - row['tc_mean']]],
                fmt='s', color=OI['black'], ms=6, lw=2, capsize=3)

ax.set_xlabel('Inter-soma distance (µm)')
ax.set_ylabel('Total fluorescence correlation (r)')
ax.set_title('B: Total correlation vs distance\n(full session, detrended)')
ax.set_xlim(0, 600)
ax.set_ylim(-0.3, 0.6)

# Panel C: NC distribution — observed short-range vs long-range vs surrogate
ax = axes[2]
short_nc_vals = pair_nc[pair_dist_rois < 50]
long_nc_vals  = pair_nc[pair_dist_rois >= 300]

bins = np.linspace(-0.7, 0.9, 80)
ax.hist(nc_null[::5], bins=bins, alpha=0.5, color=OI['red'],
        density=True, label=f'Surrogate null\n(n={len(nc_null[::5]):,})', lw=0)
ax.hist(long_nc_vals[::10], bins=bins, alpha=0.5, color=OI['blue'],
        density=True, label=f'Long-range (d≥300µm)\n(n={len(long_nc_vals[::10]):,})', lw=0)
ax.hist(short_nc_vals, bins=bins, alpha=0.6, color=OI['orange'],
        density=True, label=f'Short-range (d<50µm)\n(n={len(short_nc_vals):,})', lw=0)

ax.axvline(np.percentile(nc_null, 99), color=OI['red'], ls='-.', lw=1.5, label='99th pct null')
ax.set_xlabel('Noise correlation (r)')
ax.set_ylabel('Density')
ax.set_title('C: NC distribution by pair type')
ax.legend(fontsize=7)

fig.suptitle('MICrONS functional: pairwise noise correlations\n'
             '(session 4-scan-9; 10 repeats of "Mad Max" clip; GCaMP6, 6.3 Hz)',
             fontsize=10, fontweight='bold')
fig.tight_layout()
fig.savefig('/work/fig1_noise_correlation_vs_distance.png')
plt.close()
print("Figure 1 saved.")
