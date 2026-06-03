
# ── 5. Compute mean expression and fraction expressing ────────────────────────
# Mouse: raw counts → normalize to 10k CPM → log1p (to match marmoset normalization)
import scipy.sparse as sp

def normalize_log1p(mat):
    """Normalize to 10k CPM then log1p. Works on dense or sparse."""
    if sp.issparse(mat):
        mat = mat.toarray()
    mat = mat.astype(np.float64)
    lib = mat.sum(axis=1, keepdims=True)
    lib[lib == 0] = 1
    normed = mat / lib * 1e4
    return np.log1p(normed)

X_mouse_norm = normalize_log1p(sst_m.X)
print(f"Mouse norm matrix: {X_mouse_norm.shape}, max={X_mouse_norm.max():.2f}")

# Marmoset: already log1p normalized
X_mar = sst_mar.X
if sp.issparse(X_mar):
    X_mar = X_mar.toarray()
X_mar = X_mar.astype(np.float64)
print(f"Marmoset matrix: {X_mar.shape}, max={X_mar.max():.2f}")

# Build summary DataFrames
def make_summary(X, genes, species):
    df = pd.DataFrame({
        'gene': genes,
        'species': species,
        'mean_expr': X.mean(axis=0),
        'pct_expr': (X > 0).mean(axis=0) * 100,
        'n_cells': X.shape[0]
    })
    return df

summary_mouse = make_summary(X_mouse_norm, mouse_found, 'mouse')
summary_mar   = make_summary(X_mar, mar_found_syms, 'marmoset')

# Unify gene names (uppercase for join)
summary_mouse['gene_upper'] = summary_mouse['gene'].str.upper()
summary_mar['gene_upper']   = summary_mar['gene'].str.upper()

print("\nMouse summary:")
print(summary_mouse[['gene','mean_expr','pct_expr','n_cells']].to_string(index=False))
print("\nMarmoset summary:")
print(summary_mar[['gene','mean_expr','pct_expr','n_cells']].to_string(index=False))
