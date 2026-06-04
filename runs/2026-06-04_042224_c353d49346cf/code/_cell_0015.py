import gc; gc.collect()

# Read just the header to get all column names
header_df = pd.read_csv(COUNT_CSV, nrows=0, index_col=0)
all_cols = header_df.columns.tolist()
print("Total cell columns:", len(all_cols))
print("First 3 col names:", all_cols[:3])
print("Index name:", header_df.index.name)