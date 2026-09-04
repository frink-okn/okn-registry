---
template: overrides/kg.html
shortname: ubergraph
title: Ubergraph
description: Integrated suite of OBO ontologies with precomputed inferred relationships
#stats:
homepage: https://github.com/INCATools/ubergraph/
sparql: https://apps.okn.us/ubergraph/sparql
tpf: https://apps.okn.us/ldf/ubergraph
frink-options:
  lakefs-repo: ubergraph
  documentation-path: ubergraph
  kgf:
    semantics:
      prefixes:
        bican: "https://purl.brain-bican.org/taxonomy/"
        bican-ccn: "https://purl.brain-bican.org/taxonomy/CCN20230722#"
        jcvi-nsf2: "http://www.jcvi.org/framework/nsf2_full_mtg#"
        n2o: "http://n2o.neo/custom/"
        chemrof: "https://w3id.org/chemrof/"
        ubergraph-axioms: "http://translator.renci.org/ubergraph-axioms.ofn#"
        reasoner: "http://reasoner.renci.org/vocab/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "http://www.w3.org/2004/02/skos/core#prefLabel"
          - "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym"
      authoritative_namespaces:
        - ubergraph-axioms
        - reasoner
contact:
  email: balhoff@renci.org  
  github: balhoff
  label: Jim Balhoff
---
[Ubergraph](https://github.com/INCATools/ubergraph) is an RDF triplestore which provides a SPARQL query endpoint to an integrated suite of OBO ontologies, and includes precomputed inferred edges which allow logically complete queries over those ontologies for a subset of OWL. This Proto-OKN copy of the Ubergraph triplestore is provided by okn.us.
