
import os

csv_path = "/data/vizgen-merfish-brain-map/Slice3_Replicate1/detected_transcripts.csv"
size_gb = os.path.getsize(csv_path) / 1e9
print(f"CSV size: {size_gb:.2f} GB")

# Peek at header and a few rows
import pandas as pd
head = pd.read_csv(csv_path, nrows=3)
print("Columns:", list(head.columns))
print(head)
