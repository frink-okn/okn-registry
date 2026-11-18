---
template: overrides/kg.html
shortname: cognitive-kb
title: Cognitive Active Inference knowledge base
description: Concept pages on Active Inference and related fields, with typed and untyped relations and citation records, as SKOS/Dublin Core/schema.org RDF.
stats: https://registry.okn.us/kg-stats/cognitive-kb
homepage: https://github.com/ActiveInferenceInstitute/cognitive
sparql: https://apps.okn.us/cognitive-kb/sparql
tpf: https://apps.okn.us/kgf/cognitive-kb/latest/tpf
kgf: https://apps.okn.us/kgf/cognitive-kb
frink-options:
  lakefs-repo: cognitive-kb
  documentation-path: cognitive-kb
  kgf:
    # No roles: the federation defaults already cover every naming predicate
    # this graph uses (skos:prefLabel, dcterms:title, rdfs:label; skos:altLabel,
    # schema:alternateName; dcterms:description, rdfs:comment, skos:definition).
    semantics:
      prefixes:
        cognitive-kb: "https://purl.org/okn/frink/kg/cognitive-kb/"
      authoritative_namespaces:
        - cognitive-kb
contacts:
  - email: daniel@activeinference.institute
    github: docxology
    label: "Daniel Ari Friedman"
---

The knowledge base of the Active Inference Institute's `cognitive` repository as RDF. Every
page is a `schema:CreativeWork` document. Topic-bearing documents link through
`schema:about` and `dcterms:subject` to separate stable `/concept/<path>` SKOS
concepts in one concept scheme, grouped into domain `skos:Collection`s.
Conceptual relations have concept endpoints and explicit predicate meanings;
document references, citations, navigation, redirects and documentation relations
retain document endpoints. Ambiguous mixed-role assertions are preserved under
`https://purl.org/okn/frink/kg/cognitive-kb/relation/document/` without a SKOS
super-property. Body links use `dcterms:references`. Citation pages carry
authors, year and DOI (`schema:sameAs`). Explicit reviewed mappings use SKOS
predicates with source, rationale and review-date evidence. Unreviewed Wikidata
identifiers are `rdfs:seeAlso` discovery links. Tags point to concepts; citation
relations reuse BIBO. Provenance is `prov:wasDerivedFrom` the public
repository; repository-owned graph content is licensed under CC BY 4.0.
The graph serves public research and education by connecting explanatory concepts
and their literature across Active Inference, cognitive science, mathematics and
biology. SKOS correspondences apply to concept meanings and do not assert OWL
identity or clinical equivalence. No external grant funding is claimed.

A cross-graph query follows reviewed Wikidata mappings through the OKN
identifier-mappings graph to labeled OBO identifiers in Ubergraph. The query,
captured responses and replayable join evidence for the current corpus are in
[`docs/okn/evidence/2026-11-16-current-corpus`](https://github.com/ActiveInferenceInstitute/cognitive/tree/main/docs/okn/evidence/2026-11-16-current-corpus).
The join demonstrates identifier-based discovery while preserving the stated
mapping predicates. The reusable capture and submission methods are maintained
in `docxology/daf-okn`.

Entity IRIs are under `https://purl.org/okn/frink/kg/cognitive-kb/`; the named graph is
`https://purl.org/okn/frink/kg/cognitive-kb`. A prose description, vocabulary mapping, sample
and counts are in the source repository: <https://github.com/ActiveInferenceInstitute/cognitive/tree/main/docs/okn>.
The exporter, `code/scripts/export_rdf.py`, is in the same repository.
