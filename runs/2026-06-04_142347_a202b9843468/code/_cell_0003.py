
import pyarrow.csv as pa_csv
import pyarrow.compute as pc
import pyarrow as pa
import pandas as pd
import numpy as np

GENES = ["Calb2", "Crh", "Nos1", "Pdyn"]
csv_path = "/data/vizgen-merfish-brain-map/Slice3_Replicate1/detected_transcripts.csv"

# Read only the 3 columns we need; pyarrow CSV is much faster than pandas for large files
print("Reading CSV with pyarrow (3 columns only)…")
read_opts = pa_csv.ReadOptions()
convert_opts = pa_csv.ConvertOptions(
    include_columns=["global_x", "global_y", "gene"]
)

table = pa_csv.read_csv(csv_path, convert_options=convert_opts)
print(f"Total rows: {len(table):,}")
print(f"Memory usage: {table.nbytes / 1e6:.1f} MB")

# Filter to our 4 genes
mask = pc.is_in(table["gene"], value_set=pa.array(GENES))
filtered = table.filter(mask)
print(f"Rows for target genes: {len(filtered):,}")
df = filtered.to_pandas()
print(df["gene"].value_counts())
