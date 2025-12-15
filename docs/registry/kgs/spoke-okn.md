---
template: overrides/kg.html
shortname: spoke-okn
title: SPOKE-OKN
description: The spoke-okn (SPOKE Open Knowledge Network) KG is a comprehensive biomedical and environmental health knowledge graph that integrates diverse data across genomics, environmental science, and public health.
stats: https://frink.renci.org/kg-stats/spoke-okn
homepage: https://spoke.ucsf.edu
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333819
sparql: https://frink.apps.renci.org/spoke-okn/sparql
tpf: https://frink.apps.renci.org/ldf/spoke-okn
frink-options:
  lakefs-repo: spoke-kg
  documentation-path: spoke-kg
  neo4j-conversion-config-path: https://raw.githubusercontent.com/frink-okn/okn-registry/refs/heads/main/docs/registry/neo4j-conf/spoke-okn.yaml
contact:
  email: sergio.baranzini@ucsf.edu
  github: "baranzini-lab"
  label: "Sergio Baranzini"
---

The spoke-okn (SPOKE Open Knowledge Network) KG is a comprehensive biomedical and environmental health knowledge graph that integrates diverse data across genomics, environmental science, and public health. It encompasses multiple primary entity types, including organisms, geographic locations (from countries to ZIP codes), genes, diseases, chemical compounds, social determinants of health, and environmental contexts. With detailed hierarchical coverage of geographic information, spoke-okn supports spatial analyses of health outcomes, environmental exposures, and socioeconomic factors across a range of geographic scales.
