# Biomedical identifier choice guidelines

These guidelines have been informed by a combination of the following:

* the [availability of such identifiers](https://prop-explorer.toolforge.org/) on Wikidata;
* the ontologies used in the Common Fund Data Ecosystem's [Crosscut Metadata Model](https://data.cfde.cloud/documentation/C2M2); and
* the prefixes preferred for identifiers in the Biolink Model (specifically those listed for [AnatomicalEntities](https://biolink.github.io/biolink-model/AnatomicalEntity/#valid-id-prefixes), [ChemicalEntities](https://biolink.github.io/biolink-model/ChemicalEntity/#valid-id-prefixes), [MolecularEntities](https://biolink.github.io/biolink-model/MolecularEntity/#valid-id-prefixes), and [NucleicAcidEntities](https://biolink.github.io/biolink-model/NucleicAcidEntity/#valid-id-prefixes)).

Each ID listed below is followed by a IRI format that references to entities through that ID should use (that is, by substituting "$1" with the ID in question) as well as RDF predicates that would be used to link an entity to its identifier string.

## Converting to preferred identifiers

RENCI provides a [node normalizer](https://nodenormalization-sri.renci.org/docs#/) that may be used to convert data using non-preferred identifiers to preferred ones if they exist.

If the node normalizer's output is not satisfactory, you may be able to make a mapping happen through identifiers present on Wikidata; get in touch with [Mahir](mailto:morshedm@renci.org) for help with this.

## Identifiers with broad scopes

These are identifiers that can refer to a wide variety of classes. While their use is dispreferred for those entity classes listed underneath this section, their use may still be tolerated for entity types falling outside of those classes.

* Wikidata item IDs (Qids, e.g. http://www.wikidata.org/entity/Q42)
* [UMLS CUIs](https://evsexplore.semantics.cancer.gov/evsexplore/welcome?terminology=ncim) ([wdt:P2892](http://www.wikidata.org/prop/direct/P2892)) (e.g. https://identifiers.org/umls:C0037379)
  * ~740k IDs mapped to Wikidata
* [NCIt IDs](https://www.ebi.ac.uk/ols4/ontologies/ncit) ([wdt:P1748](http://www.wikidata.org/prop/direct/P1748)) (e.g. http://purl.obolibrary.org/obo/NCIT_C20047)
  * ~12k IDs (out of 200k) mapped to Wikidata
* [MeSH concepts](https://id.nlm.nih.gov/mesh/) ([wdt:P6694](http://www.wikidata.org/prop/direct/P6694)) (e.g. http://id.nlm.nih.gov/mesh/M0000115)
  * ~1.2k IDs (out of ~450k) mapped to Wikidata
  * cf. [MeSH tree codes](https://meshb-prev.nlm.nih.gov/treeView) ([wdt:P672](http://www.wikidata.org/prop/direct/P672)) of which ~65k IDs have been mapped to Wikidata

## Anatomical entities

Prefer [UBERON IDs](https://obophenotype.github.io/uberon/) (http://purl.obolibrary.org/obo/UBERON_$1) ([wdt:P1554](http://www.wikidata.org/prop/direct/P1554))

* Disclaimer: some Fabric team members have been part of UBERON's development
* ~6000k IDs (out of at least 16k) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present
* cf. [FMA IDs](https://www.ebi.ac.uk/ols4/ontologies/fma) where ~79k (out of around 104k) have been mapped to Wikidata

## Chemical entities (compounds, substances)

Prefer [PubChem CIDs](https://pubchem.ncbi.nlm.nih.gov/) (http://rdf.ncbi.nlm.nih.gov/pubchem/compound/CID$1) ([wdt:P662](http://www.wikidata.org/prop/direct/P662))

* CAS registry numbers are imprecise (per [Tom Luechtefeld](mailto:tom@insilica.co))
  * BioBricks/SPOKE standardizing on PubChem CIDs already
* 1.3m IDs (out of ~111m) mapped to Wikidata; we may need to federate with other external sources

## Data types/file formats

Prefer [EDAM IDs](https://edamontology.org/page)

* (No Wikidata identifier property for this; must map from Wikidata item to RDF URL using [identifier mappings](https://frink.apps.renci.org/ldf/identifier-mappings))
* Only 44 IDs mapped to Wikidata; no harm in adding remainder to Wikidata if not already present

## Diseases

Prefer [Monarch Disease Ontology IDs](https://github.com/monarch-initiative/mondo) (http://purl.obolibrary.org/obo/MONDO_$1) ([wdt:P5270](http://www.wikidata.org/prop/direct/P5270))

* Disclaimer: some Fabric team members have been part of MONDO's development
* 19k IDs (out of at least 26k) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present
* cf. [DOID IDs](https://www.ebi.ac.uk/ols4/ontologies/doid) where all(?) IDs have been mapped to Wikidata

## Genes

Prefer [Entrez gene IDs](https://www.ncbi.nlm.nih.gov/gene/) (http://purl.uniprot.org/geneid/$1) ([wdt:P351](http://www.wikidata.org/prop/direct/P351))

* 794k IDs mapped to Wikidata; we may need to federate with other external sources

## Phenotypes

Prefer [HPO IDs](https://hpo.jax.org/) (http://purl.obolibrary.org/obo/HP_$1) ([wdt:P3841](http://www.wikidata.org/prop/direct/P3841))

* ~2k IDs (out of 20k+) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present

## Proteins

Prefer [UniProt protein IDs](https://www.uniprot.org/uniprotkb/) (http://purl.uniprot.org/uniprot/$1) ([wdt:P352](http://www.wikidata.org/prop/direct/P352))

* 627 IDs (out of at least 8.2m) mapped to Wikidata; we may need to federate with other external sources

## Publications (references)

Prefer [DOIs](https://doi.org) (http://dx.doi.org/$1) ([wdt:P356](http://www.wikidata.org/prop/direct/P356)) if present

* [PubMed IDs](https://pubmed.ncbi.nlm.nih.gov) ([wdt:P698](http://www.wikidata.org/prop/direct/P698)) and [PMCIDs](https://www.ncbi.nlm.nih.gov/pmc/) ([wdt:P932](http://www.wikidata.org/prop/direct/P932)) may be allowed if no DOI exists

## Taxa

Prefer [NCBI taxa IDs](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) (http://purl.obolibrary.org/obo/NCBITaxon_$1) ([wdt:P685](http://www.wikidata.org/prop/direct/P685))

* 600k IDs (out of 2.7m) mapped to Wikidata; [Mahir](mailto:morshedm@renci.org) could try to map the remainder automatically (is already planning this with elurikkus.ee)
