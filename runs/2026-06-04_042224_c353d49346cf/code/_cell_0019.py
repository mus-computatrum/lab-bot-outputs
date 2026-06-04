# Save clean CSV (drop debug columns)
df_save = df_out[['ttype', 'n_cells', 'marker1', 'marker2', 'marker3']].copy()
df_save.to_csv('/work/gouwens_sst_ttypes.csv', index=False)

# Verify
check = pd.read_csv('/work/gouwens_sst_ttypes.csv')
print("Saved shape:", check.shape)
print(check.to_string(index=False))