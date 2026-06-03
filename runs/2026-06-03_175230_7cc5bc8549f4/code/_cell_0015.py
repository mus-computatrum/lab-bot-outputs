
import json, os
from datetime import datetime

os.makedirs("/work", exist_ok=True)

# Build full cell-type label integrity check
ct_counts = adata.obs['cell_type'].value_counts().to_dict()
subclass_counts = adata.obs['Subclass'].value_counts().to_dict()
cluster_counts = adata.obs['Cluster'].value_counts().to_dict()

qc = {
    "dataset_id": "marmoset-cortical-atlas",
    "source_file": "marmoset_MTG_Jorstad2023.h5ad",
    "paper_doi": "10.1126/science.ade9516",
    "paper_citation": "Jorstad NL, Song JHT, Exposito-Alonso D, Suresh H, Castro-Pacheco N, Krienen FM, et al. Comparative transcriptomics reveals human-specific cortical features. Science 382, 1318-1323 (2023).",
    "license": "CC BY 4.0 (CellxGene curation standard)",
    "sha256": "8646351428616ac95df965cd1b0075faa637841c8297b40ea0a21bb265290bd3",
    "file_size_bytes": 485918824,
    "cellxgene_collection_id": "4dca242c-d302-4dba-a68f-4c61e7bad553",
    "cellxgene_dataset_id": "b7a0cd4e-77c2-4ae6-9eb7-8945e27e93b8",
    "download_timestamp": datetime.utcnow().isoformat(),
    "sanity_check": {
        "n_cells": int(adata.n_obs),
        "n_genes": int(adata.n_vars),
        "matrix_dtype": str(adata.X.dtype),
        "matrix_shape": list(adata.X.shape),
        "organism": adata.uns.get("organism", ""),
        "tissue": adata.obs['tissue'].unique().tolist(),
        "n_donors": int(adata.obs['donor_id'].nunique()),
        "n_cell_types": int(adata.obs['cell_type'].nunique()),
        "n_subclasses": int(adata.obs['Subclass'].nunique()),
        "n_clusters": int(adata.obs['Cluster'].nunique()),
        "n_cross_species_clusters": int(adata.obs['CrossSpeciesCluster'].nunique()),
        "mean_genes_per_cell": round(float(adata.obs['nFeature_RNA'].mean()), 1),
        "gene_id_type": "gene_symbol",
        "example_genes_first10": adata.var['feature_name'][:10].tolist(),
        "has_umap": "X_umap" in adata.obsm,
        "obs_columns": list(adata.obs.columns),
    },
    "top10_cell_types": dict(list(sorted(ct_counts.items(), key=lambda x: -x[1]))[:10]),
    "all_subclasses": dict(sorted(subclass_counts.items(), key=lambda x: -x[1])),
    "first10_clusters": dict(list(sorted(cluster_counts.items()))[:10]),
}

with open("/work/marmoset_cortical_atlas_qc.json", "w") as f:
    json.dump(qc, f, indent=2)

print("QC written to /work/marmoset_cortical_atlas_qc.json")
print(json.dumps(qc["sanity_check"], indent=2))
print("\nTop 10 cell types:")
for k, v in qc["top10_cell_types"].items():
    print(f"  {k}: {v:,}")
print("\nAll subclasses:")
for k, v in qc["all_subclasses"].items():
    print(f"  {k}: {v:,}")
