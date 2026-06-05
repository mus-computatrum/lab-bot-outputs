
import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl"

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Top 30
top30 = counts.head(30).iloc[::-1]  # reverse for horizontal bar (largest at top)

fig, ax = plt.subplots(figsize=(10, 9))
bars = ax.barh(top30["cell_type"], top30["n_cells"], color="#4878cf", edgecolor="white", linewidth=0.4)

# Value labels
for bar, val in zip(bars, top30["n_cells"]):
    ax.text(val + 8, bar.get_y() + bar.get_height() / 2,
            str(val), va="center", ha="left", fontsize=8)

ax.set_xlabel("Number of cells", fontsize=11)
ax.set_title("Tasic 2018 — VISp cell types by abundance (top 30 of 118)", fontsize=12, fontweight="bold")
ax.set_xlim(0, top30["n_cells"].max() * 1.15)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
fig.savefig("/work/celltype_counts_bar.png", dpi=150)
plt.close()
print("Saved /work/celltype_counts_bar.png")
