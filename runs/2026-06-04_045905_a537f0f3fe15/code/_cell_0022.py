# NaN = nan denominator (Rpref + Rorth = 0 or both nan; likely all-zero responses).
# OSI > 1 = negative Rorth (orthogonal orientation produces below-baseline response).
# Both are valid real-data cases. Save raw values as-is; note in histogram.

# Save CSV
full_df.to_csv('/work/abo_v1_sst_osi.csv', index=False)
print("Saved /work/abo_v1_sst_osi.csv")
print(full_df.head())
