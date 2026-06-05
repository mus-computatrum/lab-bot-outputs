
import pandas as pd
import pickle
import numpy as np

# Load proofreading status
pr = pd.read_parquet('/data/microns-minnie65/proofreading_status_and_strategy.parquet')
print("Proofreading table shape:", pr.shape)
print("Columns:", pr.columns.tolist())
print("\nFirst few rows:")
print(pr.head(3).to_string())
print("\nValue counts for key columns:")
for col in ['strategy_axon', 'strategy_dendrite', 'status_axon', 'status_dendrite']:
    if col in pr.columns:
        print(f"\n{col}:\n{pr[col].value_counts().head(5)}")
