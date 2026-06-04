# ── Make histogram ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))

valid_osi = full_df.osi.dropna()

# Main histogram (bin from -0.1 to 1.2 to capture out-of-range values)
bins = np.arange(-0.1, 1.21, 0.1)
counts, edges, patches = ax.hist(valid_osi, bins=bins, color='#4C72B0', edgecolor='white',
                                  linewidth=0.6, zorder=3)

# Shade out-of-range region (>1 means negative orthogonal suppression)
for patch, left in zip(patches, edges[:-1]):
    if left >= 1.0:
        patch.set_facecolor('#E07070')
        patch.set_label('Rorth < 0 (suppressed)' if left == edges[edges >= 1.0][0] else '')

# Annotations
n_valid = valid_osi.notna().sum()
n_nan   = full_df.osi.isna().sum()
n_gt1   = (valid_osi > 1).sum()
med_osi = valid_osi.median()
mean_osi = valid_osi.mean()

ax.axvline(med_osi, color='tomato', lw=1.8, ls='--', zorder=5, label=f'Median = {med_osi:.2f}')
ax.axvline(mean_osi, color='orange', lw=1.5, ls=':', zorder=5, label=f'Mean = {mean_osi:.2f}')
ax.axvline(1.0, color='#E07070', lw=1.2, ls='-', alpha=0.6, zorder=4)

ax.set_xlabel('Orientation Selectivity Index (OSI)', fontsize=12)
ax.set_ylabel('Number of cells', fontsize=12)
ax.set_title('Drifting Grating OSI — Sst-IRES-Cre cells in VISp\n'
             '(Allen Brain Observatory Visual Coding 2P, 11 experiments)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(axis='y', alpha=0.3)
ax.set_xlim(-0.15, 1.25)

# Annotation box
textstr = (f'N cells = {n_valid}  ({n_nan} NaN)\n'
           f'N experiments = {full_df.ophys_experiment_id.nunique()}\n'
           f'OSI > 1 (Rorth < 0): {n_gt1} cells')
ax.text(0.03, 0.97, textstr, transform=ax.transAxes, fontsize=8.5,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/work/abo_v1_sst_osi_hist.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved /work/abo_v1_sst_osi_hist.png")
