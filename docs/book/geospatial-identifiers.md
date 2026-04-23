# Geospatial identifier choice guidelines

References to locations occur across many graphs in the Proto-OKN, whether as areas that certain species abound in, as points where companies are headquartered, or as jurisdictions within which incidents take place. Regardless of the particular use case one has for locations, it is very important that they be referred to consistently across graphs.

## Entity classes

The particular recommendations listed here are intended to be consistent with existing [geospatial recommendations](https://docs.google.com/document/d/1wy8qXeMNTnT9PtxmMJHN2Ee-sih08LfXcqrvWsK2ZCQ/edit).
Each recommendation consists of at minimum an IRI format (in which the substring "$1" is replaced with a particular identifying string) and an example of an IRI using that format to refer to an entity.

Many of the entries below refer to KnowWhereGraph, which the Proto-OKN is in the process of incorporating sufficient geospatial components of.

Some of the entries below also refer to the Google Data Commons, but some general warnings about this data source:

* Do not use it for an entity that is also defined in KnowWhereGraph.
    * Example: use http://stko-kwg.geog.ucsb.edu/lod/resource/administrativeRegion.USA.23 to refer to Maine instead of https://datacommons.org/browser/geoId/23
* Do not use it if the IRI for it contains "wikidataId": use http://www.wikidata.org/entity/ as the prefix to the Wikidata ID used in that IRI instead.
    * Example: use http://www.wikidata.org/entity/Q203122 to refer to Whistler, British Columbia (if the need arises) instead of https://datacommons.org/place/wikidataId/Q203122
* Do not use a relationship type defined in Data Commons if it exists somewhere else.
    * Example: use http://stko-kwg.geog.ucsb.edu/lod/ontology/sfWithin to link places to the other places they're contained in instead of https://datacommons.org/browser/containedInPlace

### U.S. states

(KnowWhereGraph)

* IRI format: http://stko-kwg.geog.ucsb.edu/lod/resource/administrativeRegion.USA.$1
* Example: California = http://stko-kwg.geog.ucsb.edu/lod/resource/administrativeRegion.USA.06

### U.S. cities

(KnowWhereGraph/GNIS-LD)

* IRI format: http://gnis-ld.org/lod/gnis/feature/$1
* Example: Fontana = http://gnis-ld.org/lod/gnis/feature/2410517

### U.S. ZIP code regions

(KnowWhereGraph)

* IRI format: http://stko-kwg.geog.ucsb.edu/lod/resource/zipCodeArea.$1
* Example: 04419 = http://stko-kwg.geog.ucsb.edu/lod/resource/zipCodeArea.04419

### U.S. census tracts

(Data Commons)

* IRI format: https://datacommons.org/browser/geoId/$1
* Example: Census Tract 110, Penobscot County, Maine = https://datacommons.org/browser/geoId/23019011000

### U.S. census tract block groups

(Data Commons)

* IRI format: https://datacommons.org/browser/geoId/$1
* Example: Block Group 1, Census Tract 110, Penobscot County, Maine = https://datacommons.org/browser/geoId/230190110001
