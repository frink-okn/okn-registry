---
template: overrides/kg.html
shortname: identifier-mappings
title: ID Mappings
description: Mappings using standard RDF predicates between Wikidata entities and external identifiers represented as RDF IRIs
frink-options:
  lakefs-repo: identifier-mappings
  documentation-path: "identifier-mappings"
#stats:
homepage: https://www.wikidata.org/
sparql: https://frink.apps.renci.org/identifier-mappings/sparql
tpf: https://frink.apps.renci.org/ldf/identifier-mappings
contact: 
  email: mmorshed@scripps.edu
  github: ""
  label: "Mahir Morshed"
---
This graph is a subset of the Wikidata graph, consisting of mappings between Wikidata entities, mostly items, and external identifiers on those entities. They have been produced through taking existing triples from the Wikidata RDF dump representing those mappings and converting their custom predicates to standard predicates such as "skos:exactMatch". This mapping graph is provided by the NSF [FRINK](https://frink.renci.org) project.
