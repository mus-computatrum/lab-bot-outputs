
# ── 2. Compute summary statistics ─────────────────────────────────────────────
summary = (
    data.groupby("gene")
    .agg(
        n_transcripts=("global_x", "count"),
        mean_x       =("global_x", "mean"),
        mean_y       =("global_y", "mean"),
        std_x        =("global_x", "std"),
        std_y        =("global_y", "std"),
    )
    .loc[TARGET_GENES]   # keep requested order
    .reset_index()
)

# round to 2 dp for readability
for col in ["mean_x","mean_y","std_x","std_y"]:
    summary[col] = summary[col].round(2)

print(summary.to_string(index=False))
summary.to_csv("/work/vizgen_receptor_summary.csv", index=False)
print("\n✓ Saved /work/vizgen_receptor_summary.csv")
