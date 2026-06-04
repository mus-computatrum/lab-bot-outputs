
run_coreg = '''\
#!/usr/bin/env python3
"""
microns_coreg_sample.py
-----------------------
Read the first 20 ROIs from MICrONS NWB PlaneSegmentation1,
look up their EM pt_root_id via caveclient, and save a CSV.

Requirements:
  - Complete NWB at:
      /data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb
  - Valid CAVE token in ~/.cloudvolume/secrets/cave-secret.json
  - pip install pynwb caveclient

Usage:
  python run_coreg.py [--nwb PATH] [--out PATH] [--n N]
"""
import argparse, pathlib, warnings
import numpy as np
import pandas as pd

# Suppress NWB/h5py warnings about namespace versions
warnings.filterwarnings("ignore", category=UserWarning)

NWB_DEFAULT = "/data/microns-functional/sub-17797_ses-4-scan-9_behavior+image+ophys.nwb"
OUT_DEFAULT = "/work/microns_coreg_sample.csv"
DATASTACK   = "minnie65_public"
TABLE_NAME  = "apl_functional_coreg_forward_v5"


def parse_session_scan(nwb_path: str):
    """Extract session and scan_idx from NWB filename."""
    stem = pathlib.Path(nwb_path).name
    # sub-17797_ses-4-scan-9_behavior+image+ophys.nwb
    import re
    m = re.search(r"ses-(\d+)-scan-(\d+)", stem)
    if not m:
        raise ValueError(f"Cannot parse session/scan from filename: {stem}")
    return int(m.group(1)), int(m.group(2))


def load_roi_info(nwb_path: str, n: int = 20):
    """Return DataFrame with (unit_id, field, session, scan_idx) for the first n ROIs."""
    from pynwb import NWBHDF5IO
    session, scan_idx = parse_session_scan(nwb_path)

    with NWBHDF5IO(nwb_path, "r", load_namespaces=True) as io:
        nwb = io.read()
        # Navigate to PlaneSegmentation1
        ophys = nwb.processing["ophys"]
        img_seg = ophys["ImageSegmentation"]
        ps = img_seg["PlaneSegmentation1"]

        unit_ids = ps.id[:n]
        # Field comes from the ImagingPlane description or index in ps.imaging_plane
        # The imaging_plane.description often encodes the field number
        ip = ps.imaging_plane
        # Try to get field number from imaging plane location/description
        # MICrONS convention: field is the plane index (0-based) in the volume
        # It\'s usually stored in ip.location or ip.name
        location = getattr(ip, "location", None) or ""
        desc     = getattr(ip, "description", None) or ""
        name     = getattr(ip, "name", "")
        # Try to parse field number: e.g. "field_1" or "plane_1"
        import re
        field_match = re.search(r"(?:field|plane)[_-]?(\d+)", f"{location} {desc} {name}", re.I)
        field = int(field_match.group(1)) if field_match else 1

        print(f"Session={session}, scan_idx={scan_idx}, field={field}")
        print(f"ImagingPlane name={name!r}, location={location!r}")
        print(f"First {len(unit_ids)} unit_ids: {unit_ids}")

    rows = [{"unit_id": int(u), "field": field,
             "session": session, "scan_idx": scan_idx}
            for u in unit_ids]
    return pd.DataFrame(rows)


def lookup_coreg(df_rois: pd.DataFrame) -> pd.DataFrame:
    """Query CAVE for pt_root_id and pt_position for each ROI."""
    import caveclient
    client = caveclient.CAVEclient(DATASTACK)

    results = []
    for _, row in df_rois.iterrows():
        filters = {
            "session":   int(row.session),
            "scan_idx":  int(row.scan_idx),
            "field":     int(row.field),
            "unit_id":   int(row.unit_id),
        }
        try:
            tbl = client.annotation.query_table(
                TABLE_NAME,
                filter_equal_dict=filters,
                desired_resolution=[4, 4, 40],  # nm/voxel, standard minnie65
            )
            if len(tbl) > 0:
                r = tbl.iloc[0]
                results.append({
                    "unit_id":      int(row.unit_id),
                    "pt_root_id":   int(r["pt_root_id"]),
                    "pt_position_x": float(r["pt_position_x"]),
                    "pt_position_y": float(r["pt_position_y"]),
                    "pt_position_z": float(r["pt_position_z"]),
                })
            else:
                results.append({
                    "unit_id":      int(row.unit_id),
                    "pt_root_id":   None,
                    "pt_position_x": None,
                    "pt_position_y": None,
                    "pt_position_z": None,
                })
        except Exception as e:
            print(f"  Warning: lookup failed for unit_id={row.unit_id}: {e}")
            results.append({
                "unit_id":      int(row.unit_id),
                "pt_root_id":   None,
                "pt_position_x": None,
                "pt_position_y": None,
                "pt_position_z": None,
            })
    return pd.DataFrame(results)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nwb", default=NWB_DEFAULT)
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--n",   type=int, default=20)
    args = ap.parse_args()

    print(f"Loading ROIs from {args.nwb}")
    df_rois = load_roi_info(args.nwb, args.n)
    print(df_rois)

    print(f"\\nQuerying CAVE table {TABLE_NAME} on {DATASTACK}...")
    df_result = lookup_coreg(df_rois)

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df_result.to_csv(out, index=False)
    print(f"\\nSaved {len(df_result)} rows to {out}")
    print(df_result.to_string())


if __name__ == "__main__":
    main()
'''

with open("/work/run_coreg.py", "w") as f:
    f.write(run_coreg)
print("Wrote /work/run_coreg.py")
