
# Zero matches — let's check gene names in the dataset
unique_genes = pc.unique(table["gene"]).to_pylist()
print(f"Total unique genes: {len(unique_genes)}")
print("First 30 genes:", sorted(unique_genes)[:30])

# Search for our targets case-insensitively
targets_lower = [g.lower() for g in GENES]
matches = [g for g in unique_genes if g.lower() in targets_lower]
print("\nFuzzy matches for Calb2/Crh/Nos1/Pdyn:", matches)

# Also search with contains
for t in GENES:
    hits = [g for g in unique_genes if t.lower() in g.lower()]
    print(f"  Contains '{t}': {hits}")
