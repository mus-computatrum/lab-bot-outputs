
# Focus on cortical Sst: '053 Sst Gaba' + '056 Sst Chodl Gaba' (exclude PB Sst)
sst_tax_ctx = taxonomy[taxonomy['subclass'].isin(['053 Sst Gaba', '056 Sst Chodl Gaba'])]
sst_aliases = set(sst_tax_ctx['cluster_alias'].tolist())
print(f"Cortical Sst clusters: {len(sst_tax_ctx)}")
print(f"Supertypes: {sst_tax_ctx['supertype'].nunique()}")

# Build alias -> supertype mapping
alias_to_supertype = dict(zip(sst_tax_ctx['cluster_alias'], sst_tax_ctx['supertype']))
print("\nSample alias->supertype:", list(alias_to_supertype.items())[:3])
