
# ── 3. Build the top-30 horizontal bar chart ─────────────────────────────────

top30 = counts.head(30).copy()

# Okabe-Ito-inspired palette: color by broad class (excitatory, inhibitory, non-neuronal)
def assign_color(name):
    name_lower = name.lower()
    # Non-neuronal
    if any(k in name_lower for k in ["astro", "endo", "oligo", "micro", "opc", "smc", "vlmc", "peri"]):
        return "#999999"  # gray
    # Inhibitory (GABAergic)
    if any(k in name_lower for k in ["lamp5", "pvalb", "sst", "vip", "sncg", "meis2", "chodl"]):
        return "#E69F00"  # Okabe-Ito orange
    # Excitatory (Glutamatergic) — default
    return "#56B4E9"  # Okabe-Ito sky-blue

colors = [assign_color(ct) for ct in top30["cell_type"]]

# Figure height scaled by number of bars
n = len(top30)
fig_h = 0.28 * n + 0.8
fig, ax = plt.subplots(figsize=(7.5, fig_h), constrained_layout=True)

# Horizontal bars — sorted descending means largest at top
y = np.arange(n)
bars = ax.barh(y, top30["n_cells"], color=colors, height=0.72, edgecolor="none")

# Count labels at bar ends
for bar_obj, val in zip(bars, top30["n_cells"]):
    ax.text(
        bar_obj.get_width() + 10, bar_obj.get_y() + bar_obj.get_height() / 2,
        f"{val:,}", va="center", ha="left", fontsize=7.5, color="#444444"
    )

# Y-axis tick labels (cell type names)
ax.set_yticks(y)
ax.set_yticklabels(top30["cell_type"], fontsize=8.2)
ax.invert_yaxis()  # largest at top

# Axes decoration — Tufte style
ax.set_xlabel("Number of cells", fontsize=10)
ax.set_title(
    f"Tasic 2018 — VISp cell-type composition (top 30 of {len(counts)} types, n={counts['n_cells'].sum():,})",
    fontsize=10, fontweight="semibold", loc="left", pad=8
)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_color("#222222")
ax.spines["bottom"].set_linewidth(0.8)
ax.tick_params(axis="y", length=0)
ax.tick_params(axis="x", labelsize=8.5, color="#222222")

# Subtle vertical grid lines only
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.grid(axis="x", color="#dddddd", linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

# Legend for class color coding
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#56B4E9", label="Excitatory (Glutamatergic)"),
    Patch(facecolor="#E69F00", label="Inhibitory (GABAergic)"),
    Patch(facecolor="#999999", label="Non-neuronal"),
]
ax.legend(
    handles=legend_elements, fontsize=7.5, frameon=False,
    loc="lower right", bbox_to_anchor=(1.0, 0.0)
)

# Extend x-axis so count labels don't clip
ax.set_xlim(0, top30["n_cells"].max() * 1.18)

fig.savefig("/work/celltype_counts_bar.png", dpi=150, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print("Saved /work/celltype_counts_bar.png")

# Quick sanity check on CSV
check = pd.read_csv("/work/celltype_counts.csv")
print(f"CSV shape: {check.shape}, columns: {list(check.columns)}")
print(check.head(3).to_string(index=False))
