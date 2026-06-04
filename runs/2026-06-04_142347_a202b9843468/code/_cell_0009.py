
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Scatter plot: spatial distribution of proxy genes ─────────────────────────
# Downsample for plotting (max 8k pts per gene to keep file size reasonable)
N_SAMPLE = 8000
rng = np.random.default_rng(42)

fig, ax = plt.subplots(figsize=(9, 8))

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]
original_markers = ["Calb2", "Crh", "Nos1", "Pdyn"]
legend_patches = []

for gene, label, color, orig in zip(proxy_genes, target_genes_label, colors, original_markers):
    sub = df_proxy[df_proxy["gene"] == gene]
    idx = rng.choice(len(sub), size=min(N_SAMPLE, len(sub)), replace=False)
    pts = sub.iloc[idx]
    ax.scatter(pts["global_x"], pts["global_y"],
               c=color, alpha=0.25, s=3, linewidths=0,
               rasterized=True)
    # Mark centroid with a star
    ax.scatter(sub["global_x"].mean(), sub["global_y"].mean(),
               c=color, marker="*", s=220, edgecolors="k", linewidths=0.7, zorder=5)
    patch = mpatches.Patch(color=color,
                           label=f"{orig} → {gene}  (n={len(sub):,})")
    legend_patches.append(patch)

ax.set_xlabel("global_x (µm)", fontsize=11)
ax.set_ylabel("global_y (µm)", fontsize=11)
ax.set_title(
    "Vizgen MERFISH Slice 3 — SST Marker Spatial Distribution\n"
    "(Requested genes absent from receptor-map panel; receptor proxies shown)",
    fontsize=11, pad=10
)
ax.legend(handles=legend_patches, fontsize=9, loc="upper left",
          framealpha=0.85, title="Requested gene → Proxy used", title_fontsize=9)

# Annotation box
ax.text(0.99, 0.02,
        "★ = centroid\n"
        "Calb2/Crh/Nos1/Pdyn not in\n"
        "Vizgen receptor-map panel",
        transform=ax.transAxes, fontsize=7.5, ha="right", va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow", ec="grey", alpha=0.9))

fig.tight_layout()
fig.savefig("/work/vizgen_sst_marker_spatial.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved /work/vizgen_sst_marker_spatial.png")
