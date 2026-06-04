
# Peek at cell metadata columns
cell_path = "/data/yao2023-wmb-10x/_abc_cache/metadata/WMB-10X/20241115/cell_metadata.csv"
cells_peek = pd.read_csv(cell_path, nrows=5)
print("Cell metadata columns:", cells_peek.columns.tolist())
print(cells_peek.head(3).to_string())
