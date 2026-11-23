# FRINK geo / administrative feature-class inventory

Every instantiated geographic or administrative feature **class IRI** in the 14-graph FRINK federation, grouped by the real-world **concept** it denotes and the broader **feature family**. Under each class IRI, one line per **knowledge graph** that instantiates it, with the graph's **instance count** and the **instance-IRI template** its members follow.

> **IRIs are shown in full, including scheme.** `http://` and `https://` forms of the "same" vocabulary term are listed as **separate class IRIs**, because they are distinct RDF resources: an instance typed `http://schema.org/Place` will not join to one typed `https://schema.org/Place` without an explicit `owl:sameAs` or a normalization rule.

**Interoperability tier** (of the class's *instance*-IRI scheme):

- 🔵 **SHARED** — the same instance-IRI scheme is minted by ≥2 graphs (real cross-graph join key)
- 🟠 **SHAREABLE** — a governed / reference scheme (e.g. `https://geoconnex.us/…`, `https://datacommons.org/…`) currently used by one graph but designed for reuse
- 🟤 **SILOED** — a project-local scheme, not designed for reuse

`×N` on a class = *N* co-typed sibling subtype classes in that graph folded onto one shared instance template (e.g. the 51 USGS NWIS monitoring-location site-types).

---

**Scope:** 65 class-IRI nodes · 152 class partitions folded · 19 concepts · 6 families · 13 class IRIs shared across ≥2 graphs.

## Administrative hierarchy

### Country (ADM0)  ·  2 graphs, 2 class IRIs

- **`http://asu.edu/semantics/SUDOKN/Country`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **128** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion_0`** — 🔵 SHARED  ·  1 graph
    - `sockg` — **2** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`

### State (ADM1)  ·  7 graphs, 5 class IRIs

- **`http://asu.edu/semantics/SUDOKN/State`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **938** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion_1`** — 🔵 SHARED  ·  5 graphs
    - `spatialkg` — **102** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `hydrologykg` — **50** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sockg` — **36** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `fiokg` — **1** instance — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **1** instance — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`http://gnis-ld.org/lod/gnis/ontology/State`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **56** instances — `https://geoconnex.us/ref/states/{id}`
- **`https://schema.org/State`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **56** instances — `https://geoconnex.us/ref/states/{id}`
- **`http://w3id.org/fio/v1/epa-frs#Agency.State`** — 🟤 SILOED  ·  1 graph
    - `fiokg` — **3** instances — `http://w3id.org/fio/v1/epa-frs-data#{id}`

### County (ADM2)  ·  6 graphs, 2 class IRIs

- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion_2`** — 🔵 SHARED  ·  5 graphs
    - `spatialkg` — **6.2 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `hydrologykg` — **3.1 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `fiokg` — **102** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sockg` — **62** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **16** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`http://gnis-ld.org/lod/gnis/ontology/County`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **3.2 k** instances — `https://geoconnex.us/ref/counties/{id}`

### County subdivision (ADM3)  ·  4 graphs, 1 class IRI

- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion_3`** — 🔵 SHARED  ·  4 graphs
    - `hydrologykg` — **35.5 k** instances — `https://datacommons.org/browser/geoId/{id}`
    - `spatialkg` — **35.5 k** instances — `https://datacommons.org/browser/geoId/{id}`
    - `fiokg` — **1.7 k** instances — `https://datacommons.org/browser/geoId/{id}`
    - `sawgraph` — **529** instances — `https://datacommons.org/browser/geoId/{id}`

### Census statistical unit  ·  1 graph, 1 class IRI

- **`https://metadata.phila.gov/CensusTract`** — 🟤 SILOED  ·  1 graph
    - `nikg` — **361** instances — `https://metadata.phila.gov/{id}`

### Administrative area (other)  ·  6 graphs, 4 class IRIs

- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/Region`** — 🔵 SHARED  ·  3 graphs
    - `spatialkg` — **7.45 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `hydrologykg` — **7.44 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **86.9 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`https://schema.org/AdministrativeArea`** — 🟠 SHAREABLE  ·  2 graphs
    - `spoke-okn` — **113.9 k** instances — `https://purl.org/okn/frink/kg/spoke-okn/location/{id}`
    - `geoconnex` — **3.3 k** instances — `https://geoconnex.us/ref/counties/{id}`
- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/AdministrativeRegion`** — 🔵 SHARED  ·  3 graphs
    - `spatialkg` — **41.8 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `hydrologykg` — **38.6 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **546** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`http://sail.ua.edu/ruralkg/settlementtype/CountyStatus`** — 🟤 SILOED  ·  1 graph
    - `ruralkg` — **3.2 k** instances — `http://sail.ua.edu/ruralkg/settlementtype/{id}`

## Populated places

### City / populated place  ·  6 graphs, 7 class IRIs

- **`https://schema.org/Place`** — 🟠 SHAREABLE  ·  3 graphs
    - `ufokn` — **5.84 M** instances — `https://ufokn.org/id/urmi/{id}`
    - `geoconnex` — **2.96 M** instances — `https://api.wwdh.internetofwater.app/collections/awdb-forecasts-edr/items/{id}`
    - `sudokn` — **56.2 k** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://asu.edu/semantics/SUDOKN/GeospatialLocation`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **56.2 k** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://asu.edu/semantics/SUDOKN/City`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **10.3 k** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://schema.org/Place`** — 🟤 SILOED  ·  1 graph
    - `dreamkg` — **1.0 k** instances — `dreamkg:/service/location/{id}`
- **`https://idir.uta.edu/sockg-ontology#WaterQualityArea`** — 🟤 SILOED  ·  1 graph
    - `sockg` — **681** instances — `https://idir.uta.edu/sockg-ontology/individuals/{id}`
- **`http://release.niem.gov/niem/niem-core/5.0/#Location`** — 🔵 SHARED  ·  1 graph
    - `scales` — **536** instances — `https://datacommons.org/browser/geoId/{id}`
- **`https://idir.uta.edu/sockg-ontology#WindErosionArea`** — 🟤 SILOED  ·  1 graph
    - `sockg` — **34** instances — `https://idir.uta.edu/sockg-ontology/individuals/{id}`

## Grid / DGG cells

### Grid / DGG cell  ·  5 graphs, 4 class IRIs

- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/S2Cell_Level13`** — 🔵 SHARED  ·  4 graphs
    - `hydrologykg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `spatialkg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **86.3 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sockg` — **1.1 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/Cell`** — 🔵 SHARED  ·  3 graphs
    - `hydrologykg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `spatialkg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **86.3 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`http://stko-kwg.geog.ucsb.edu/lod/ontology/S2Cell`** — 🔵 SHARED  ·  3 graphs
    - `hydrologykg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `spatialkg` — **7.40 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **86.3 k** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
- **`https://stko-kwg.geog.ucsb.edu/lod/ontology#S2Cell`** — 🟤 SILOED  ·  1 graph
    - `ufokn` — **11.72 M** instances — `bn1970324`

## Water & hydrology

### Flow path / river  ·  2 graphs, 2 class IRIs

- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_FlowPath`** — 🟠 SHAREABLE  ·  2 graphs
    - `hydrologykg` — **434.5 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`
    - `geoconnex` — **34.1 k** instances — `https://geoconnex.us/ref/mainstems/{id}`
- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_ElementaryFlowPath`** — 🟠 SHAREABLE  ·  1 graph
    - `hydrologykg` — **434.5 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`

### Lake  ·  1 graph, 1 class IRI

- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_Lake`** — 🟠 SHAREABLE  ·  1 graph
    - `hydrologykg` — **60.1 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`

### Aquifer  ·  1 graph, 1 class IRI

- **`http://gwml2.org/def/gwml2#GW_Aquifer`** — 🟤 SILOED  ·  1 graph
    - `hydrologykg` — **8.4 k** instances — `http://sawgraph.spatialai.org/v1/il_isgs_data#{id}`

### Watershed / catchment  ·  1 graph, 1 class IRI

- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_CatchmentRealization`** — 🟠 SHAREABLE  ·  1 graph
    - `hydrologykg` — **434.5 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`

### Hydrologic feature / location  ·  2 graphs, 6 class IRIs

- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_HydroLocation`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **2.42 M** instances — `https://api.wwdh.internetofwater.app/collections/awdb-forecasts-edr/items/{id}`
- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_HydrometricFeature`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **2.41 M** instances — `https://geoconnex.us/iow/demo/{id}`
- **`https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroLocation`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **155.5 k** instances — `https://api.wwdh.internetofwater.app/collections/awdb-forecasts-edr/items/{id}`
- **`https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydrometricFeature`** — 🔵 SHARED  ·  1 graph
    - `geoconnex` — **154.7 k** instances — `https://geoconnex.us/iow/wqp/{id}`
- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_WaterBody`** — 🟠 SHAREABLE  ·  2 graphs
    - `hydrologykg` — **73.0 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`
    - `geoconnex` — **34.1 k** instances — `https://geoconnex.us/ref/mainstems/{id}`
- **`https://www.opengis.net/def/schema/hy_features/hyf/HY_HydroFeature`** — 🟠 SHAREABLE  ·  1 graph
    - `hydrologykg` — **73.0 k** instances — `https://geoconnex.us/nhdplusv2/comid/{id}`

## Sites, facilities & samples

### Monitoring / observation site  ·  2 graphs, 3 class IRIs

- **`https://api.waterdata.usgs.gov/ogcapi/v0/collections/site-types/items/GW`** ×51 — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **1.73 M** instances (×51 subtypes) — `https://geoconnex.us/usgs/monitoring-location/{id}`
- **`http://sawgraph.spatialai.org/v1/il-isgs#ISGS-Well`** — 🟤 SILOED  ·  1 graph
    - `hydrologykg` — **379.5 k** instances — `http://sawgraph.spatialai.org/v1/il-isgs-data#{id}`
- **`http://sawgraph.spatialai.org/v1/me-mgs#MGS-Well`** — 🟤 SILOED  ·  1 graph
    - `hydrologykg` — **153.3 k** instances — `http://sawgraph.spatialai.org/v1/me-mgs-data#{id}`

### Site / sampled feature  ·  3 graphs, 8 class IRIs

- **`http://www.w3.org/ns/sosa/FeatureOfInterest`** ×3 — 🔵 SHARED  ·  1 graph
    - `sawgraph` — **54.9 k** instances (×3 subtypes) — `http://geoconnex.us/ref/pws/{id}`
- **`http://w3id.org/coso/v1/contaminoso#SamplePoint`** ×7 — 🟤 SILOED  ·  1 graph
    - `sawgraph` — **38.2 k** instances (×7 subtypes) — `http://w3id.org/sawgraph/v1/me-egad-data#{id}`
- **`https://idir.uta.edu/sockg-ontology#SoilBiologicalSample`** — 🟤 SILOED  ·  1 graph
    - `sockg` — **18.3 k** instances — `https://idir.uta.edu/sockg-ontology/individuals/{id}`
- **`http://w3id.org/coso/v1/contaminoso#SampledFeature`** — 🟠 SHAREABLE  ·  1 graph
    - `sawgraph` — **10.9 k** instances — `http://w3id.org/hyfo/wbd/v1/wbd-data#{id}`
- **`http://w3id.org/sawgraph/v1/us-wqp#Site`** — 🔵 SHARED  ·  1 graph
    - `sawgraph` — **2.5 k** instances — `https://geoconnex.us/iow/wqp/{id}`
- **`http://asu.edu/semantics/SUDOKN/GeospatialSite`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **227** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://w3id.org/sawgraph/v1/us-wqp#Project`** ×3 — 🟤 SILOED  ·  1 graph
    - `sawgraph` — **125** instances (×3 subtypes) — `http://w3id.org/sawgraph/v1/us-wqp-data#{id}`
- **`https://idir.uta.edu/sockg-ontology#Site`** — 🟤 SILOED  ·  1 graph
    - `sockg` — **60** instances — `https://idir.uta.edu/sockg-ontology/individuals/{id}`

### Environmental sample  ·  1 graph, 3 class IRIs

- **`http://www.w3.org/ns/sosa/Sample`** ×20 — 🟤 SILOED  ·  1 graph
    - `sawgraph` — **193.0 k** instances (×20 subtypes) — `http://w3id.org/sawgraph/v1/me-egad-data#{id}`
- **`http://w3id.org/sawgraph/v1/us-wqp#Sample`** ×5 — 🟤 SILOED  ·  1 graph
    - `sawgraph` — **14.0 k** instances (×5 subtypes) — `http://w3id.org/sawgraph/v1/us-wqp-data#{id}`
- **`http://w3id.org/sawgraph/v1/us-wqp#SampledFeature`** — 🟠 SHAREABLE  ·  1 graph
    - `sawgraph` — **2.8 k** instances — `http://w3id.org/hyfo/wbd/v1/wbd-data#{id}`

### Facility  ·  2 graphs, 2 class IRIs

- **`http://w3id.org/fio/v1/epa-frs#FRS-Facility`** ×3 — 🟤 SILOED  ·  1 graph
    - `fiokg` — **10.01 M** instances (×3 subtypes) — `http://w3id.org/fio/v1/epa-frs-data#{id}`
- **`http://release.niem.gov/niem/domains/jxdm/7.2/#Court`** — 🟤 SILOED  ·  1 graph
    - `scales` — **94** instances — `http://schemas.scales-okn.org/rdf/scales#{id}`

## Generic place / feature

### Generic place / feature  ·  10 graphs, 10 class IRIs

- **`http://www.opengis.net/ont/geosparql#Feature`** — 🔵 SHARED  ·  4 graphs
    - `hydrologykg` — **8.49 M** instances — `http://geoconnex.us/ref/pws/{id}`
    - `spatialkg` — **7.45 M** instances — `http://stko-kwg.geog.ucsb.edu/lod/resource/{id}`
    - `sawgraph` — **111.6 k** instances — `http://geoconnex.us/ref/pws/{id}`
    - `sudokn` — **56.2 k** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`http://gnis-ld.org/lod/gnis/ontology/Feature`** — 🟠 SHAREABLE  ·  1 graph
    - `geoconnex` — **969.0 k** instances — `https://geoconnex.us/usgs/gnis/{id}`
- **`http://w3id.org/coso/v1/contaminoso#Feature`** — 🔵 SHARED  ·  1 graph
    - `sawgraph` — **13.9 k** instances — `http://geoconnex.us/ref/pws/{id}`
- **`https://metadata.phila.gov/Location`** — 🟤 SILOED  ·  1 graph
    - `nikg` — **9.1 k** instances — `https://metadata.phila.gov/{id}`
- **`https://wildlife.proto-okn.net/kg/Location`** — 🟤 SILOED  ·  1 graph
    - `wildlifekn` — **657** instances — `https://wildlife.proto-okn.net/kg/{id}`
- **`http://release.niem.gov/niem/niem-core/5.0/#RelativeLocationReferencePoint`** — 🔵 SHARED  ·  1 graph
    - `scales` — **536** instances — `https://datacommons.org/browser/geoId/{id}`
- **`https://spec.industrialontologies.org/ontology/supplychain/SupplyChain/GeospatialLocation`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **225** instances — `http://asu.edu/semantics/SUDOKN/{id}`
- **`https://idir.uta.edu/sockg-ontology#Location`** — 🟤 SILOED  ·  1 graph
    - `sockg` — **58** instances — `https://idir.uta.edu/sockg-ontology/individuals/{id}`
- **`http://w3id.org/sawgraph/v1/us-wqp#DefWQPSurfaceWaterFeatureType`** ×3 — 🟤 SILOED  ·  1 graph
    - `sawgraph` — **20** instances (×3 subtypes) — `http://w3id.org/sawgraph/v1/us-wqp-data#{id}`
- **`https://w3id.org/biolink/vocab/EnvironmentalFeature`** — 🟠 SHAREABLE  ·  1 graph
    - `spoke-okn` — **2** instances — `http://purl.obolibrary.org/obo/{id}`

### Other geographic feature  ·  2 graphs, 2 class IRIs

- **`http://sail.ua.edu/ruralkg/settlementtype/RUCC`** — 🟤 SILOED  ·  1 graph
    - `ruralkg` — **10** instances — `http://sail.ua.edu/ruralkg/settlementtype/{id}`
- **`http://asu.edu/semantics/SUDOKN/HUBZone`** — 🟤 SILOED  ·  1 graph
    - `sudokn` — **1** instance — `http://asu.edu/semantics/SUDOKN/{id}`
