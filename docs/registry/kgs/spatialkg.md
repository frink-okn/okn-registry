---
template: overrides/kg.html
shortname: spatialkg
title: SAWGraph Spatial KG
description: The SAWGraph Spatial KG is part of the Safe Agricultural Products and Water Graph (SAWGraph) project. It contains all the Level 13 grid cells from the S2 grid as well as administrative regions of levels 1 to 3 (states, counties, and county subdivisions) and the spatial relationships between them for the 48 contiguous states in the U.S.
homepage: https://sawgraph.github.io/
stats: https://frink.renci.org/kg-stats/spatial-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333782
sparql: https://frink.apps.renci.org/spatialkg/sparql
tpf: https://frink.apps.renci.org/ldf/spatialkg
frink-options:
  lakefs-repo: spatial-kg
  documentation-path: spatial-kg
contact:
  - email: david.kedrowski@maine.edu 
    github: "dkedrowski"
    label: "David Kedrowski"
  - email: "torsten.hahmann@maine.edu"
    github: "thahmann"
    label: "Torsten Hahmann"
---
The SAWGraph Spatial KG is a large-scale geospatial knowledge graph developed by the SAWGraph project (funded by NSF award #2333782) for researchers and practitioners working with place-based data and spatial analytics. It supports spatial reasoning, place-based linkage, and geographic data integration.
The graph covers the entire 48 contiguous states in the U.S. and contains 756.9 million triples describing 16.8 million spatial entities, including 7.4 million S2 cells (Level 13 discretization) and hierarchical administrative regions across three levels: Level 1 (102 states), Level 2 (6,228 counties), Level 3 (35,458 county subdivisions such as towns and townships). The administrative entities are hierarchically linked as well as spatially integrated with the Level 13 S2 cells using the spatial:connectedTo relation. The knowledge graph leverages the KWG ontology and implements OGC GeoSPARQL standards for interoperability with other geospatial datasets. 
