more = {
 'Jorstad human-specific':'Jorstad comparative transcriptomics human-specific cortical features',
 'Jorstad cytoarchitecture MTG':'Jorstad transcriptomic cytoarchitecture human neocortical organization',
 'Chen macaque cortex stereoseq':'macaque cortex Stereo-seq single cell spatial cortical layers',
 'Macaque snRNA cortex Suresh':'macaque prefrontal cortex single nucleus transcriptomic interneuron',
 'human MERFISH whole brain BICAN':'human brain MERFISH spatial atlas cell types',
}
for k,q in more.items():
    res=pubmed_search(q,retmax=6)
    print('###',k,'->',res['esearchresult']['idlist'])
    time.sleep(0.34)
