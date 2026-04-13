# Environmental identifier choice guidelines

The pages on biomedical identifiers and geospatial identifiers may also be worth consulting, though some sections of the former are also reproduced below.

## Entity classes

### Chemical entities (compounds, substances)

Prefer [PubChem CIDs](https://pubchem.ncbi.nlm.nih.gov/) (http://rdf.ncbi.nlm.nih.gov/pubchem/compound/CID$1) ([wdt:P662](http://www.wikidata.org/prop/direct/P662))

* CAS registry numbers are imprecise (per [Tom Luechtefeld](mailto:tom@insilica.co))
    * BioBricks/SPOKE standardizing on PubChem CIDs already
* 1.3m IDs (out of ~111m) mapped to Wikidata; we may need to federate with other external sources

### Taxa

Prefer [NCBI taxa IDs](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) (http://purl.obolibrary.org/obo/NCBITaxon_$1) ([wdt:P685](http://www.wikidata.org/prop/direct/P685))

* 600k IDs (out of 2.7m) mapped to Wikidata; [Mahir](mailto:morshedm@renci.org) could try to map the remainder automatically (is already planning this with elurikkus.ee)
