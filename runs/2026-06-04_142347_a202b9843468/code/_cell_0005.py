
# None of the 4 genes are present. This is a RECEPTOR MAP panel — let's understand what's in it.
print(f"Total unique genes (incl. Blank): {len(unique_genes)}")

real_genes = sorted([g for g in unique_genes if not g.startswith("Blank")])
blank_genes = [g for g in unique_genes if g.startswith("Blank")]
print(f"Real (non-Blank) genes: {len(real_genes)}")
print(f"Blank codes: {len(blank_genes)}")
print("\nAll real genes (sorted):")
for g in real_genes:
    print(f"  {g}")
