---
template: overrides/kg.html
shortname: wikidata
title: Wikidata
description: Wikidata is a free and open knowledge base that can be read and edited by both humans and machines
homepage: https://www.wikidata.org/
sparql: https://qlever.dev/api/wikidata
tpf: https://apps.okn.us/ldf/wikidata
frink-options:
  lakefs-repo: wikidata
  kgf:
    semantics:
      prefixes:
        schema: "http://schema.org/"
        wd: "http://www.wikidata.org/entity/"
        p: "http://www.wikidata.org/prop/"
        wdv: "http://www.wikidata.org/value/"
        wdref: "http://www.wikidata.org/reference/"
      authoritative_namespaces:
        - wd
        - p
        - wdv
        - wdref
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "http://www.w3.org/2004/02/skos/core#prefLabel"
        synonym:
          - "http://www.w3.org/2004/02/skos/core#altLabel"
    contents:
      text:
        untagged_language: none
contact: 
  email: balhoff@renci.org
  github: balhoff
  label: Jim Balhoff
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
[Wikidata](https://www.wikidata.org/) is a free and open knowledge base that can be read and edited by both humans and machines. The standalone SPARQL endpoint linked here is provided by the [Qlever project](https://qlever.dev/wikidata). A slightly out of date copy of the Wikidata graph is included in the merged SPARQL endpoint provided by [https://okn.us](https://okn.us). These two access methods will be reconciled in the near future.
