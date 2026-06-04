
# In this taxonomy, "Sst" is at the subclass level (not class).
# Let's identify the Sst subclasses and their supertypes
sst_piv = piv[piv["subclass"].str.contains("Sst", na=False)]
print(f"Sst subclass rows: {len(sst_piv)}")
print("\nSst subclasses:", sst_piv["subclass"].unique())
print("\nParent classes for Sst subclasses:", sst_piv["class"].unique())
print("\nSupertype sample:")
print(sst_piv[["class","subclass","supertype","cluster"]].head(10).to_string())
