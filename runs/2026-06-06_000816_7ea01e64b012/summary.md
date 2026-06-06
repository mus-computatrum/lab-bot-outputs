# research-internet-cave-table-list

**Mode**: research  ·  **Effort**: standard

## Request

> From inside the sandbox, use caveclient.CAVEclient('minnie65_public') to fetch the live list of available materialize tables. Save the list at /work/cave_tables.csv with columns table_name, voxel_resolution_nm, and table_metadata_url (the URL each table's metadata endpoint resolves to). The CAVE token is at /home/sandbox/.cloudvolume/secrets/ — caveclient picks it up automatically. Also save /work/cave_summary.md with (a) the number of tables, (b) the 5 tables you'd most want for a gap-junction analysis and why, (c) any 404s you encountered and what they imply.

## Final summary

## Summary
The CAVE endpoint at `global.daf-apis.com` is fully reachable from the sandbox and the token in `/home/sandbox/.cloudvolume/secrets/` authenticated cleanly. All **45 materialization tables** were fetched with HTTP 200 — no 404s whatsoever. Both output files are saved and validated.

## What I did
- Confirmed token presence at `/home/sandbox/.cloudvolume/secrets/global.daf-apis.com-cave-secret.json`
- Connected with `caveclient v8.1.0` to `minnie65_public` and retrieved the full 45-table catalogue
- Fetched `get_table_metadata()` for every table to extract `voxel_resolution` and construct the canonical metadata URL
- **`/work/cave_tables.csv`** — 45 rows × 3 cols: `table_name`, `voxel_resolution_nm`, `table_metadata_url`
- **`/work/cave_summary.md`** — full write-up with all three requested sections (a–c)

## Caveats / next steps
- **No gap-junction–specific table exists** in minnie65_public. The top-5 picks for GJ work are: `synapses_pni_2` (connectivity backbone), `aibs_metamodel_celltypes_v661` (cell-type labels), `proofreading_status_and_strategy` (merge-error QC), `gamlin_2023_mcs`+`gamlin_2023_mcs_met_types` (SST/MC MET-types), and `nucleus_detection_v0` (soma positions for spatial filtering). A GJ analysis would need to filter `synapses_pni_2` for very small soma/shaft contacts between same-type interneurons and confirm in raw EM — there is no automated GJ detection table yet.
- Voxel resolutions: 40 tables at 4×4×40 nm (native), 4 at 1×1×1 nm, 1 at 8×8×40 nm — coordinates across tables are **not directly interchangeable**; transform to nm before joining.
- The table list reflects the live materialisation version; retired tables will disappear and new ones may appear without notice.
