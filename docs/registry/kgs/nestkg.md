---
template: overrides/kg.html
shortname: nestkg
title: NeST KG
description: The NeST (Nested Systems in Tumors) Knowledge Graph converts the NeST hierarchical map of cancer protein systems into RDF, together with the IAS (Integrated Association Stringency) protein-association network from which the map was derived. It captures the nested containment hierarchy of protein systems, their member proteins, per-system cancer-mutation statistics and MONDO-typed cancer associations, and ~210k scored protein-protein associations as reified statements.
stats: https://registry.okn.us/kg-stats/nestkg
homepage: https://www.ndexbio.org/viewer/networks/9a8f5326-aa6e-11ea-aaef-0ac135e8bacf
# funding: NSF Proto-OKN
sparql: https://apps.okn.us/nestkg/sparql
tpf: https://apps.okn.us/ldf/nestkg
frink-options:
  lakefs-repo: nestkg
  documentation-path: nestkg
contact:
  email: support@ndexbio.org
  github: ""
  label: "Cytoscape and NDEx Team"
license: "https://creativecommons.org/licenses/by/4.0/"
---

The NeST (Nested Systems in Tumors) Knowledge Graph (NeST KG) is a semantic knowledge graph derived from the NeST hierarchical map of human cancer protein systems. NeST organizes proteins into a nested hierarchy of physical assemblies and functional systems, inferred from integration of large-scale protein-protein interaction and cancer proteomics data.

The knowledge graph is constructed by converting the NeST networks from the Cytoscape CX2 format into RDF (Resource Description Framework) using standard biological ontologies. The source networks are publicly available on NDEx (Network Data Exchange).

## Key Features

- **Nested System Hierarchy**: Captures the containment relationships between protein systems, representing how smaller assemblies nest within larger functional systems
- **System Membership**: Associates proteins (identified by UniProt accessions, or numeric HGNC identifiers for the 12 symbols with no protein product) with the systems they belong to
- **System Annotations**: Every system carries its size (`ndexv:memberCount`) and HiSig significance statistics (lasso weight, BH-adjusted p-value); systems significantly mutated in a cohort additionally carry cancer associations with a tumors-mutated fraction
- **Standard Ontologies**: Uses [Biolink Model](https://biolink.github.io/biolink-model/) predicates for containment (`biolink:part_of`), system membership (`biolink:has_member`) and protein association (`biolink:interacts_with`), together with Biolink's `Association` pattern for system–cancer links; Semanticscience Integrated Ontology (SIO) for entity typing; and MONDO and ECO for cancer types and evidence codes.
- **Querying**: `biolink:interacts_with` is symmetric but stored in one direction only — match both (`?a ^biolink:interacts_with|biolink:interacts_with ?b`). Per-edge IAS scores live on reified `rdf:Statement` nodes, not on the asserted triple.

## Ontologies Used

| Prefix | Ontology | Usage |
|--------|----------|-------|
| biolink | Biolink Model | Containment (`part_of`), system membership (`has_member`), protein associations (`interacts_with`), and association structure (`Association`, `genetically_associated_with`, `knowledge_level`, `agent_type`, `has_evidence`) |
| SIO | Semanticscience Integrated Ontology | Entity types — `SIO:010043` (protein), `SIO:010035` (gene) |
| UniProt | UniProt | Protein entity identifiers |
| HGNC | HGNC | Gene entity identifiers — the 12 symbols with no protein product |
| MONDO | Mondo Disease Ontology | Cancer types in system→disease associations (14 types, incl. pan-cancer `MONDO:0004992`) |
| ECO | Evidence & Conclusion Ontology | Evidence code on each association |
| STATO, OBI, NCIT | — | Referenced via `rdfs:seeAlso` on the statistical properties |
| ndexv, nestv, iasv | Minted (NDEx) | `ndexv:ProteinSystem`, `ndexv:memberCount`, HiSig weight/p-value, IAS score |

## Funding

This work is supported by the NSF Proto-OKN (Prototype Open Knowledge Network) program, the NIH NCI NDEx project (5U24CA269436), and the NIH NHGRI Cytoscape project (5U24HG012107).

## References

Zheng F, Kelly MR, Ramms DJ, Heintschel ML, Tao K, Tutuncuoglu B, Lee JJ, Ono K, Foussard H, Chen M, Herrington KA, Silva E, Liu SN, Chen J, Churas C, Wilson N, Kratz A, Pillich RT, Patel DN, Park J, Kuenzi B, Yu MK, Licon K, Pratt D, Kreisberg JF, Kim M, Swaney DL, Nan X, Fraley SI, Gutkind JS, Krogan NJ, Ideker T. Interpretation of cancer mutations using a multiscale map of protein systems. Science. 2021 Oct;374(6563):eabf3067. [doi: 10.1126/science.abf3067](https://doi.org/10.1126/science.abf3067). PMID: 34591613; PMCID: PMC8590742.

Pratt D, Chen J, Welker D, Rivas R, Pillich R, Rynkov V, Ono K, Miello C, Hicks L, Szalma S, Stojmirovic A, Dobrin R, Braxenthaler M, Kuentzer J, Demchak B, Ideker T. NDEx, the Network Data Exchange. Cell Syst. 2015 Oct 28;1(4):302-305. [doi: 10.1016/j.cels.2015.10.001](https://doi.org/10.1016/j.cels.2015.10.001). PMID: 26594663; PMCID: PMC4649937.

Shannon P, Markiel A, Ozier O, Baliga NS, Wang JT, Ramage D, Amin N, Schwikowski B, Ideker T. Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome Res. 2003 Nov;13(11):2498-504. [doi: 10.1101/gr.1239303](https://doi.org/10.1101/gr.1239303). PMID: 14597658; PMCID: PMC403769.

Ono K, Fong D, Gao C, Churas C, Pillich R, Lenkiewicz J, Pratt D, Pico AR, Hanspers K, Xin Y, Morris J, Kucera M, Franz M, Lopes C, Bader G, Ideker T, Chen J. Cytoscape Web: bringing network biology to the browser. Nucleic Acids Res. 2025 Jul 7;53(W1):W203-W212. [doi: 10.1093/nar/gkaf365](https://doi.org/10.1093/nar/gkaf365). PMID: 40308211; PMCID: PMC12230733.
