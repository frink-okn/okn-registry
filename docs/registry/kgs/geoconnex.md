---
template: overrides/kg.html
shortname: geoconnex
title: GEOCONNEX
description: Geoconnex is an open, community-driven knowledge graph linking U.S. hydrologic features to enable seamless water data discovery, access, and collaborative monitoring.
stats: https://registry.okn.us/kg-stats/geoconnex
homepage: https://docs.geoconnex.us/about/intro
funding: 
sparql: https://apps.okn.us/geoconnex/sparql
tpf: https://apps.okn.us/ldf/geoconnex
frink-options:
  lakefs-repo: geoconnex
  documentation-path: geoconnex
  kgf:
    semantics:
      prefixes:
        geoconnex: "https://geoconnex.us/"
        geoconnex-nqhash: "https://docs.geoconnex.us/nqhash/"
        iow-nqhash: "https://iow.io/nqhash/"
        ogc-crs: "http://www.opengis.net/def/crs/"
      roles:
        label:
          - "https://schema.org/name"
          - "http://gnis-ld.org/lod/gnis/ontology/officialName"
          - "https://schema.org/sname"
          - "https://schema.org/alternateName"
      authoritative_namespaces:
        - geoconnex
        - geoconnex-nqhash
contact:
  email: "apadilla@lincolninst.edu"
  github: "adplincinst"
  label: "Andrew Padilla"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
Geoconnex is an open, community-driven knowledge graph linking U.S. hydrologic features to enable seamless water data discovery, access, and collaborative monitoring.
