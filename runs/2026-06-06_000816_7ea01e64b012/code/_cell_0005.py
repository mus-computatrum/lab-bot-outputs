
import time

# Build the base metadata URL pattern
mat_ver = client.materialize.version
server = client.server_address
datastack = client.datastack_name

# Standard CAVE materialization metadata endpoint pattern:
# GET /materialize/api/v3/datastack/{datastack}/table/{table}/metadata
# Let's first confirm by trying one table
test_table = tables[0]
meta_url_pattern = f"{server}/materialize/api/v3/datastack/{datastack}/table/{{table}}/metadata"
print("URL pattern:", meta_url_pattern.format(table=test_table))

# Also try client.materialize.get_table_metadata
try:
    meta = client.materialize.get_table_metadata(test_table)
    print("Metadata keys:", list(meta.keys()))
    print("Sample metadata:", json.dumps(meta, indent=2)[:600])
except Exception as e:
    print("get_table_metadata error:", type(e).__name__, str(e)[:200])
