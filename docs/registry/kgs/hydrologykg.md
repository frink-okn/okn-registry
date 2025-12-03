---
template: overrides/kg.html
shortname: hydrologykg
title: SAWGraph Hydrology KG
description: The Hydrology KG is the part of the SAWGraph project that describes streams, waterbodies and wells and their locations.
stats: https://frink.renci.org/kg-stats/hydrology-kg
homepage: https://sawgraph.github.io/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333782
sparql: https://frink.apps.renci.org/hydrologykg/sparql
tpf: https://frink.apps.renci.org/ldf/hydrologykg
frink-options:
  lakefs-repo: hydrology-kg
  documentation-path: hydrology-kg
contact:
  - email: david.kedrowski@maine.edu  
    github: "dkedrowski"
    label: "David Kedrowski"
  - email: "torsten.hahmann@maine.edu"
    github: "thahmann"
    label: "Torsten Hahmann"
  
---
The SAWGraph Hydrology KG is part of the Safe Agricultural Products and Water Graph (SAWGraph) that facilities environmental regulators, water safety officials, and PFAS researchers to trace pollutant pathways, identify upstream contamination sources, assess downstream impacts from point sources, and determine which water wells are hydrologically connected to contaminated sites. 
The Hydrology knowledge graph integrates surface water features including stream reaches, watersheds and waterbodies (e.g. lakes), groundwater features like aquifers and wells, and hydrological connectivity data to support contaminant tracing and water quality analysis. It is built from USGS’s National Hydrography Dataset (NHDPlus) and state well and aquifer datasets. 
All features are spatially integrated with Level 13 S2 cells and Level 3 administrative regions using KnowWhereGraph topological relations and reuse of geoconnex URIs allows linking to additional details. 



