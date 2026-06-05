
import os
os.environ["MPLCONFIGDIR"] = "/work/.mpl"
os.makedirs("/work/.mpl", exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

top30 = counts.head(30).copy()

fig, ax = plt.subplots(figsize=(9, 10))
colors = ["#4C72B0" if "IT" in ct or "CT" in ct or "NP" in ct or "L" in ct[:2]
          else "#DD8452" if any(x in ct for x in ["Pvalb","Sst","Vip","Lamp5","Sncg","Meis2"])
          else "#55A868"  # non-neuronal
          for ct in top30["cell_type"]]

bars = ax.barh(top30["cell_type"][::-1], top30["n_cells"][::-1], color=colors[::-1], height=0.75)

# annotate counts
for bar, n in zip(bars, top30["n_cells"][::-1]):
    ax.text(bar.get_width() + 8, bar.get_y() + bar.get_height()/2,
            str(n), va="center", ha="left", fontsize=8)

ax.set_xlabel("Number of cells", fontsize=11)
ax.set_title("Tasic 2018 — VISp cell type counts (top 30 of 118)", fontsize=13, fontweight="bold")
ax.set_xlim(0, top30["n_cells"].max() * 1.13)
ax.tick_params(axis="y", labelsize=8.5)
ax.spines[["top","right"]].set_visible(False)

# legend patches
import matplotlib.patches as mpatches
legend_handles = [
    mpatches.Patch(color="#4C72B0", label="Excitatory / projection"),
    mpatches.Patch(color="#DD8452", label="Inhibitory interneuron"),
    mpatches.Patch(color="#55A868", label="Non-neuronal"),
]
ax.legend(handles=legend_handles, fontsize=9, loc="lower right")

plt.tight_layout()
plt.savefig("/work/celltype_counts_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved /work/celltype_counts_bar.png")
