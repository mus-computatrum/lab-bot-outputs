print("Loading neurons_soma_model.parquet ...")
soma = pd.read_parquet("/data/v1dd/extensions/neurons_soma_model.parquet")
print(f"  shape: {soma.shape}")
print(f"  cols: {soma.columns.tolist()}")
print(soma.head(3))

print("\nLoading proofreading_status_and_strategy.parquet ...")
proof = pd.read_parquet("/data/v1dd/extensions/proofreading_status_and_strategy.parquet")
print(f"  shape: {proof.shape}")
print(f"  cols: {proof.columns.tolist()}")
print(proof.head(5))
print("\nValue counts for key columns:")
if 'status_axon' in proof.columns:
    print(proof['status_axon'].value_counts())
if 'strategy_axon' in proof.columns:
    print(proof['strategy_axon'].value_counts())
