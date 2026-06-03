import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Top 30 cell types for bar plot
top30 = counts.head(30).copy()

# Color by cell class — join from obs
cluster_to_class = adata.obs[["cell_cluster", "cell_class"]].drop_duplicates().set_index("cell_cluster")["cell_class"]
top30["cell_class"] = top30["cell_type"].map(cluster_to_class)

palette = {
    "GABAergic":       "#e05a5a",
    "Glutamatergic":   "#4a90d9",
    "Non-neuronal":    "#6dbf67",
}
colors = top30["cell_class"].map(palette).fillna("#aaaaaa")

fig, ax = plt.subplots(figsize=(10, 11))

bars = ax.barh(
    top30["cell_type"][::-1],   # reverse so largest is at top
    top30["n_cells"][::-1],
    color=colors[::-1],
    edgecolor="white",
    linewidth=0.4,
)

ax.set_xlabel("Number of cells", fontsize=12)
ax.set_title("Tasic 2018 — V1 (VISp) cell type counts\n(top 30 of 118 clusters, n = 13,586 cells)", fontsize=13)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.tick_params(axis="y", labelsize=9)
ax.tick_params(axis="x", labelsize=10)
ax.grid(axis="x", linestyle="--", alpha=0.4, zorder=0)
ax.set_axisbelow(True)

# Legend
from matplotlib.patches import Patch
legend_handles = [Patch(color=v, label=k) for k, v in palette.items()]
ax.legend(handles=legend_handles, loc="lower right", fontsize=10, framealpha=0.85)

plt.tight_layout()
plt.savefig("/work/celltype_counts_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved /work/celltype_counts_bar.png")
