# Biomedical identifier choice guidelines

These guidelines have been informed by a combination of the following:

* the [availability of such identifiers](https://prop-explorer.toolforge.org/) on Wikidata;
* the ontologies used in the Common Fund Data Ecosystem's [Crosscut Metadata Model](https://data.cfde.cloud/documentation/C2M2); and
* the prefixes preferred for identifiers in the Biolink Model (specifically those listed for [AnatomicalEntities](https://biolink.github.io/biolink-model/AnatomicalEntity/#valid-id-prefixes), [ChemicalEntities](https://biolink.github.io/biolink-model/ChemicalEntity/#valid-id-prefixes), [MolecularEntities](https://biolink.github.io/biolink-model/MolecularEntity/#valid-id-prefixes), and [NucleicAcidEntities](https://biolink.github.io/biolink-model/NucleicAcidEntity/#valid-id-prefixes)).

Each ID listed below is followed by a IRI format that references to entities through that ID should use (that is, by substituting "$1" with the ID in question) as well as RDF predicates that would be used to link an entity to its identifier string.

## Converting to preferred identifiers

RENCI provides a [node normalizer](https://nodenormalization-sri.renci.org/docs#/) that may be used to convert data using non-preferred identifiers to preferred ones if they exist.

If the node normalizer's output is not satisfactory, you may be able to make a mapping happen through identifiers present on Wikidata; get in touch with [Mahir](mailto:morshedm@renci.org) for help with this.

### Identifiers with broad scopes

These are identifiers that can refer to a wide variety of classes. While their use is dispreferred for those entity classes listed underneath this section, their use may still be tolerated for entity types falling outside of those classes.

* Wikidata item IDs (Qids, e.g. http://www.wikidata.org/entity/Q42)
* [UMLS CUIs](https://evsexplore.semantics.cancer.gov/evsexplore/welcome?terminology=ncim) ([wdt:P2892](http://www.wikidata.org/prop/direct/P2892)) (e.g. https://identifiers.org/umls:C0037379)
    * ~740k IDs mapped to Wikidata
* [NCIt IDs](https://www.ebi.ac.uk/ols4/ontologies/ncit) ([wdt:P1748](http://www.wikidata.org/prop/direct/P1748)) (e.g. http://purl.obolibrary.org/obo/NCIT_C20047)
    * ~12k IDs (out of 200k) mapped to Wikidata
* [MeSH concepts](https://id.nlm.nih.gov/mesh/) ([wdt:P6694](http://www.wikidata.org/prop/direct/P6694)) (e.g. http://id.nlm.nih.gov/mesh/M0000115)
    * ~1.2k IDs (out of ~450k) mapped to Wikidata
    * cf. [MeSH tree codes](https://meshb-prev.nlm.nih.gov/treeView) ([wdt:P672](http://www.wikidata.org/prop/direct/P672)) of which ~65k IDs have been mapped to Wikidata

## Relationship predicates

In general, if a relationship is indicated by a predicate in the [Biolink Model](https://biolink.github.io/biolink-model/predicates.html), that version of the predicate should be used to indicate that relationship (with the IRI prefix https://w3id.org/biolink/vocab/).

Biolink provides mappings from many Biolink predicates to those in other ontologies, both [in the main model definition](https://github.com/biolink/biolink-model/blob/master/biolink-model.yaml) and [in dedicated files](https://github.com/biolink/biolink-model/blob/master/predicate_mapping.yaml). The exact and close mappings provided by Biolink have been reproduced in tabular format below. (If a predicate is not listed in the table below, then Biolink does not provide a mapping for it.)

### Some prefix definitions for the relationship mappings table

* BFO: http://purl.obolibrary.org/obo/BFO_
* CHEMBL.MECHANISM: https://www.ebi.ac.uk/chembl/mechanism/inspect/
* CTD: http://ctdbase.org/
* DGIdb: https://www.dgidb.org/interaction_types
* ExO: http://purl.obolibrary.org/obo/ExO_
* GAMMA: http://translator.renci.org/GAMMA_
* GOREL: http://purl.obolibrary.org/obo/GOREL_
* GTEx: https://www.gtexportal.org/home/gene/
* IAO: http://purl.obolibrary.org/obo/IAO_
* RO: http://purl.obolibrary.org/obo/RO_
* SEMMEDDB: https://skr3.nlm.nih.gov/SemMedDB
* SIO: http://semanticscience.org/resource/SIO_
* SO: http://purl.obolibrary.org/obo/SO_
* wdt: http://www.wikidata.org/prop/direct/

### Table of Biolink relationship mappings

| BioLink | exact mappings | close mappings |
| --- | --- | -- |
| active in | RO:0002432 |  |
| actively involved in | RO:0002331 |  |
| acts upstream of | RO:0002263 |  |
| acts upstream of negative effect | RO:0004035 |  |
| acts upstream of or within | RO:0002264 |  |
| acts upstream of or within negative effect | RO:0004033 |  |
| acts upstream of or within positive effect | RO:0004032 |  |
| acts upstream of positive effect | RO:0004034 |  |
| affects | SEMMEDDB:AFFECTS; DGIdb:affects |  |
| affects abundance of | CTD:affects_abundance_of |
| affects activity of | CTD:affects_activity_of; DGIdb:modulator |
| affects degradation of | CTD:affects_degradation_of |
| affects expression of | CTD:affects_expression_of; GTEx:affects_expression_in |
| affects folding of | CTD:affects_folding_of |
| affects localization of | CTD:affects_localization_of; GOREL:0002003 |
| affects metabolic processing of | CTD:affects_metabolic_processing_of |
| affects molecular interaction | CTD:affects_molecular_interaction |
| affects molecular modification of | CTD:affects_molecular_modification_of |
| affects mutation rate of | CTD:affects_mutation_rate_of |
| affects secretion of | CTD:affects_secretion_of |
| affects secretion of | CTD:affects_secretion_of |
| affects sensitivity to | CTD:affects_response_to |  |
| affects splicing of | CTD:affects_splicing_of |
| affects splicing of | CTD:affects_splicing_of |
| affects synthesis of | CTD:affects_synthesis_of |
| affects transport of | CTD:affects_transport_of |
| affects uptake of | CTD:affects_uptake_of |
| ameliorates condition | RO:0003307 |  |
| augments | SEMMEDDB:AUGMENTS |
| author | dct:creator; wdt:P50 |  |
| binds |  | DGIdb:binder |
| biomarker for | NCIT:R39 |  |
| broad match | skos:broadMatch;  |  |
| broad synonym | oboInOwl:hasBroadSynonym |  |
| capable of | RO:0002215 |  |
| catalyzes | RO:0002327 |  |
| caused by | wdt:P828 |  |
| causes | SEMMEDDB:CAUSES; wdt:P1542; SNOMED:cause_of; RO:0003303 |  |
| chemical role mixin | CHEBI:51086 |  |
| chi squared statistic | STATO:0000030 |  |
| close match | skos:closeMatch; SEMMEDDB:same_as |  |
| colocalizes with | RO:0002325 |  |
| composed primarily of | RO:0002473 |  |
| contraindicated in | NCIT:C37933 |  |
| contributes to | RO:0002326 | IDO:0000664 |
| contributor | dct:contributor |  |
| correlated with | RO:0002610; PATO:correlates_with |  |
| created with | pav:createdWith |  |
| creation date | dct:createdOn; wdt:P577 |  |
| decreases abundance of | CTD:decreases_abundance_of |
| decreases activity of | CTD:decreases_activity_of; GAMMA:ic50; GAMMA:ki; DGIdb:vaccine; DGIdb:antagonist; DGIdb:blocker; DGIdb:channel_blocker; DGIdb:gating_inhibitor; CHEMBL.MECHANISM:antisense_inhibitor; CHEMBL.MECHANISM:blocker; CHEMBL.MECHANISM:inhibitor; CHEMBL.MECHANISM:negative_allosteric_modulator; CHEMBL.MECHANISM:negative_modulator; DGIdb:negative_modulator; DGIdb:inverse_agonist; SEMMEDDB:INHIBITS; DGIdb:inhibitor |
| decreases degradation of | CTD:decreases_degradation_of; CTD:decreases_cleavage; CTD:decreases_hydrolysis |
| decreases expression of | RO:0003002; CTD:decreases_expression_of |
| decreases folding of | CTD:decreases_folding_of |
| decreases localization of | CTD:decreases_localization_of |
| decreases metabolic processing of | CTD:decreases_metabolic_processing_of |
| decreases molecular interaction | CTD:decreases_molecular_interaction |
| decreases molecular modification of | CTD:decreases_molecular_modification_of |
| decreases mutation rate of | CTD:decreases_mutation_rate_of; CTD:decreases_mutagenesis |
| decreases secretion of | CTD:decreases_secretion_of |
| decreases secretion of | CTD:decreases_secretion_of |
| decreases sensitivity to | CTD:decreases_response_to |  |
| decreases splicing of | CTD:decreases_splicing_of |
| decreases splicing of | CTD:decreases_splicing_of; CTD:decreases_RNA_splicing |
| decreases synthesis of | CTD:decreases_synthesis_of |
| decreases transport of | CTD:decreases_transport_of |
| decreases uptake of | CTD:decreases_uptake_of |
| deprecated | oboInOwl:ObsoleteClass |  |
| derives from | RO:0001000; FMA:derives_from; DOID-PROPERTY:derives_from |  |
| derives into | RO:0001001; SEMMEDDB:CONVERTS_TO; FMA:derives |  |
| description | IAO:0000115; skos:definitions |  |
| develops from | BTO:develops_from; DDANAT:develops_from; FMA:develops_from; RO:0002202 | RO:0002203; FMA:develops_into |
| diagnoses | DrugCentral:5271; SEMMEDDB:DIAGNOSES | NCIT:C15220; SIO:001331 |
| directly physically interacts with | RO:0002436 |  |
| disease has location | RO:0004026; MONDO:disease_has_location |  |
| disrupts | SEMMEDDB:DISRUPTS; CHEMBL.MECHANISM:disrupting_agent |  |
| distribution download url | dcat:downloadURL |  |
| drug regulatory status world wide | NCIT:C172573 |  |
| editor | wdt:P98 |  |
| enabled by | RO:0002333 |  |
| enables | RO:0002327 |  |
| end coordinate | gff3:end | faldo:end |
| end interbase coordinate |  | faldo:end |
| entity negatively regulates entity | RO:0002212; RO:0002449 |
| entity positively regulates entity | RO:0002450 |
| exacerbates condition | RO:0003309 |  |
| exact match | skos:exactMatch; ; WIKIDATA:P2888 |  |
| exact synonym | oboInOwl:hasExactSynonym |  |
| expressed in | RO:0002206 |  |
| expresses | RO:0002292 |  |
| format | dct:format; wdt:P2701 |  |
| gene product of | RO:0002204 |  |
| genetically associated with | wdt:P2293 |  |
| genetically interacts with | RO:0002435 |  |
| genome build | gff3:strand |  |
| has attribute | SIO:000008 | OBI:0001927 |
| has chemical formula | wdt:P274 |  |
| has completed | CL:has_completed |  |
| has confidence score | SEPIO:0000168 | SEPIO:0000187; SEPIO:0000167 |
| has count | LOINC:has_count |  |
| has evidence | RO:0002558 |  |
| has gene product | RO:0002205; wdt:P688; NCIT:gene_encodes_gene_product | PR:has_gene_template |
| has input | RO:0002233; SEMMEDDB:USES |  |
| has member | RO:0002351; skos:member |  |
| has metabolite | CHEBI:25212 |  |
| has not completed | CL:has_not_completed |  |
| has numeric value | qud:quantityValue |  |
| has output | RO:0002234 |  |
| has part | BFO:0000051; BFO:0000055; wdt:P527; RO:0001019; RXNORM:consists_of; RXNORM:has_part |  |
| has participant | RO:0000057; RO:has_participant | wdt:P2283 |
| has phenotype | RO:0002200 |  |
| has plasma membrane part | RO:0002104 |  |
| has quantitative value | qud:quantityValue |  |
| has receptor | ExO:0000001 |  |
| has route | ExO:0000055 |  |
| has sequence location | faldo:location |  |
| has side effect | NCIT:C2861 |  |
| has stressor | ExO:0000000 |  |
| has supporting studies |  | OBAN:has_study_id |
| has topic | foaf:topic |  |
| has unit | qud:unit; IAO:0000039 | EFO:0001697; UO-PROPERTY:is_unit_of |
| has variant part | GENO:0000382 |  |
| homologous to | RO:HOM0000001; SIO:010302 |  |
| id | AGRKB:primaryId; gff3:ID; gpi:DB_Object_ID |  |
| in linkage disequilibrium with | NCIT:C16798 |  |
| in taxon | RO:0002162; wdt:P703 |  |
| in taxon label | wdt:P225 |  |
| increases abundance of | CTD:increases_abundance_of |
| increases activity of | CTD:increases_activity_of; CHEMBL.MECHANISM:opener; CHEMBL.MECHANISM:positive_modulator; CHEMBL.MECHANISM:releasing_agent; DGIdb:activator; DGIdb:agonist |
| increases degradation of | CTD:increases_degradation_of; CTD:increases_cleavage; CTD:increases_hydrolysis; GOREL:0002004 |
| increases expression of | RO:0003003; CTD:increases_expression_of |
| increases folding of | CTD:increases_folding_of |
| increases localization of | CTD:increases_localization_of |
| increases metabolic processing of | CTD:increases_metabolic_processing_of |
| increases molecular interaction | CTD:increases_molecular_interaction |
| increases molecular modification of | CTD:increases_molecular_modification_of |
| increases mutation rate of | CTD:increases_mutation_rate_of; CTD:increases_mutagenesis |
| increases secretion of | CTD:increases_secretion_of |
| increases secretion of | CTD:increases_secretion_of |
| increases sensitivity to | CTD:increases_response_to |  |
| increases splicing of | CTD:increases_splicing_of |
| increases splicing of | CTD:increases_splicing_of; CTD:increases_RNA_splicing |
| increases synthesis of | CTD:increases_synthesis_of |
| increases transport of | CTD:increases_transport_of |
| increases uptake of | CTD:increases_uptake_of |
| inheritance | OMIM:has_inheritance_type |  |
| interacting molecules category | MI:1046 |  |
| interacts with | SEMMEDDB:INTERACTS_WITH |  |
| iri | wdt:P854 |  |
| is frameshift variant of | SO:0001589 |  |
| is input of | RO:0002352 |  |
| is metabolite | CHEBI:25212 |  |
| is metabolite of | CHEBI:25212 |  |
| is missense variant of | SO:0001583 |  |
| is output of | RO:0002353 |  |
| is splice site variant of | SO:0001629 |  |
| is synonymous variant of | SO:0001819 |  |
| iso abbreviation | wdt:P1160 |  |
| issue | wdt:P433 |  |
| knowledge source |  | pav:providedBy |
| lacks part | CL:lacks_part; PR:lacks_part |  |
| latitude | wgs:lat |  |
| license | dct:license |  |
| located in | RO:0001025; FMA:has_location |  |
| location of | RO:0001015; SEMMEDDB:LOCATION_OF; wdt:P276; FMA:location_of |  |
| logical interpretation | os:LogicalInterpretation |  |
| longitude | wgs:long |  |
| manifestation of | SEMMEDDB:MANIFESTATION_OF; OMIM:manifestation_of |  |
| mechanism of action | NCIT:C54680; MI:2044; LOINC:MTHU019741 |  |
| member of | RO:0002350 | skos:member |
| mentions | IAO:0000142 |  |
| mesh terms | dcid:MeSHTerm |  |
| model of | RO:0003301 |  |
| name | gff3:Name; gpi:DB_Object_Name |  |
| narrow match | skos:narrowMatch;  |  |
| narrow synonym | oboInOwl:hasNarrowSynonym |  |
| negatively correlated with | CTD:negative_correlation |  |
| object | owl:annotatedTarget; OBAN:association_has_object |  |
| occurs in | BFO:0000066; PathWhiz:has_location; SNOMED:occurs_in | BFO:0000067; SNOMED:has_occurrence; UBERON:site_of |
| opposite of | RO:0002604 |  |
| orthologous to | RO:HOM0000017; wdt:P684 |  |
| overlaps | RO:0002131 |  |
| p value | OBI:0000175; NCIT:C44185; EDAM-DATA:1669 |  |
| pages | wdt:P304 |  |
| paralogous to | RO:HOM0000011 |  |
| part of | BFO:0000050; SEMMEDDB:PART_OF; wdt:P361; FMA:part_of; RXNORM:constitutes; RXNORM:part_of |  |
| participates in | RO:0000056; BFO:0000056 |  |
| phase | gff3:phase |  |
| positively correlated with | CTD:positive_correlation |  |
| preceded by | BFO:0000062 |  |
| precedes | BFO:0000063; SEMMEDDB:PRECEDES; SNOMED:occurs_before | RO:0002263; RO:0002264 |
| predicate | owl:annotatedProperty; OBAN:association_has_predicate |  |
| process negatively regulates process | RO:0002212 |
| process positively regulates process | RO:0002213 |
| produced by | RO:0003001 |  |
| produces | RO:0003000; wdt:P1056; SEMMEDDB:PRODUCES |  |
| published in | wdt:P1433 |  |
| publisher | dct:publisher; wdt:P123 |  |
| regulates | RO:0002448 |  |
| related condition | GENO:0000790 |  |
| related synonym | oboInOwl:hasRelatedSynonym |  |
| related to | UMLS:related_to |  |
| retrieved on | pav:retrievedOn |  |
| rights | dct:rights |  |
| same as | owl:sameAs; skos:exactMatch; wdt:P2888; CHEMBL.MECHANISM:equivalent_to; MONDO:equivalentTo | owl:equivalentClass |
| similar to | RO:HOM0000000; SO:similar_to |  |
| start coordinate | gff3:start | faldo:begin |
| start interbase coordinate |  | faldo:begin |
| strand | gff3:strand |  |
| subclass of | rdfs:subClassOf; SEMMEDDB:ISA; wdt:P279; CHEMBL.MECHANISM:subset_of; GO:isa; MESH:isa; RXNORM:isa; VANDF:isa | LOINC:class_of; LOINC:has_class |
| subject | owl:annotatedSource; OBAN:association_has_subject |  |
| summary | dct:abstract;  |  |
| superclass of | ; CHEMBL.MECHANISM:superset_of; GO:inverse_isa; RXNORM:inverse_isa; MESH:inverse_isa; VANDF:inverse_isa |  |
| symbol | AGRKB:symbol; gpi:DB_Object_Symbol |  |
| temporally related to | SNOMED:temporally_related_to |  |
| transcribed from | RO:0002510; SIO:010081 |  |
| transcribed to | RO:0002511; SIO:010080 |  |
| translates to |  | RO:0002513; SIO:010082 |
| translation of |  | RO:0002512; SIO:010083 |
| treated by | wdt:P2176; MONDO:disease_responds_to |  |
| treats | DRUGBANK:treats; wdt:P2175 |  |
| treats or applied or studied to treat | SEMMEDDB:TREATS |  |
| type | gff3:type; gpi:DB_Object_Type |  |
| version of | dct:isVersionOf |  |
| volume | wdt:P478 |  |
| xenologous to | RO:HOM0000018 |  |
| z score | STATO:0000104; NCIT:C68741; EDAM-DATA:1668 |  |

## Entity classes

### Anatomical entities

Prefer [UBERON IDs](https://obophenotype.github.io/uberon/) (http://purl.obolibrary.org/obo/UBERON_$1) ([wdt:P1554](http://www.wikidata.org/prop/direct/P1554))

* Disclaimer: some Fabric team members have been part of UBERON's development
* ~6000k IDs (out of at least 16k) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present
* cf. [FMA IDs](https://www.ebi.ac.uk/ols4/ontologies/fma) where ~79k (out of around 104k) have been mapped to Wikidata

### Chemical entities (compounds, substances)

Prefer [PubChem CIDs](https://pubchem.ncbi.nlm.nih.gov/) (http://rdf.ncbi.nlm.nih.gov/pubchem/compound/CID$1) ([wdt:P662](http://www.wikidata.org/prop/direct/P662))

* CAS registry numbers are imprecise (per [Tom Luechtefeld](mailto:tom@insilica.co))
    * BioBricks/SPOKE standardizing on PubChem CIDs already
* 1.3m IDs (out of ~111m) mapped to Wikidata; we may need to federate with other external sources

### Data types/file formats

Prefer [EDAM IDs](https://edamontology.org/page)

* (No Wikidata identifier property for this; must map from Wikidata item to RDF URL using [identifier mappings](https://frink.apps.renci.org/ldf/identifier-mappings))
* Only 44 IDs mapped to Wikidata; no harm in adding remainder to Wikidata if not already present

### Diseases

Prefer [Monarch Disease Ontology IDs](https://github.com/monarch-initiative/mondo) (http://purl.obolibrary.org/obo/MONDO_$1) ([wdt:P5270](http://www.wikidata.org/prop/direct/P5270))

* Disclaimer: some Fabric team members have been part of MONDO's development
* 19k IDs (out of at least 26k) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present
* cf. [DOID IDs](https://www.ebi.ac.uk/ols4/ontologies/doid) where all(?) IDs have been mapped to Wikidata

### Genes

Prefer [Entrez gene IDs](https://www.ncbi.nlm.nih.gov/gene/) (http://purl.uniprot.org/geneid/$1) ([wdt:P351](http://www.wikidata.org/prop/direct/P351))

* 794k IDs mapped to Wikidata; we may need to federate with other external sources

### Phenotypes

Prefer [HPO IDs](https://hpo.jax.org/) (http://purl.obolibrary.org/obo/HP_$1) ([wdt:P3841](http://www.wikidata.org/prop/direct/P3841))

* ~2k IDs (out of 20k+) mapped to Wikidata; no harm in adding remainder to Wikidata if not already present

### Proteins

Prefer [UniProt protein IDs](https://www.uniprot.org/uniprotkb/) (http://purl.uniprot.org/uniprot/$1) ([wdt:P352](http://www.wikidata.org/prop/direct/P352))

* 627 IDs (out of at least 8.2m) mapped to Wikidata; we may need to federate with other external sources

### Publications (references)

Prefer [DOIs](https://doi.org) (http://dx.doi.org/$1) ([wdt:P356](http://www.wikidata.org/prop/direct/P356)) if present

* [PubMed IDs](https://pubmed.ncbi.nlm.nih.gov) ([wdt:P698](http://www.wikidata.org/prop/direct/P698)) and [PMCIDs](https://www.ncbi.nlm.nih.gov/pmc/) ([wdt:P932](http://www.wikidata.org/prop/direct/P932)) may be allowed if no DOI exists

### Taxa

Prefer [NCBI taxa IDs](https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon) (http://purl.obolibrary.org/obo/NCBITaxon_$1) ([wdt:P685](http://www.wikidata.org/prop/direct/P685))

* 600k IDs (out of 2.7m) mapped to Wikidata; [Mahir](mailto:morshedm@renci.org) could try to map the remainder automatically (is already planning this with elurikkus.ee)
