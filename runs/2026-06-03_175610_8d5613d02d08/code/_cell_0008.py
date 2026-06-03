
# Marmoset X is actually raw integer counts - inspect library sizes
mar_libsizes = np.array(adata_mar.X.sum(axis=1)).flatten()
print(f"Marmoset library sizes: median={np.median(mar_libsizes):.0f}, mean={mar_libsizes.mean():.0f}, "
      f"min={mar_libsizes.min():.0f}, max={mar_libsizes.max():.0f}")
# This confirms raw counts → normalize the same way as mouse
X_mar_norm = normalize_log1p(X_mar)
print(f"Marmoset normalized: min={X_mar_norm.min():.3f}, max={X_mar_norm.max():.3f}, mean={X_mar_norm.mean():.4f}")

# Also check mouse lib sizes for reference
mouse_libsizes = np.array(sst_m.X.sum(axis=1)).flatten() if not sp.issparse(sst_m.X) else np.array(sst_m.X.sum(axis=1)).flatten()
print(f"Mouse SST library sizes: median={np.median(mouse_libsizes):.0f}, mean={mouse_libsizes.mean():.0f}")
