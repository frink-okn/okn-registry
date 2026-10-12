---
template: overrides/kg.html
shortname: kwg-society
title: KnowWhereGraph Society
description: Demographic and public health layers from KnowWhereGraph, covering US Census statistical areas, county-level public health indicators, hospitals, public health departments, and federally qualified health centers.
stats: https://registry.okn.us/kg-stats/kwg-society
homepage: https://knowwheregraph.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2033521
# sparql: https://apps.okn.us/kwg-society/sparql
# tpf: https://apps.okn.us/ldf/kwg-society
frink-options:
  lakefs-repo: kwg-society
  documentation-path: kwg-society
  kgf:
    semantics:
      prefixes:
        eo: "http://knowwheregraph/ontology/expertise-ontology/"
        org: "http://www.w3.org/ns/org#"
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
KnowWhereGraph Society is one of four graphs that republish [KnowWhereGraph](https://knowwheregraph.org/) (KWG) version 4, the "Santa Barbara" release, from a November 2024 snapshot. It holds the demographic and public health layers, and is the smallest of the four; the companion graphs are [kwg-places](kwg-places.md), [kwg-hazards](kwg-hazards.md), and [kwg-environment](kwg-environment.md).

Contents:

* KWG's US Census Bureau layer (sourced from American Community Survey 5-year data): metropolitan and micropolitan statistical areas and their relations to counties and S2 cells
* KWG's integrated public health layer, 2020 to 2024: County Health Rankings, CDC PLACES measures (such as diabetes, obesity, and poverty), the CDC Social Vulnerability Index, hospitals from the Homeland Infrastructure Foundation-Level Data, and public health departments
* HRSA federally qualified health center sites, with addresses, patient totals, specialties, and staffing
* Shared `time:Instant` entities for years and dates

Indicators are modeled as SOSA observations on counties and other regions. Facilities (hospitals, health departments, and health center sites) are described with the W3C Organization ontology and FIBO addresses, and are located with KWG's spatial relations (`kwg-ont:sfWithin`, `kwg-ont:sfContains`) to level 13 [S2 cells](http://s2geometry.io/) and to counties, asserted in both directions.

Resource IRIs are under `http://stko-kwg.geog.ucsb.edu/lod/resource/`. Counties are referenced as `administrativeRegion.USA.<FIPS code>` and described in [kwg-places](kwg-places.md). S2 cells appear only through their relations to regions and facilities; their own types, labels, and geometries are not included. The SAWGraph [spatialkg](spatialkg.md) graph uses the same county and S2 cell IRIs.

Each KWG source subgraph is kept as a named graph, `http://stko-kwg.geog.ucsb.edu/lod/resource/subgraph.<name>` (for example `subgraph.public-health`). The KWG ontology modules for these layers and the vocabularies they reuse (SOSA, OWL-Time, GeoSPARQL, W3C Organization, PROV-O, FIBO addresses and locations) are included, each in a named graph named by its ontology IRI.

KnowWhereGraph's own contribution is released under CC0. The underlying sources keep their own terms, which should be checked with each provider.
