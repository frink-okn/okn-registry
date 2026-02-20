---
template: overrides/kg.html
shortname: ufokn
title: UF-OKN
description: The Urban Flooding Open Knowledge Network (UF-OKN) is an informational infrastructure built using knowledge graphs aiming to extract structured content from the information scattered across open-source geospatial datasets and hydrologic models.
stats: https://frink.renci.org/kg-stats/wen-kg
homepage: https://ufokn.com
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333726
sparql: https://frink.apps.renci.org/ufokn/sparql
tpf: https://frink.apps.renci.org/ldf/ufokn
frink-options:
  lakefs-repo: urban-flooding-open-knowledge-network
  documentation-path: ufokn-kg  
contact: 
  email: "yeghialt@ucmail.uc.edu"
  github: ""
  label: "Lilit Yeghiazarian"
---
UF-OKN is an informational infrastructure built using knowledge graphs aiming to extract structured content from the information scattered across open-source geospatial datasets and hydrologic models.

The Urban Flooding Open Knowledge Network (UF-OKN) is a geospatial knowledge graph infrastructure that integrates urban built environment data with real-time and historical hydrologic forecasts to enable flood risk assessment and emergency response. UF-OKN contains structured representations of urban infrastructure (buildings, roads, stormwater networks, power stations) derived from OpenStreetMap, linked to hydrologic features (rivers, streams) and operational forecast models including NOAA's National Water Model and local models like HEC-RAS and SWMM. The knowledge graph introduces "Risk-Points™"—locations where built and natural environments interact with potential flood impacts—providing 24-year historical analysis coverage across the continental United States. UF-OKN uses schema.org vocabularies (Place, GeoShape, GeoCoordinates, Observation, PropertyValue) and STKO spatial ontologies (S2Cell) to enable SPARQL queries connecting infrastructure vulnerability to forecast conditions. The knowledge graph supports developers building custom flood information applications, emergency management systems, and risk analysis tools for planning and real-time response.

