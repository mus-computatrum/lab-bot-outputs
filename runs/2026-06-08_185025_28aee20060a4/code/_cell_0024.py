import shutil, os, datetime
today=datetime.date.today().isoformat()
g232=f'/work/staged/green-2023-ppc-inhibitory-snatac'
g136=f'/work/staged/hrvatin-2019-pesca-interneuron'

# move configured h5ads into staged dirs
shutil.move('/work/gse232200_snapatac.h5ad', f'{g232}/gse232200_snapatac.h5ad')
shutil.move('/work/gse136802_scrna.h5ad', f'{g136}/gse136802_scrna.h5ad')
shutil.move('/work/gse136802_atac.h5ad', f'{g136}/gse136802_atac.h5ad')

cfg232=f"""# GSE232200 — provenance & schema

**Source:** NCBI GEO GSE232200 (Green et al. 2023, Nature, doi:10.1038/s41586-023-06357-1, PMID 37468637).
10x snATAC-seq of Gad2-Cre;Sun1-GFP cortical (PPC) inhibitory neurons. Downloaded {today} from
ftp.ncbi.nlm.nih.gov/geo/samples/GSM7317nnn/.

**Raw files committed:** GSM7317753_biorep1.snap.gz, GSM7317754_biorep2.snap.gz (SnapATAC v1, genome mm10),
plus per-biorep CellRanger-ATAC singlecell.csv.gz.

**Configured artifact:** gse232200_snapatac.h5ad — merged peak x cell matrix.
- shape: 22,988 cells x 459,912 peaks; X = peak fragment counts (float32, uint8 origin).
- obs: BD QC fields from .snap (TN,UM,PP,UQ,SE,SA,PE,PL,US,CM), barcode, biorep (biorep1=GSM7317753,
  biorep2=GSM7317754), plus joined CellRanger QC (passed_filters, peak_region_fragments, TSS_fragments,
  promoter/enhancer_region_fragments, is__cell_barcode, cell_id).
- var: chr/start/end (mm10); index = "chr:start-end".
- Median UQ ~12-13k fragments/cell; 22,876/22,988 flagged is__cell_barcode==1.

**Gotchas:**
- Built from the .snap `PM` (peak) group: idx=cell (1-based -> BD order), idy=peak (1-based -> peakChrom order).
- 63 orphan peak indices (idy 459913-459975) had NO stored coordinates; their entries (~0.008% of nnz)
  were dropped. Peak coordinate array is genomically sorted (chr1..chrY), so index<->coord is a valid prefix.
- Also available in .snap but NOT extracted: AM/5000 (5kb bin x cell matrix), FM (raw fragments), BD full QC.
"""
open(f'{g232}/gse232200_config.md','w').write(cfg232)

cfg136=f"""# GSE136802 — provenance & schema

**Source:** NCBI GEO GSE136802 (Hrvatin et al. 2019, eLife, doi:10.7554/eLife.48089). PESCA enhancer-AAV
platform: ATAC + scRNA of cortical Sst/Vip/Pv INTACT interneurons. Downloaded {today} from
ftp.ncbi.nlm.nih.gov/geo/series/GSE136nnn/GSE136802/.

**Raw files committed:** GSE136802_RAW.tar (10 scRNA counts.tsv.gz + 6 per-sample ATAC peak .bed.gz),
GSE136802_atac_master_counts.csv.gz, GSE136802_atac_master_binary_peak_table.csv.gz,
GSE136802_S2_annotated_gres.csv.gz.

**Configured artifact 1: gse136802_scrna.h5ad** (INTACT cortical interneuron scRNA-seq)
- shape: 47,348 cells x 27,035 genes. Concatenated from 10 lanes (GSM4058339_180320_6-19-*).
- X = raw counts; layers['counts']=raw; layers['lognorm']=log1p(CP10k).
- obs: lane, gsm, assay. Cell barcodes prefixed "<lane>|<barcode>".
- NOTE: cell-type (Sst/Vip/Pv) is assigned downstream by clustering — not provided as deposited metadata.

**Configured artifact 2: gse136802_atac.h5ad** (pseudobulk ATAC master peak matrix)
- shape: 6 samples x 323,369 peaks. obs = CTX_{{PV,VIP,SST}}_{{1,2}} (celltype, replicate, region).
- X = master_counts (fragment counts); layers['binary'] = binary peak-call table (same 6 samples).
- var: chr/start/end + conservation (MeanCons/MinCons/MaxCons) for all peaks; GRE annotation columns
  (Annotation, Gene_Name, Name, ATAC_Specificity, PESCA_Specificity) for the 287 annotated GREs
  (is_annotated_GRE flag). Peak index = "master_N".

**Gotchas:**
- ATAC data is pseudobulk (6 sorted samples), NOT single-cell.
- binary_peak_table has 12 cols (Chr/Start/End + 6 samples + 3 conservation); only the 6 sample cols form layers['binary'].
"""
open(f'{g136}/gse136802_config.md','w').write(cfg136)

# remove large decompressed .snap (keep .snap.gz as canonical raw)
for p in ['/work/GSM7317753_biorep1.snap','/work/GSM7317754_biorep2.snap']:
    os.remove(p)

print("== staged green ==")
for f in sorted(os.listdir(g232)): print(f"  {os.path.getsize(g232+'/'+f)/1e6:9.1f} MB  {f}")
print("== staged hrvatin ==")
for f in sorted(os.listdir(g136)): print(f"  {os.path.getsize(g136+'/'+f)/1e6:9.1f} MB  {f}")
