---
template: overrides/kg.html
shortname: cognitive-kb
title: Cognitive Active Inference knowledge base
description: Concept pages on Active Inference and related fields, with typed and untyped relations and citation records, as SKOS/Dublin Core/schema.org RDF.
stats: https://registry.okn.us/kg-stats/cognitive-kb
homepage: https://github.com/ActiveInferenceInstitute/cognitive
frink-options:
  lakefs-repo: cognitive-kb
  documentation-path: cognitive-kb
contacts:
  - email: daniel@activeinference.institute
    github: docxology
    label: "Daniel Ari Friedman"
---

The knowledge base of the Active Inference Institute's `cognitive` repository as RDF. Every
page is a `schema:CreativeWork`; articles on one idea are also `skos:Concept`s in one concept
scheme, grouped into `skos:Collection`s by domain (mathematics, biology, cognitive science,
philosophy, systems, ontology, citations). Edges are typed relations from each page's
`semantic_relations` (`skos:related`, `dcterms:isPartOf`, `dcterms:hasPart` or a term under
`https://purl.org/okn/frink/kg/cognitive-kb/relation/` that is a sub-property of
`skos:semanticRelation`) and untyped body links (`dcterms:references`). Citation pages carry
authors, year and DOI (`schema:sameAs`), and many concept pages link to the matching Wikidata item with `skos:closeMatch`. Provenance is `prov:wasDerivedFrom` the public
repository; repository-owned graph content is licensed under CC BY 4.0.
The graph serves public research and education by connecting explanatory concepts
and their literature across Active Inference, cognitive science, mathematics and
biology. Wikidata mappings are candidate correspondences requiring review before
using them as identity assertions. No external grant funding is claimed.

A cross-graph query follows the existing Wikidata mappings through the OKN
identifier-mappings graph to labeled OBO identifiers in Ubergraph. Captured live
responses, the query and replayable join evidence are in the source repository's
`docs/okn/evidence/2026-10-13/`. This demonstrates identifier-based discovery;
it does not promote candidate page mappings to identity assertions. The reusable
capture and submission methods are maintained in `docxology/daf-okn`.

Entity IRIs are under `https://purl.org/okn/frink/kg/cognitive-kb/`; the named graph is
`https://purl.org/okn/frink/kg/cognitive-kb`. A prose description, vocabulary mapping, sample
and counts are in the source repository: <https://github.com/ActiveInferenceInstitute/cognitive/tree/main/docs/okn>.
The exporter, `code/scripts/export_rdf.py`, is in the same repository.
