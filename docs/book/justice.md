# Identifier choice guidelines in the realm of justice

The page on identifiers for institutions may also be worth consulting here.

## NIEM standards

There is a growing consensus to use [NIEM Open](https://niemopen.org/) predicates for representing different types of entities in the justice space.
Current graphs use, in addition to the [core model](https://github.com/niemopen/niem-model) version 5.0, the [Justice XML Data Model](https://niemopen.org/community/justice/) version 7.3 and [OmniClass Construction Specifications](https://github.com/niemopen/niem-model/blob/main/xsd/codes/occs.xsd) version 5.0.

The Proto-OKN will seek to ensure a correspondence between entity types and relationships defined in NIEM and existing RDF entities and relationships where possible.

## Entity classes

### U.S. judicial circuits

(KnowWhereGraph)

* IRI format: http://stko-kwg.geog.ucsb.edu/lod/resource/circuit.$1
* Example: Ninth Circuit = http://stko-kwg.geog.ucsb.edu/lod/resource/circuit.9

See also the page on geospatial identifiers.

### U.S. judicial districts

(KnowWhereGraph)

* IRI format: http://stko-kwg.geog.ucsb.edu/lod/resource/federalJudicialDistrict.$1
* Example: Northern District of Iowa = http://stko-kwg.geog.ucsb.edu/lod/resource/federalJudicialDistrict.89

See also the page on geospatial identifiers.
