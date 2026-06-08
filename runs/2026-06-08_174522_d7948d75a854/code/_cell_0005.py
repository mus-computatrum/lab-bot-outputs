g = fetch("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136802&targ=self&form=text&view=brief")
for line in g.splitlines():
    if any(k in line for k in ['Series_title','Series_type','Series_summary','relation','SubSeries','sample_id','overall_design','supplementary']):
        print(line[:300])