import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl_cache"

# --- Horizontal bar plot of top 30 types ---
top30 = counts.head(30).iloc[::-1]  # reverse so highest is at top

# Color bars by cell class
class_map = (
    adata.obs[["cell_cluster", "cell_class"]]
    .drop_duplicates("cell_cluster")
    .set_index("cell_cluster")["cell_class"]
)

palette = {
    "GABAergic":    "#e06c75",
    "Glutamatergic": "#61afef",
    "Non-neuronal": "#98c379",
}
bar_colors = [palette.get(class_map.get(ct, "Non-neuronal"), "#abb2bf") for ct in top30["cell_type"]]

fig, ax = plt.subplots(figsize=(10, 9))
bars = ax.barh(top30["cell_type"], top30["n_cells"], color=bar_colors, edgecolor="white", linewidth=0.4)

# Value labels
for bar, val in zip(bars, top30["n_cells"]):
    ax.text(val + 10, bar.get_y() + bar.get_height() / 2,
            str(val), va="center", ha="left", fontsize=7.5)

ax.set_xlabel("Number of cells", fontsize=11)
ax.set_title("Top 30 cell types — Tasic 2018 VISp\n(cell_cluster, n=13,586 total, 118 types)", fontsize=12)
ax.set_xlim(0, top30["n_cells"].max() * 1.15)

# Legend
from matplotlib.patches import Patch
legend_handles = [Patch(facecolor=c, label=l) for l, c in palette.items()]
ax.legend(handles=legend_handles, loc="lower right", fontsize=9, framealpha=0.8)

ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("/work/celltype_counts_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved /work/celltype_counts_bar.png")
