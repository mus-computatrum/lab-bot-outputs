
# Print full descriptions for all tables to assess GJ relevance
for r in rows:
    print(f"\n=== {r['table_name']} ({r['schema']}) ===")
    # Fetch full description
    try:
        meta = client.materialize.get_table_metadata(r["table_name"])
        desc = (meta.get("description") or "").strip()
        print(desc[:400] if desc else "(no description)")
    except:
        print("(metadata fetch failed)")
    time.sleep(0.05)
