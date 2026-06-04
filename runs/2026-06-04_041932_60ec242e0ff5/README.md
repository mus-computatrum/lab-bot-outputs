# Run `60ec242e0ff5` — research

**When (UTC):** 2026-06-04 04:19:32
**Datasets:** `bugeon2022-v1`

## Request

> [bench:research-bugeon-state-modulation] Using the Bugeon 2022 dataset at /data/bugeon2022-v1/, find the top 10 SST t-types (cells with neuron.ttype starting with 'Sst') whose mean neural activity differs most between running (state label 0) and stationary-desynchronized (state label 1) frames. Pool cells across all sessions. Save /work/sst_state_modulation.csv (columns: ttype, n_cells, mean_run, mean_stat, delta) sorted by abs(delta) descending, plus /work/sst_state_modulation_bar.png.

## Summary

All done. Here's the full report:

## Summary
Pooling all 113 SST cell-session records across 15 sessions (4 mice), the Bugeon 2022 V1 dataset contains exactly **9 unique SST t-types** — so all 9 are reported. The large majority are **run-activated**: `Sst-Hpse-Sema3c` tops the ranking with a +73.7 a.u. delta (running minus stationary-desynchronized), followed by `Sst-Calb2-Pdlim5` (+44.2) and `Sst-Calb2-Necab1` (+31.4). Two types buck the trend: `Sst-Tac1-Htr1d` and `Sst-Chodl` show modest *suppression* during running (delta ≈ −2.5 and −1.9 respectively).

## What I did
- Described dataset: 4 mouse folders → 15 sessions → 3 stimulus sub-types (Drifting Gratings, Natural Scenes, Blank), each with `frame.neuralActivity.npy` (frames × neurons) and `frame.states.npy`.
- Loaded all `neuron.ttype.txt` files; identified SST neurons (ttype starting with `'Sst'`).
- For each SST cell in each session, summed activity across **all** recording sub-folders (all stim conditions), then computed per-cell mean activity separately for state=0 (running) and state=1 (stat-desync). Averaged cell-level means within each t-type.
- Saved `/work/sst_state_modulation.csv` (9 rows: ttype, n_cells, mean_run, mean_stat, delta) sorted by |delta| descending.
- Saved `/work/sst_state_modulation_bar.png` — grouped bar chart with Δ annotations and cell counts.

## Caveats / next steps
- **Only 9 t-types exist** (not 10 as requested); all 9 are included.
- `Sst-Tac2-Tacstd2` (n=1) and `Sst-Chodl` (n=2) have very few cells — treat their estimates as unreliable.
- Per-cell means are averaged equally regardless of how many frames a cell contributed; sessions with few running frames will have noisier estimates.
- Pooling across all stimulus conditions (gratings, natural scenes, blank) means `mean_run` / `mean_stat` reflects mixed visual drive — if stimulus-specific modulation is of interest, separate analyses per condition are warranted.
- No significance testing (e.g., permutation test per t-type) was performed.

## Files

- [`code/_cell_0001.py`](./code/_cell_0001.py)
- [`code/_cell_0002.py`](./code/_cell_0002.py)
- [`code/_cell_0003.py`](./code/_cell_0003.py)
- [`code/_cell_0004.py`](./code/_cell_0004.py)
- [`code/_cell_0005.py`](./code/_cell_0005.py)
- [`code/_cell_0006.py`](./code/_cell_0006.py)
- [`code/_cell_0007.py`](./code/_cell_0007.py)
- [`figures/sst_state_modulation_bar.png`](./figures/sst_state_modulation_bar.png)
- [`summary.md`](./summary.md)
- [`tables/.kernel.json`](./tables/.kernel.json)
- [`tables/sst_state_modulation.csv`](./tables/sst_state_modulation.csv)
