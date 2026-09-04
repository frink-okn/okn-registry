---
template: overrides/kg.html
shortname: spoke-okn
title: SPOKE-OKN
description: The spoke-okn (SPOKE Open Knowledge Network) KG is a comprehensive biomedical and environmental health knowledge graph that integrates diverse data across genomics, environmental science, and public health.
stats: https://registry.okn.us/kg-stats/spoke-okn
homepage: https://spoke.ucsf.edu
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333819
sparql: https://apps.okn.us/spoke-okn/sparql
tpf: https://apps.okn.us/ldf/spoke-okn
frink-options:
  lakefs-repo: spoke-kg
  documentation-path: spoke-kg
  neo4j-conversion-config-path: https://raw.githubusercontent.com/frink-okn/okn-registry/refs/heads/main/docs/registry/neo4j-conf/spoke-okn.yaml
  kgf:
    semantics:
      prefixes:
        spoke-okn: "https://purl.org/okn/frink/kg/spoke-okn/schema/"
        spoke-okn-rel: "https://purl.org/okn/frink/kg/spoke-okn/relationship/"
        spoke-okn-location: "https://purl.org/okn/frink/kg/spoke-okn/location/"
        spoke-okn-organism: "https://purl.org/okn/frink/kg/spoke-okn/organism/"
        spoke-okn-sdoh: "https://purl.org/okn/frink/kg/spoke-okn/sdoh/"
        pubchem-inchikey: "http://rdf.ncbi.nlm.nih.gov/pubchem/inchikey/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "https://purl.org/okn/frink/kg/spoke-okn/schema/location_name"
          - "https://purl.org/okn/frink/kg/spoke-okn/schema/state_name"
          - "https://purl.org/okn/frink/kg/spoke-okn/schema/host_name"
      authoritative_namespaces:
        - spoke-okn
        - spoke-okn-rel
        - spoke-okn-location
        - spoke-okn-organism
        - spoke-okn-sdoh
contact:
  email: sergio.baranzini@ucsf.edu
  github: "baranzini-lab"
  label: "Sergio Baranzini"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---

The spoke-okn (SPOKE Open Knowledge Network) KG is a comprehensive biomedical and environmental health knowledge graph that integrates diverse data across genomics, environmental science, and public health. It encompasses multiple primary entity types, including organisms, geographic locations (from countries to ZIP codes), genes, diseases, chemical compounds, social determinants of health, and environmental contexts. With detailed hierarchical coverage of geographic information, spoke-okn supports spatial analyses of health outcomes, environmental exposures, and socioeconomic factors across a range of geographic scales.
