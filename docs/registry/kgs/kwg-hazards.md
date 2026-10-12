---
template: overrides/kg.html
shortname: kwg-hazards
title: KnowWhereGraph Hazards
description: Natural hazard and disaster layers from KnowWhereGraph, covering storms, hurricanes, earthquakes, wildfires, smoke, drought, FEMA disaster declarations, and ReliefWeb reports, located by S2 cell and administrative region.
stats: https://registry.okn.us/kg-stats/kwg-hazards
homepage: https://knowwheregraph.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2033521
# sparql: https://apps.okn.us/kwg-hazards/sparql
# tpf: https://apps.okn.us/ldf/kwg-hazards
frink-options:
  lakefs-repo: kwg-hazards
  documentation-path: kwg-hazards
  kgf:
    semantics:
      prefixes:
        eo: "http://knowwheregraph/ontology/expertise-ontology/"
        dmdo: "http://knowwheregraph/ontology/dmdo#"
        undrr-hip: "https://knowwheregraph.org/undrr-hip/"
        org: "http://www.w3.org/ns/org#"
        fibo-fnd-arr-rep: "https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/"
        doid: "http://purl.obolibrary.org/obo/doid#"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "http://purl.org/dc/terms/title"
contacts:
  - email: shirlystephen@ucsb.edu
    github: "shirlysteph"
    label: "Shirly Stephen"
  - email: cogan.shimizu@wright.edu
    github: "cogan-shimizu"
    label: "Cogan Shimizu"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
KnowWhereGraph Hazards is one of four graphs that republish [KnowWhereGraph](https://knowwheregraph.org/) (KWG) version 4, the "Santa Barbara" release, from a November 2024 snapshot. It holds the hazard and disaster layers; the companion graphs are [kwg-places](kwg-places.md), [kwg-environment](kwg-environment.md), and [kwg-society](kwg-society.md).

Contents, with the coverage KWG documents for each source:

* NOAA Storm Events, US, from 1950
* NOAA historical hurricane tracks, with pressure and wind speed, from 1842
* USGS ANSS Comprehensive Earthquake Catalog, global, from 1843
* Monitoring Trends in Burn Severity (MTBS) burned area boundaries, US, 1984 to 2022
* National Interagency Fire Center wildland fire incident locations, with acres burned and estimated cost, from 2014
* NOAA smoke plume polygons, from 2005
* US Forest Service AirFire BlueSky smoke forecasts
* US Drought Monitor drought zones (National Drought Mitigation Center), weekly from 2000
* OpenFEMA disaster declarations, from 1953
* UN OCHA ReliefWeb reports, global
* A topic hierarchy (`eo:Topic`, with references to the Disease Ontology and other vocabularies) used to tag reports, with `owl:sameAs` links from disease topics to SPOKE Disease nodes
* Shared `time:Instant` entities for years and dates

Events and their observations follow SOSA and OWL-Time. Each event is located with KWG's spatial relations (`kwg-ont:sfWithin`, `kwg-ont:sfContains`, `kwg-ont:sfOverlaps`) to [S2 cells](http://s2geometry.io/) and to administrative regions, asserted in both directions. Most layers use level 13 cells; drought zones use level 10. KWG's hazard classes are mapped to the UNDRR-ISC hazard classification.

Resource IRIs are under `http://stko-kwg.geog.ucsb.edu/lod/resource/`. Administrative regions and other places are referenced by IRI and described in [kwg-places](kwg-places.md). S2 cells appear only through their relations to events; their own types, labels, and geometries are not included. The SAWGraph [spatialkg](spatialkg.md) graph uses the same S2 cell IRIs.

Each KWG source subgraph is kept as a named graph, `http://stko-kwg.geog.ucsb.edu/lod/resource/subgraph.<name>` (for example `subgraph.earthquake-usgs`). The KWG ontology modules for these layers and the vocabularies they reuse (SOSA, OWL-Time, GeoSPARQL, W3C Organization, UNDRR-ISC hazard classification) are included, each in a named graph named by its ontology IRI.

KnowWhereGraph's own contribution is released under CC0. The underlying sources keep their own terms, which should be checked with each provider.
