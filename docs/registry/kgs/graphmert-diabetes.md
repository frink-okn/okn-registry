---
template: overrides/kg.html
shortname: graphmert-diabetes
title: GraphMERT Diabetes KG
description: Diabetes-related biomedical knowledge graph extracted from PubMed Central abstracts with GraphMERT, with per-triple provenance.
stats: https://registry.okn.us/kg-stats/graphmert-diabetes
homepage: https://openreview.net/forum?id=tnXSdDhvqc
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2216746
frink-options:
  lakefs-repo: graphmert-diabetes
  documentation-path: graphmert-diabetes
  kgf:
    semantics:
      prefixes:
        gm: "https://w3id.org/graphmert/diabetes/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "http://www.w3.org/2004/02/skos/core#altLabel"
      authoritative_namespaces:
        - gm
contacts:
  - email: margarita.bel@princeton.edu
    github: across-stars
    label: Margarita Belova
license: "https://creativecommons.org/licenses/by/4.0/"
---

# GraphMERT Diabetes KG

A knowledge graph of diabetes-related biomedical facts distilled from 350k PubMed Central
abstracts with **GraphMERT**, an encoder-only graph language model for distilling knowledge graphs from text. The graph has
**72,627 edges** (74,412 extracted triples) over **45,575 entities**. Relations use Biolink and RO predicates
(93% of edges), and 2,691 entities are ontology terms, mostly MONDO, HP, ChEBI, CL, UBERON or GO, so the graph joins
with other OKN graphs on these identifiers. Each triple is grouped with the source text sequence it was extracted from,
and 99% of triples link through that sequence to the PubMed Central article(s) it came from.

## Contents

- Entities are text phrases extracted from abstracts. Phrases that exactly match a MONDO, HP, ChEBI, CL, UBERON or
  GO term (name, or a hand-reviewed exact synonym) use the ontology IRI, with the extracted phrases as
  `skos:altLabel` and a Biolink category; the rest are `gm:entity/<id>` with the phrase as `rdfs:label`, a few with
  `skos:broadMatch`/`closeMatch`/`narrowMatch` to a related term. All are typed `gm:Entity`.
- GraphMERT predicts completion for the 28 UMLS (SNOMED CT) relations of the seed KG. On edges they are mapped to Biolink/RO predicates
  (`biolink:related_to`, `obo:RO_0000087` has role, `biolink:causes`, `biolink:subclass_of`,
  `biolink:has_part`, `biolink:located_in`, ...), with inverse relations published in the canonical direction;
  9 SNOMED-specific relations stay `gm:` (e.g. `gm:has_associated_morphology`).
- Every triple has a reified `rdf:Statement` that records the extracted relation (`gm:extractedRelation`) and whose
  `prov:wasDerivedFrom` points to a `gm:SourceSequence` (identified by `dcterms:identifier`), which in turn links to
  its PMC article(s) through `prov:wasDerivedFrom`. Article text is not distributed.

IRI patterns (namespace `https://w3id.org/graphmert/diabetes/`): `entity/<id>`, `statement/<id>`,
`sequence/<id>`, `vocab/<relation>`, `dataset`.

## How it was built

The pipeline uses a diabetes-related PubMed Central corpus and GraphMERT trained with seed-KG injection. Predicted tails are filtered by similarity, deduplicated and accepted by an LLM judge that sees only the source sequence. Triples identical to UMLS seed-KG triples were removed.

### Limitations

Triples are automatically extracted and LLM-checked; not intended for clinical use.

## Citation

Data and documentation: <https://github.com/across-stars/graphmert_diabetes_kg>

Extractor code: <https://github.com/jha-lab/graphmert_umls>

If you use this graph, please cite:

> Margarita Belova, Jiaxin Xiao, Shikhar Tuli, and Niraj Jha. *GraphMERT: Efficient and Scalable
> Distillation of Reliable Knowledge Graphs from Unstructured Data.* Transactions on Machine Learning
> Research, published 21 Feb 2026. <https://openreview.net/forum?id=tnXSdDhvqc>


## License

**CC BY 4.0.** You may use, share and adapt this graph, including commercially, as long as you give
appropriate credit. If you use it in your research or in any derived resource, please cite the paper above.


## Example questions

Questions the graph can answer:

- What does type 2 diabetes cause?
- Which drugs and compounds have an antidiabetic role?
- What is metformin associated with?
- What causes diabetic nephropathy?
- Which conditions or findings are located in the pancreatic islet?
- What are subtypes of diabetic retinopathy?
- Which conditions or factors are reported as the cause of the most different effects?
- Through which relations is HbA1c connected to other biomedical terms?
- What is both associated with obesity and a cause of cardiovascular disease?
- What are the two-step cause chains that start from hyperglycemia?
- Which source sequences support a given triple?
- How big is the graph and how should it be cited?
- Which relation types does the graph use, and how many triples does each have?
