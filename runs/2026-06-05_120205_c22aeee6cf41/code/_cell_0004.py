
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
os.environ["MPLCONFIGDIR"] = "/work/.mpl_cache"
os.makedirs("/work/.mpl_cache", exist_ok=True)

import anndata as ad
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Patch

# Load V1 object
adata = ad.read_h5ad("/data/tasic2018-v1/v1_all_proc.h5ad")

# Count cells per cluster
counts = (
    adata.obs["cell_cluster"]
    .value_counts()
    .reset_index()
)
counts.columns = ["cell_type", "n_cells"]
counts = counts.sort_values("n_cells", ascending=False).reset_index(drop=True)
counts.to_csv("/work/celltype_counts.csv", index=False)
print(f"Saved CSV: {len(counts)} clusters, {counts['n_cells'].sum()} total cells")

# --- Bar plot top 30 ---
top30 = counts.head(30).copy()

def assign_color(ct):
    cl = ct.lower()
    if any(x in cl for x in ["l2", "l3", "l4", "l5", "l6"]):
        return "#4878CF"
    elif any(x in cl for x in ["sst", "pvalb", "lamp5", "vip", "sncg", "meis2", "chodl"]):
        return "#D65F5F"
    else:
        return "#6ACC65"

colors = [assign_color(ct) for ct in top30["cell_type"]]

fig, ax = plt.subplots(figsize=(10, 10))

bars = ax.barh(
    top30["cell_type"][::-1].values,
    top30["n_cells"][::-1].values,
    color=list(reversed(colors)),
    edgecolor="white",
    linewidth=0.5
)

for bar, n in zip(bars, top30["n_cells"][::-1].values):
    ax.text(
        bar.get_width() + 8, bar.get_y() + bar.get_height() / 2,
        str(n), va="center", ha="left", fontsize=8
    )

ax.set_xlabel("Number of cells", fontsize=12)
ax.set_title(
    "Tasic 2018 — VISp cell types (top 30 by count)\n"
    f"n={counts['n_cells'].sum():,} cells total, {len(counts)} clusters",
    fontsize=13
)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="y", labelsize=9)

legend_elements = [
    Patch(facecolor="#4878CF", label="Excitatory (IT/CT/NP/L6b)"),
    Patch(facecolor="#D65F5F", label="Inhibitory (Sst/Pvalb/Lamp5/Vip…)"),
    Patch(facecolor="#6ACC65", label="Non-neuronal (Astro/Oligo/Micro…)"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=9)

plt.tight_layout()
plt.savefig("/work/celltype_counts_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved /work/celltype_counts_bar.png")

# Quick sanity check - show top 10 and bottom 5
print("\nTop 10:")
print(counts.head(10).to_string(index=False))
print("\nBottom 5:")
print(counts.tail(5).to_string(index=False))
