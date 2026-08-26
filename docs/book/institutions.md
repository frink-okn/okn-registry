# Identifier choice guidelines for institutions

This page lists recommendations of identifiers to use for legal entities (corporate bodies, non-profit organizations, etc.). It is likely that these will evolve and will apply most leniently since, unlike with some of the other domains within the Proto-OKN, there is not one particular identifier which is clearly more appropriate than the others for identifying even organizations within a particular subdomain.

## Entity classes

Each recommendation consists of at minimum an IRI format (in which the substring "$1" is replaced with a particular identifying string) and an example of an IRI using that format to refer to an entity.

Some recommendations below are given as triple examples, where the subject and predicate, and the predicate and object, are split using a "⸻" for clarity.

### Product categories

There is in general no need for all categories of products to prefer a particular IRI format over others, given how diverse products are in the first place.

Some United Nations identifiers exist, however, that could be attached to entities using particular predicates:

* Standard Products and Services Code (<http://www.wikidata.org/prop/direct/P2167>)
    * Example: <http://www.wikidata.org/entity/Q180481> ⸻ <http://www.wikidata.org/prop/direct/P2167> ⸻ "25101703"
    * ~1.5k IDs mapped to Wikidata
* Central Product Classification (<http://www.wikidata.org/prop/direct/P11373>)
    * Example: <http://www.wikidata.org/entity/Q334637> ⸻ <http://www.wikidata.org/prop/direct/P11373> ⸻ "35322"
    * 170 IDs mapped to Wikidata
* Harmonized System Code (2022) (<http://www.wikidata.org/prop/direct/P5471>)
    * Example: <http://www.wikidata.org/entity/Q174320> ⸻ <http://www.wikidata.org/prop/direct/P5471> ⸻ "903020"
    * 156 IDs mapped to Wikidata

Among those which were not introduced by the United Nations:

* GS1 Global Product Classification (<http://www.wikidata.org/prop/direct/P8957>)
    * Example: <http://www.wikidata.org/entity/Q722338> ⸻ <http://www.wikidata.org/prop/direct/P8957> ⸻ "10000273"
    * 423 IDs mapped to Wikidata

### Businesses

The following identifiers for businesses do not have RDF-compatible IRIs known to the Fabric, and must be attached to entities using particular predicates:

* ISNI (<http://www.wikidata.org/prop/direct/P213>)
    * Example: <http://www.wikidata.org/entity/Q19861084> ⸻ <http://www.wikidata.org/prop/direct/P213> ⸻ "0000000446638501"
    * ISO 27729-defined standard
    * 2.4 million IDs mapped to Wikidata
* PermID (<http://www.wikidata.org/prop/direct/P3347>)
    * Example: <http://www.wikidata.org/entity/Q1022711> ⸻ <http://www.wikidata.org/prop/direct/P3347> ⸻ "4295905828"
    * ~6k IDs mapped to Wikidata
* D-U-N-S (<http://www.wikidata.org/prop/direct/P2771>)
    * Example: <http://www.wikidata.org/entity/Q19861084> ⸻ <http://www.wikidata.org/prop/direct/P2771> ⸻ "968806054"
    * 491 IDs mapped to Wikidata
* CAGE (<http://www.wikidata.org/prop/direct/P5574>)
    * Example: <http://www.wikidata.org/entity/Q19861084> ⸻ <http://www.wikidata.org/prop/direct/P5574> ⸻ "6MHA5"
    * 255 IDs mapped to Wikidata

There is, however, at least one identifier that could be used to form an IRI for a business entity:

* Legal Entity Code (https://rdf.gleif.org/L1/L-$1)
    * Example: ORCID, Inc. = https://rdf.gleif.org/L1/L-875500AZPSXM0HP6VP03
    * ISO 17442-defined standard
    * 53k IDs mapped to Wikidata
