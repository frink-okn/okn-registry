---
template: overrides/kg.html
shortname: ncipidkg
title: NCI-PID 2.0 KG
description: The NCI-PID 2.0 Knowledge Graph converts NCI Pathway Interaction Database version 2.0 networks into RDF, capturing protein interactions, signaling pathways, and post-translational modifications enriched with INDRA evidence metadata.
stats: https://frink.renci.org/kg-stats/ncipidkg
homepage: https://www.ndexbio.org/index.html#/networkset/7bc65b82-2a2f-11ed-ac45-0ac135e8bacf
# funding: NSF Proto-OKN
sparql: https://frink.apps.renci.org/ncipidkg/sparql
tpf: https://frink.apps.renci.org/ldf/ncipidkg
frink-options:
  lakefs-repo: ncipidkg
  documentation-path: ncipidkg
contact:
  email: support@ndexbio.org
  github: ""
  label: "Cytoscape and NDEx Team"
---

The NCI-PID 2.0 Knowledge Graph (NCI-PID 2.0 KG) is a semantic knowledge graph derived from the NCI Pathway Interaction Database (NCI-PID) version 2.0 networks. These networks represent curated biomolecular interactions and cellular signaling pathways, enhanced with evidence from the INDRA (Integrated Network and Dynamical Reasoning Assembler) system.

The knowledge graph is constructed by converting 196 NCI-PID 2.0 pathway networks from the Cytoscape CX2 format into RDF (Resource Description Framework) using standard biological ontologies. The source networks are publicly available on NDEx (Network Data Exchange).

## Key Features

- **Protein Interactions**: Captures binding, activation, inhibition, and post-translational modification relationships between proteins identified by UniProt accessions
- **Evidence Provenance**: Each relationship is annotated with INDRA evidence counts, source database attribution (INDRA and/or NCI-PID), and links to supporting evidence
- **Standard Ontologies**: Uses Relations Ontology (RO) predicates for relationship semantics, Gene Ontology (GO) biological process terms for post-translational modification types, and Semanticscience Integrated Ontology (SIO) for entity typing
- **RDF Reification**: Relationships are reified to attach evidence metadata, enabling queries at multiple levels of abstraction

## Ontologies Used

| Prefix | Ontology | Usage |
|--------|----------|-------|
| RO | Relations Ontology | Relationship predicates (binds, activates, inhibits, regulates) |
| GO | Gene Ontology | PTM process types (phosphorylation, ubiquitination, sumoylation) |
| SIO | Semanticscience Integrated Ontology | Entity types (protein, complex, gene product) |
| UniProt | UniProt | Protein entity identifiers |
| CHEBI | Chemical Entities of Biological Interest | Small molecule and chemical entity types |

## Funding

This work is supported by the NSF Proto-OKN (Prototype Open Knowledge Network) program, the NIH NCI NDEx project (5U24CA269436), and the NIH NHGRI Cytoscape project (5U24HG012107).

## References

Pillich RT, Chen J, Churas C, Fong D, Gyori BM, Ideker T, Karis K, Liu SN, Ono K, Pico A, Pratt D. NDEx IQuery: a multi-method network gene set analysis leveraging the Network Data Exchange. Bioinformatics. 2023 Mar 1;39(3):btad118. [doi: 10.1093/bioinformatics/btad118](https://doi.org/10.1093/bioinformatics/btad118)
