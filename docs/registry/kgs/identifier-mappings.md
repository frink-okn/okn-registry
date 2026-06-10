---
template: overrides/kg.html
shortname: identifier-mappings
title: ID Mappings
description: Mappings using standard RDF predicates between Wikidata entities and external identifiers represented as RDF IRIs
frink-options:
  lakefs-repo: identifier-mappings
  documentation-path: "identifier-mappings"
stats: https://registry.okn.us/kg-stats/identifier-mappings
homepage: https://www.wikidata.org/
sparql: https://apps.okn.us/identifier-mappings/sparql
tpf: https://apps.okn.us/ldf/identifier-mappings
contact: 
  email: morshedm@renci.org
  github: "mahir256"
  label: "Mahir Morshed"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
This graph is a subset of the Wikidata graph, consisting of mappings between Wikidata entities, mostly items, and external identifiers on those entities. They have been produced through taking existing triples from the Wikidata RDF dump representing those mappings and converting their custom predicates to standard predicates such as "skos:exactMatch". This mapping graph is provided by okn.us.
