import caveclient

client = caveclient.CAVEclient("minnie65_public")
print("Connected:", client.info.datastack_name)

# List available tables to confirm the target table
tables = client.annotation.get_tables()
target = [t for t in tables if 'functional_coreg' in t.lower()]
print("Matching tables:", target)
