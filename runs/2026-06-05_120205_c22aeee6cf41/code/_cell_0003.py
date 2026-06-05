
import os
os.environ["MPLCONFIGDIR"] = "/work/.mpl_cache"
os.makedirs("/work/.mpl_cache", exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

top30 = counts.head(30).copy()

fig, ax = plt.subplots(figsize=(10, 10))

colors = []
for ct in top30["cell_type"]:
    cl = ct.lower()
    if any(x in cl for x in ["l2", "l3", "l4", "l5", "l6"]):
        colors.append("#4878CF")   # excitatory – blue
    elif any(x in cl for x in ["sst", "pvalb", "lamp5", "vip", "sncg", "meis2", "chodl"]):
        colors.append("#D65F5F")   # inhibitory – red/coral
    else:
        colors.append("#6ACC65")   # non-neuronal – green

bars = ax.barh(
    top30["cell_type"][::-1],
    top30["n_cells"][::-1],
    color=list(reversed(colors)),
    edgecolor="white",
    linewidth=0.5
)

# Annotate bar ends
for bar, n in zip(bars, top30["n_cells"][::-1]):
    ax.text(
        bar.get_width() + 8, bar.get_y() + bar.get_height() / 2,
        str(n), va="center", ha="left", fontsize=8
    )

ax.set_xlabel("Number of cells", fontsize=12)
ax.set_title("Tasic 2018 — VISp cell types (top 30 by count)\nn=13,586 cells, 118 clusters total", fontsize=13)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="y", labelsize=9)

# Legend patches
from matplotlib.patches import Patch
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
