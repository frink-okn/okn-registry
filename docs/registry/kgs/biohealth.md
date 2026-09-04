---
template: overrides/kg.html
shortname: biohealth
title: Bio-Health KG
description: Bio-Health KG is a dynamically-updated open knowledge network for health, integrating biomedical insights with social determinants of health.
# homepage: 
stats: https://registry.okn.us/kg-stats/biobricks-ice-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333740
sparql: https://apps.okn.us/biohealth/sparql
tpf: https://apps.okn.us/ldf/biohealth
frink-options:
  lakefs-repo: biohealth
  documentation-path: "biohealth"
  neo4j-conversion-config-path: https://raw.githubusercontent.com/frink-okn/okn-registry/refs/heads/main/docs/registry/neo4j-conf/biohealth.yaml
  kgf:
    semantics:
      prefixes:
        biohealth: "https://biohealthkg.proto-okn.net/kg/schema/"
        biohealth-node: "https://biohealthkg.proto-okn.net/kg/node/"
        biohealth-rel: "https://biohealthkg.proto-okn.net/kg/relationship/"
        biohealth-semtype: "https://biohealthkg.proto-okn.net/kg/semtype/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - biohealth
        - biohealth-node
        - biohealth-rel
        - biohealth-semtype
contact:
  email: aidong@virginia.edu
  label: "Aidong Zhang"
  github: ""
---
Bio-Health KG is a dynamically-updated open knowledge network for health: integrating biomedical insights with social determinants of health.

Bio-Health KG is a comprehensive health knowledge graph developed by the University of Virginia under NSF funding (Award #2333740) that integrates biomedical facts with Social Determinants of Health (SDoH) data to address healthcare disparities. The graph contains over 110 million triples representing 250,976 biomedical entities interconnected through 18.3 million biomedical relationships. It continuously updates from streams of scientific literature (primarily PubMed) and Electronic Health Records (including MIMIC clinical data), enabling real-time integration of emerging research findings. Core semantic relationships leverage the Biolink vocabulary with predicates including location_of, affects, treats, coexists_with, and causes, while custom schema extensions capture clinical processes and measurements. The knowledge graph employs reified statements (RDF reification) for comprehensive provenance tracking. The project aims to uncover associations between social determinants and health outcomes to improve healthcare equity. 
