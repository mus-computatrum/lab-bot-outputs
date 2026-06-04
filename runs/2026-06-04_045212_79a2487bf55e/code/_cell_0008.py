# Quick validation
import os
csv_size = os.path.getsize('/work/v1dd_top_axon_proofread.csv')
png_size = os.path.getsize('/work/v1dd_top_synapse_counts.png')
print(f"CSV: {csv_size} bytes")
print(f"PNG: {png_size/1024:.1f} KB")

# Show final table
import pandas as pd
final = pd.read_csv('/work/v1dd_top_axon_proofread.csv')
print("\nFinal CSV contents:")
print(final.to_string(index=False))
print(f"\nRows: {len(final)}  Columns: {list(final.columns)}")
print(f"\nSynapse count range: {final.n_outgoing_syn.min():,} – {final.n_outgoing_syn.max():,}")
