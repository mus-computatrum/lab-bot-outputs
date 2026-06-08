import csv
rows = [
 {"paper":"Green, Bruno, Traunmüller, ... Hrvatin, Harvey (2023) Nature",
  "title":"A cell-type-specific error-correction signal in the posterior parietal cortex",
  "doi":"10.1038/s41586-023-06357-1","pmid":"37468637",
  "accession":"GEO GSE232200",
  "data_type":"10x single-cell ATAC-seq (snATAC), Gad2-Cre;Sun1-GFP cortical inhibitory neurons, 2 bioreps (GSM7317753/4)",
  "files":"GSE232200_RAW.tar; per-sample .snap.gz + singlecell.csv.gz",
  "status":"PUBLIC (since 11 May 2023)",
  "notes":"Only the snATAC-seq is deposited. Code 'available on request'; calcium imaging / electrophysiology 'available on request' (NOT in a public repo)."},
 {"paper":"Hrvatin, Tzeng, Nagy, ... Green, Harvey, Griffith, Greenberg (2019) eLife",
  "title":"A scalable platform (PESCA) for the development of cell-type-specific viral drivers",
  "doi":"10.7554/eLife.48089","pmid":"31524597",
  "accession":"GEO GSE136802 (BioProject PRJNA563701, SRA SRP220190)",
  "data_type":"PESCA: bulk/single-cell ATAC-seq + scRNA-seq of Sst/Vip/Pv INTACT-sorted cortical interneurons (7 GSM samples)",
  "files":"GSE136802_RAW.tar; processed: annotated_gres.csv, atac_master_binary_peak_table.csv, atac_master_counts.csv",
  "status":"PUBLIC",
  "notes":"Fully public incl. processed peak/count tables. Underpins the enhancer-AAV used in the 2023 paper."},
]
fn="/work/green_hrvatin_datasets.csv"
with open(fn,"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("saved",fn)
for r in rows:
    print(r["paper"],"->",r["accession"],"|",r["status"])