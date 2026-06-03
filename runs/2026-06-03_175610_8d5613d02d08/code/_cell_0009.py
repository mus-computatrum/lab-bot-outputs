
# Recompute marmoset summary with proper normalization
summary_mar = make_summary(X_mar_norm, mar_found_syms, 'marmoset')
summary_mar['gene_upper'] = summary_mar['gene'].str.upper()

print("Marmoset summary (corrected, normalized):")
print(summary_mar[['gene','mean_expr','pct_expr','n_cells']].to_string(index=False))

# Note: library sizes differ substantially (mouse ~200 vs marmoset ~7600)
# Normalization to 10k CPM equalizes depth. But tech platform differs too
# (mouse: SMART-seq2 full-length; marmoset: likely 10x or similar)
print(f"\nNote: Mouse median lib size = {np.median(mouse_libsizes):.0f} (SMART-seq2 full-length)")
print(f"Marmoset median lib size = {np.median(mar_libsizes):.0f} (likely 10x-based - check)")
