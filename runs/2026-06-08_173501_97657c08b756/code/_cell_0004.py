queries = {
 'Krienen primate interneuron':'Krienen primate interneuron repertoire',
 'Bakken motor cortex cross-species':'Bakken comparative motor cortex human marmoset mouse',
 'Jorstad great ape cortex':'Jorstad comparative transcriptomics human cortex',
 'Ma DLPFC primate':'Ma molecular cellular evolution primate dorsolateral prefrontal cortex',
 'Hodge human MTG':'Hodge conserved cell types divergent human mouse cortex',
 'Chen macaque whole brain stereo-seq':'Chen macaque whole-brain spatial transcriptome',
 'Fang MERFISH human mouse cortex':'Fang conservation divergence cortical MERFISH human mouse',
 'BICAN human brain atlas':'Siletti transcriptomic diversity human brain cell types',
 'macaque MERFISH cortex':'macaque cortex MERFISH interneuron spatial',
 'marmoset cortex atlas':'marmoset cortex single cell atlas interneuron',
}
hits={}
for k,q in queries.items():
    res=pubmed_search(q,retmax=6)
    ids=res['esearchresult']['idlist']
    hits[k]=ids
    print('###',k,'->',ids)
    time.sleep(0.34)
