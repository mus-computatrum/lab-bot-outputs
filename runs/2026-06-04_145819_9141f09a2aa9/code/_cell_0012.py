
# The Sst subclasses are: '053 Sst Gaba', '056 Sst Chodl Gaba', '265 PB Sst Gly-Gaba'
# For Isocortex SST cells (CTX-MGE class), we want subclass '053 Sst Gaba' and '056 Sst Chodl Gaba'
# Let's look at the supertypes within Sst subclasses
print("Sst GABA supertypes:")
print(sst_subclass.groupby(['class','subclass'])['supertype'].apply(lambda x: x.unique().tolist()))
