
import os, subprocess

# Get the full list of synapse files
result = subprocess.run(['find', '/data/microns-minnie65/synapses/', '-type', 'f', '-name', '*.parquet'], 
                       capture_output=True, text=True)
files = result.stdout.strip().split('\n')
print(f"Total synapse parquet files: {len(files)}")

# Check skeleton file
import pickle
import sys
print(f"\nSkeletons file size: {os.path.getsize('/data/microns-minnie65/skeletons/bulk_skeletons.pkl')/1e6:.1f} MB")
print(f"\nProofreading file size: {os.path.getsize('/data/microns-minnie65/proofreading_status_and_strategy.parquet')/1e3:.1f} KB")
