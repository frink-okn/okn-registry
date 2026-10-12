---
template: overrides/kg.html
shortname: kwg-environment
title: KnowWhereGraph Environment
description: Environmental observation layers from KnowWhereGraph, covering SSURGO soils, the USDA Cropland Data Layer, EPA air quality measurements, and NOAA climate division observations for the United States.
stats: https://registry.okn.us/kg-stats/kwg-environment
homepage: https://knowwheregraph.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2033521
tpf: https://apps.okn.us/kgf/kwg-environment/latest/tpf
kgf: https://apps.okn.us/kgf/kwg-environment
frink-options:
  lakefs-repo: kwg-environment
  documentation-path: kwg-environment
  kgf:
    semantics:
      prefixes:
        unit: "https://qudt.org/vocab/unit/"
        fibo-fnd-plc-adr: "https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/"
        fibo-fnd-plc-loc: "https://spec.edmcouncil.org/fibo/ontology/FND/Places/Locations/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
contacts:
  - email: shirlystephen@ucsb.edu
    github: "shirlysteph"
    label: "Shirly Stephen"
  - email: cogan.shimizu@wright.edu
    github: "cogan-shimizu"
    label: "Cogan Shimizu"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
KnowWhereGraph Environment is one of four graphs that republish [KnowWhereGraph](https://knowwheregraph.org/) (KWG) version 4, the "Santa Barbara" release, from a November 2024 snapshot. It holds the soil, land cover, air quality, and climate layers, and is the largest of the four; the companion graphs are [kwg-places](kwg-places.md), [kwg-hazards](kwg-hazards.md), and [kwg-society](kwg-society.md).

Contents, with the coverage KWG documents for each source:

* USDA Soil Survey Geographic Database (SSURGO): soil map units with their polygon geometries, soil types, and soil properties
* USDA Cropland Data Layer (CropScape): crop and land cover types observed per level 13 S2 cell per year, from 2008
* EPA Air Quality System: monitoring sites, with addresses, and daily summaries for lead, CO, ozone, PM2.5, NO2, SO2, and PM10, from 1980
* NOAA climate divisions for the contiguous US and their observations (temperature, precipitation, drought severity indices, heating and cooling degree days), from 1895, with QUDT units
* Shared `time:Instant` entities for years and dates

Observations follow SOSA (features of interest, observable properties, observations, and results) and OWL-Time. Features are located with KWG's spatial relations (`kwg-ont:sfWithin`, `kwg-ont:sfContains`, `kwg-ont:sfOverlaps`) to [S2 cells](http://s2geometry.io/) and to administrative regions, asserted in both directions. Cropland is the largest layer by statement count, and air quality the second; soil is dominated by its geometries.

Resource IRIs are under `http://stko-kwg.geog.ucsb.edu/lod/resource/`. Administrative regions and other places are referenced by IRI and described in [kwg-places](kwg-places.md). S2 cells appear only through their relations to features and observations; their own types, labels, and geometries are not included. The SAWGraph [spatialkg](spatialkg.md) graph uses the same S2 cell IRIs.

Each KWG source subgraph is kept as a named graph, `http://stko-kwg.geog.ucsb.edu/lod/resource/subgraph.<name>` (for example `subgraph.air-quality-epa`). The KWG ontology modules for these layers and the vocabularies they reuse (SOSA, OWL-Time, GeoSPARQL, QUDT, FIBO addresses and locations) are included, each in a named graph named by its ontology IRI.

KnowWhereGraph's own contribution is released under CC0. The underlying sources keep their own terms, which should be checked with each provider.
