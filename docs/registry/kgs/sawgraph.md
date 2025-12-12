---
template: overrides/kg.html
shortname: sawgraph
title: SAWGraph PFAS graph 
description: The Safe Agricultural Products and Water Graph (SAWGraph) PFAS graph stores data on PFAS observations and releases, describing the samples, the geospatial features they were taken from, the sampled environmental media, the specific chemical substances and the measurement values observed.
stats: https://frink.renci.org/kg-stats/sawgraph
homepage: https://sawgraph.github.io/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333782
sparql: https://frink.apps.renci.org/sawgraph/sparql
tpf: https://frink.apps.renci.org/ldf/sawgraph
frink-options:
  lakefs-repo: sawgraph-kg
  documentation-path: sawgraph-kg
contact:
  - email: katrina.schweikert@maine.edu	  
    github: "kschweikert"
    label: "Katrina Schweikert"
  - email: "torsten.hahmann@maine.edu"
    github: "thahmann"
    label: "Torsten Hahmann"
  
---
The Safe Agricultural Products and Water Graph (SAWGraph) is an open knowledge network designed for environmental health researchers, regulatory agencies, and public health officials to help track and monitor per- and polyfluoroalkyl substances (PFAS) and other contaminants in food and water systems. 
The SAWGraph PFAS graph employs the ContaminOSO ontology (coso:) for standardized contamination modeling to encode the sampled features (e.g. wells, water bodies, facilities, fields), environmental media (e.g. groundwater, surface water, waste water, soil, animal or plant tissue), sample locations (Level 13 S2 cells and Level 3 administrative regions), sample type classification (based on FOODON categories like meat, dairy, produce, and seafood and NCBITaxon organisms), and tested chemical (DSSTox Substance IDs (DTXSID) and CAS numbers). Observations include measurement values, detection limits, lab qualifiers, and validation levels. Currently, the graph includes data from the national WaterQualityPortal (WQP) dataset and select state datasets, in particular from Maine's EGAD drinking water monitoring program.

