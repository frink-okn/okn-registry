# Identifier choice guidelines

These guidelines are currently written with the ARCH graphs in mind, but may be expanded as needed to handle other domains.

These have been informed by, among other thing, the availability of such identifiers on Wikidata and the prefixes preferred for identifiers in the Biolink model.

Each ID listed below is followed by RDF predicates that would be used to link an entity to its identifier string.

## Chemical entities

Prefer [PubChem CIDs](https://pubchem.ncbi.nlm.nih.gov/) ([wdt:P662](http://www.wikidata.org/prop/direct/P662))

* CAS registry numbers are imprecise (per Tom of BioBricks); BioBricks/SPOKE standardizing on PubChem CIDs already
* 1.3m IDs (out of ~111m) mapped to Wikidata; we may need to federate with other external sources

## Taxa

Prefer [NCBI taxa IDs](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) ([wdt:P685](http://www.wikidata.org/prop/direct/P685))

* 600k IDs (out of 2.7m) mapped to Wikidata; [Mahir](mailto:morshedm@renci.org) could try to map the remainder automatically (is already planning this with elurikkus.ee)

## Genes

Prefer [Entrez gene IDs](https://www.ncbi.nlm.nih.gov/gene/) ([wdt:P351](http://www.wikidata.org/prop/direct/P351))

* 794k IDs mapped to Wikidata; we may need to federate with other external sources

## Proteins

Prefer [UniProt protein IDs](https://www.uniprot.org/uniprotkb/) ([wdt:P352](http://www.wikidata.org/prop/direct/P352))

* 627 IDs (out of at least 8.2m) mapped to Wikidata; we may need to federate with other external sources

## Diseases

Prefer [Monarch Disease Ontology IDs](https://github.com/monarch-initiative/mondo) ([wdt:P5270](http://www.wikidata.org/prop/direct/P5270))

* 19k IDs (out of at least 26k) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present

## Reference publications

Prefer [DOIs](https://doi.org) ([wdt:P356](http://www.wikidata.org/prop/direct/P356)) if present

* PubMed IDs and PMCIDs may be allowed if no DOI exists
