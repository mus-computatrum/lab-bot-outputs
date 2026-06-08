# Run `954161fb50e6` — download

**When (UTC):** 2026-06-08 20:16:54
**Datasets:** _none_

## Request

> Explore why hrvatin and green datasets are not visible to bot users via datasets command.

## Summary

## Summary
Both datasets are **correctly registered** — all files are present in `/data/green-2023-ppc-inhibitory-snatac/` and `/data/hrvatin-2019-pesca-interneuron/`, and `describe_dataset` returns full, polished cards for each. The problem is **not** missing data or a failed registration. The most likely root cause is a **stale bot registry cache**: `register_dataset` writes both a card file (read live, per-call — which is why cards work) and an entry in `registry.yaml`. Its contract makes datasets live "for all future *jobs*," but the Discord `datasets` listing appears to be served from the bot's in-memory snapshot of `registry.yaml` loaded at startup — before these two were registered (~18:50 UTC 2026‑06‑08) — so it hasn't picked them up.

## What I did
- Listed `/data`: both dataset dirs present with all expected files (green ~9 GB incl. configured `gse232200_snapatac.h5ad`; hrvatin incl. `gse136802_scrna.h5ad` + `gse136802_atac.h5ad`).
- Confirmed `describe_dataset` returns complete cards for both → card half of registration succeeded.
- Read the `register_dataset` schema: it writes a YAML entry **and** a card; "live for future jobs" ≠ the live Discord listing.
- Cross-checked prior runs (registration run 185025 reported "REGISTERED & live").
- Saved a channel note with the diagnosis + recommended fix.

## Caveats / next steps
- **Recommended fix (host-side):** reload/restart the bot's registry cache so the `datasets` command re-reads `registry.yaml`. Re-running `register_dataset` will **not** fix an in-memory cache and risks duplicate entries.
- I could not directly read host-side `registry.yaml` (outside the sandbox) to 100% confirm the YAML entry exists; the inference rests on the prior run returning OK and cards being present.
- A broad `find /` wedged the IPython kernel for the rest of this job, so I couldn't write `/work/datasets_visibility_fix.md` or stage files. With the sandbox back, I'd grep `registry.yaml` to confirm the entries, then advise the maintainer to reload the bot.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`code/_cell_0008.py`](./code/_cell_0008.py)
- [`code/_cell_0009.py`](./code/_cell_0009.py)
- [`code/_cell_0010.py`](./code/_cell_0010.py)
- [`code/_cell_0011.py`](./code/_cell_0011.py)
- [`code/_cell_0012.py`](./code/_cell_0012.py)
- [`code/_cell_0013.py`](./code/_cell_0013.py)
- [`code/_cell_0014.py`](./code/_cell_0014.py)
- [`code/_cell_0015.py`](./code/_cell_0015.py)
- [`code/_cell_0016.py`](./code/_cell_0016.py)
- [`code/_cell_0017.py`](./code/_cell_0017.py)
- [`code/_cell_0018.py`](./code/_cell_0018.py)
- [`code/_cell_0019.py`](./code/_cell_0019.py)
- [`code/_cell_0020.py`](./code/_cell_0020.py)
- [`code/_cell_0021.py`](./code/_cell_0021.py)
- [`notebook.ipynb`](./notebook.ipynb)
- [`result.md`](./result.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/fontlist-v390.json`](./tables/fontlist-v390.json)
