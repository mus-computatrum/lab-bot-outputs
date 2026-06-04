
# Verify the saved file
saved = pd.read_csv(out_path)
print("Saved CSV shape:", saved.shape)
print("Columns:", saved.columns.tolist())
print(saved)
