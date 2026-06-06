
import requests, json

# Fetch the list of materialization tables
try:
    tables = client.materialize.get_tables()
    print(f"Total tables: {len(tables)}")
    print("First 20:", tables[:20])
except Exception as e:
    print("get_tables error:", type(e).__name__, str(e))
