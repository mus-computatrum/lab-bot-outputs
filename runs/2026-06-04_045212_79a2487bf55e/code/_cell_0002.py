import pandas as pd

# Load all three parquet files
print("Loading synapses_from_axon_proofread.parquet ...")
syn = pd.read_parquet("/data/v1dd/extensions/synapses_from_axon_proofread.parquet")
print(f"  shape: {syn.shape}")
print(f"  cols: {syn.columns.tolist()}")
print(syn.head(3))
