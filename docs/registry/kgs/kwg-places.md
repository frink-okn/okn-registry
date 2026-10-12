---
template: overrides/kg.html
shortname: kwg-places
title: KnowWhereGraph Places
description: Place and region identifiers from KnowWhereGraph (global administrative areas, US Census regions, ZIP code areas, weather forecast zones, judicial districts, GNIS features, and highways) with their relations to each other and to S2 cells.
stats: https://registry.okn.us/kg-stats/kwg-places
homepage: https://knowwheregraph.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2033521
tpf: https://apps.okn.us/kgf/kwg-places/latest/tpf
kgf: https://apps.okn.us/kgf/kwg-places
frink-options:
  lakefs-repo: kwg-places
  documentation-path: kwg-places
  kgf:
    semantics:
      prefixes:
        usgs: "http://gnis-ld.org/lod/usgs/ontology/"
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
KnowWhereGraph Places is one of four graphs that republish [KnowWhereGraph](https://knowwheregraph.org/) (KWG) version 4, the "Santa Barbara" release, from a November 2024 snapshot. It holds the place and region layers that the other KWG graphs refer to; the companion graphs are [kwg-hazards](kwg-hazards.md), [kwg-environment](kwg-environment.md), and [kwg-society](kwg-society.md).

Contents:

* Global Administrative Areas (GADM), levels 0 to 5, with geometries
* US Census Bureau regions (states, counties, and core-based statistical areas) and ZIP Code Tabulation Areas
* NOAA National Weather Service public forecast zones
* US federal judicial districts (Department of Justice)
* Geographic Names Information System features (GNIS-LD)
* The National Highway Planning Network (US Department of Transportation)
* `owl:sameAs` links from administrative regions to Wikidata
* Topological relations between the different kinds of region, for example climate divisions that overlap forecast zones

Regions are related to each other and to [S2 cells](http://s2geometry.io/) with KWG's spatial relations (`kwg-ont:sfWithin`, `kwg-ont:sfContains`, `kwg-ont:sfOverlaps`, `kwg-ont:sfTouches`), asserted in both directions. Most statements in this graph are relations between regions and level 13 S2 cells, so a question such as "which county, ZIP code area, or forecast zone contains this location" is a lookup rather than a geometry computation. Geometries are GeoSPARQL WKT literals; some country outlines are tens of megabytes.

Resource IRIs are under `http://stko-kwg.geog.ucsb.edu/lod/resource/`, for example `administrativeRegion.USA.23019` for Penobscot County, Maine. The SAWGraph graphs ([spatialkg](spatialkg.md), [sawgraph](sawgraph.md)) use the same administrative region and S2 cell IRIs, so they join with this graph directly. This graph describes S2 cells only through their relations to places; it does not include the cells' own types, labels, geometries, or parent and neighbor links.

Each KWG source subgraph is kept as a named graph, `http://stko-kwg.geog.ucsb.edu/lod/resource/subgraph.<name>` (for example `subgraph.admin-regions-gadm-new`). The KWG ontology and the vocabularies it reuses (SOSA, OWL-Time, GeoSPARQL, GNIS-LD, FOAF) are included, each in a named graph named by its ontology IRI.

KnowWhereGraph's own contribution is released under CC0. The underlying sources (GADM in particular) keep their own terms, which should be checked with each provider.
