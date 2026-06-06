
import pandas as pd
import time, traceback

rows = []
errors = []

for table in tables:
    meta_url = meta_url_pattern.format(table=table)
    try:
        meta = client.materialize.get_table_metadata(table)
        vox = meta.get("voxel_resolution", None)
        # voxel_resolution is usually a list [x, y, z] in nm
        if isinstance(vox, list):
            vox_str = "x".join(str(v) for v in vox)
        else:
            vox_str = str(vox)
        rows.append({
            "table_name": table,
            "schema": meta.get("schema", ""),
            "description_snippet": (meta.get("description") or "")[:120].replace("\n", " "),
            "voxel_resolution_nm": vox_str,
            "table_metadata_url": meta_url,
            "http_status": 200,
        })
    except Exception as e:
        err_msg = str(e)[:200]
        # Try to extract HTTP status code
        status = "error"
        if "404" in err_msg:
            status = 404
        elif "403" in err_msg:
            status = 403
        elif "500" in err_msg:
            status = 500
        rows.append({
            "table_name": table,
            "schema": "",
            "description_snippet": f"ERROR: {err_msg}",
            "voxel_resolution_nm": "",
            "table_metadata_url": meta_url,
            "http_status": status,
        })
        errors.append((table, status, err_msg))
    time.sleep(0.1)  # be polite

print(f"Fetched {len(rows)} rows, {len(errors)} errors")
for e in errors:
    print("  ERROR:", e)
