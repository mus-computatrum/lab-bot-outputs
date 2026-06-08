import csv, os
os.makedirs('/work',exist_ok=True)
rows=[
# group, study, year, venue, species, region, modality, n/scale, doi, relevance
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Krienen et al. 2020","2020","Nature","marmoset, macaque, human, ferret, mouse","Multiple cortical areas (interneuron-focused)","snRNA-seq (interneuron-enriched)","~190k interneurons","10.1038/s41586-020-2781-z",
 "Interneuron-focused cross-primate atlas; directly resolves Sst GABAergic subtypes for orthology mapping. Highest-priority resource."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Bakken et al. 2021","2021","Nature","human, marmoset, mouse","Primary motor cortex (M1)","Multimodal: snRNA, snATAC, snmC, Patch-seq","~450k nuclei","10.1038/s41586-021-03465-8",
 "BICCN M1; cross-species GABAergic taxonomy AND chromatin/methyl + electrophysiology — can test molecular identity + enhancer accessibility + gap-junction/connexin expression."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Jorstad et al. 2023","2023","Science","human, chimp, gorilla, macaque, marmoset","Middle temporal gyrus (MTG)","snRNA-seq + MERFISH","~570k nuclei (5 primates)","10.1126/science.ade9516",
 "Five-primate homologous taxonomy with consensus Sst types; explicit cross-species type matching to mouse. Good for presence/absence test of a fine Sst type."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Ma et al. 2022","2022","Science","human, chimp, macaque, marmoset","Dorsolateral prefrontal cortex (DLPFC)","snRNA-seq + spatial transcriptomics","~600k nuclei","10.1126/science.abo7257",
 "Cross-primate DLPFC with species-specific cell-type analysis; includes spatial validation. Tests Sst subtype conservation in association cortex."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Hodge et al. 2019","2019","Nature","human, mouse","Middle temporal gyrus (MTG)","snRNA-seq","~16k human nuclei","10.1038/s41586-019-1506-7",
 "Foundational human cortical taxonomy with mouse homology; resolves Sst subtypes. Useful reference for marker-based matching."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Siletti et al. 2023","2023","Science","human","106 brain locations incl. many neocortical areas","snRNA-seq","~3.0M nuclei","10.1126/science.add7046",
 "Deepest human brain atlas; large Sst cell numbers across cortical areas (incl. parietal) give power to detect a rare Sst44-like type."],
["A. Cross-species snRNA-seq (interneuron resolution; best for direct Sst44 mapping)",
 "Krienen et al. 2023","2023","Sci Adv","marmoset","Whole brain, regional","snRNA-seq cell census","~2.4M nuclei","10.1126/sciadv.adk3986",
 "Marmoset brain-wide census; regional Sst diversity for a tractable NHP model."],
# Spatial
["B. Spatial transcriptomics in primate/cross-species cortex (localize a putative homolog)",
 "Chen et al. 2023","2023","Cell","macaque (Macaca fascicularis)","Whole cortex (143 areas, incl. PPC homolog)","Stereo-seq (subcellular spatial)","Whole hemisphere","10.1016/j.cell.2023.06.009",
 "Spatially resolved macaque cortex covering parietal areas; lets you ask whether a Sst44-like type localizes to the PPC/IPS homolog and shows clustered arrangement."],
["B. Spatial transcriptomics in primate/cross-species cortex (localize a putative homolog)",
 "Fang et al. 2022","2022","Science","human, mouse","Cortex","MERFISH (~4000 genes)","spatial single cell","10.1126/science.abm1741",
 "Cross-species MERFISH directly comparing cortical cell organization; good template for spatial conservation tests of GABAergic types."],
["B. Spatial transcriptomics in primate/cross-species cortex (localize a putative homolog)",
 "Qian et al. 2025","2025","Nature","human","Cortex (layer/area specification)","Spatial transcriptomics","spatial","10.1038/s41586-025-09010-1",
 "Human cortical layer/area spatial map; useful to place Sst subtypes by layer/area, including parietal."],
["B. Spatial transcriptomics in primate/cross-species cortex (localize a putative homolog)",
 "Lei et al. 2025","2025","Cell","macaque","Claustrum + connected cortex","Single-cell spatial + connectivity","spatial","10.1016/j.cell.2025.02.037",
 "Secondary: macaque spatial atlas; relevant if checking subcortical/claustral Sst, less so for PPC."],
# Multiomics / chromatin
["C. Multi-omics / chromatin (test conservation of the Sst44 enhancer / cis-regulatory element)",
 "Li et al. 2023","2023","Science","human","Multiple brain regions incl. cortex","Single-cell ATAC-seq (chromatin accessibility)","~1.1M nuclei","10.1126/science.adf7044",
 "Human brain cCRE atlas; lets you test whether the mouse Sst-subset enhancer used to label Sst44 is conserved/accessible in the homologous human Sst type."],
["C. Multi-omics / chromatin (test conservation of the Sst44 enhancer / cis-regulatory element)",
 "Bakken et al. 2021 (multiome arm)","2021","Nature","human, marmoset, mouse","M1","snATAC-seq + snmC-seq (paired with RNA)","cross-species","10.1038/s41586-021-03465-8",
 "Cross-species chromatin+methylation in homologous GABAergic types — directly supports enhancer-conservation analysis underpinning viral access in primates."],
]
cols=["group","study","year","venue","species","region","modality","scale","doi","relevance_to_Sst44"]
with open('/work/primate_Sst44_datasets.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(cols); w.writerows(rows)
print("wrote",len(rows),"rows")
print(open('/work/primate_Sst44_datasets.csv').read()[:400])
