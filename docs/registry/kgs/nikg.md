---
template: overrides/kg.html
shortname: nikg
title: Neighborhood Information KG
description: Neighborhood Information KG (NIKG) is a knowledge graph warehouse for neighborhood information.
stats: https://frink.renci.org/kg-stats/nikg
# homepage: 
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333790
sparql: https://frink.apps.renci.org/neighborhood-information-kg/sparql
tpf: https://frink.apps.renci.org/ldf/neighborhood-information-kg
frink-options:
  lakefs-repo: neighborhood-information-kg
  documentation-path: neighborhood-kg
contacts:
  - label: "Wentao Chen"
    email: wenc056@ucsd.edu
    github: "John-Steve-C"
  - label: "Jingbo Shang"
    email: jshang@ucsd.edu
    github: "shangjingbo1226"

---
Neighborhood Information KG (NIKG) is a knowledge graph warehouse for neighborhood information.

The Neighborhood Information Knowledge Graph (NIKG) is a knowledge graph warehouse designed for researchers, urban planners, and public health officials analyzing neighborhood-level data. It integrates incident records (particularly crime and safety events), census tract boundaries, and geospatial location data from Philadelphia and potentially other urban areas. The graph contains structured entities including Incidents with attributes such as officer involvement, fatality status, offender demographics (race, sex, age), and precise geospatial coordinates represented as WKT geometries via GeoSPARQL. NIKG links to standard geospatial vocabularies (OGC GeoSPARQL, sf:Point) and employs Philadelphia metadata schemas for domain-specific properties.

