
# ── 3. Scatter plot ────────────────────────────────────────────────────────────
COLORS  = {"Sstr1": "#e41a1c", "Sstr2": "#377eb8",
           "Crhr1": "#4daf4a", "Oprk1": "#ff7f00"}
ALPHA   = 0.08
S       = 0.4          # point size — small because counts are in the tens-of-thousands
SAMPLE  = 15_000       # subsample per gene so the figure stays readable

rng = np.random.default_rng(42)

fig, ax = plt.subplots(figsize=(8, 8))

for g in TARGET_GENES:
    sub = data[data.gene == g]
    idx = rng.choice(len(sub), size=min(SAMPLE, len(sub)), replace=False)
    ax.scatter(
        sub.iloc[idx]["global_x"].values,
        sub.iloc[idx]["global_y"].values,
        c=COLORS[g], s=S, alpha=ALPHA, label=f"{g} (n={len(sub):,})", rasterized=True
    )

# Mark centroid for each gene
for _, row in summary.iterrows():
    ax.scatter(row.mean_x, row.mean_y, c=COLORS[row.gene],
               s=120, marker="*", edgecolors="black", linewidths=0.6, zorder=5)

ax.set_xlabel("global_x  (µm)", fontsize=12)
ax.set_ylabel("global_y  (µm)", fontsize=12)
ax.set_title("Vizgen MERFISH Slice 3 — Receptor Gene Spatial Distributions\n"
             "Sstr1, Sstr2, Crhr1, Oprk1  (stars = centroid)", fontsize=13)

leg = ax.legend(markerscale=14, fontsize=10, framealpha=0.85,
                loc="upper left", title="Gene (total transcripts)")
# fix alpha in legend handles
for h in leg.legend_handles:
    h.set_alpha(0.9)

ax.set_aspect("equal", adjustable="datalim")
plt.tight_layout()
fig.savefig("/work/vizgen_receptor_spatial.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Saved /work/vizgen_receptor_spatial.png")
