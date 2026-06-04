# Inspect AIT2.3.1 alias values and figure out SST filtering
print("Sample AIT alias values:")
print(meta['corresponding_AIT2.3.1_alias'].value_counts().head(30))
print("\nUnique subclasses (prefix before first space):")
meta['subclass'] = meta['corresponding_AIT2.3.1_alias'].str.split(' ').str[0]
print(meta['subclass'].value_counts())