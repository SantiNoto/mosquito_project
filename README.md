# mosquito_project
find relevant mosquito fst peaks

requeriments:
  -python 3.7.10

  -pandas
  
  -gseapy

The relevant files are:

 'window_from_fst.py': function that generates windows of different sizes using the chromosomes and positions for a given mosquito-insecticide pair, as provided by Eric. 

'run_single_GSEA_for_all.ipynb': python notebook to run GSEA on the mosquito data, using only the "true" Fst (not the randomised Fst)
