# Identifiers

An external identifier (hereinafter referred to as an 'identifier') is a string that represents a particular concept within a particular vocabulary or ontology.

Identifiers are designed to be unambiguous with respect to the vocabulary in which they are defined, and are preferably detached from any natural language name for the concept they represent.
For instance, in the KnowWhereGraph, the concept of "Lancaster County, Pennsylvania" is represented with the string "administrativeRegion.USA.42071"--that is, none of the words 'Lancaster', 'County', or 'Pennsylvania' are in that string.

## Using identifiers in RDF

Identifiers for an entity in RDF *can* be represented in two ways: through their inclusion in an Internationalized Resource Identifier (IRI) for that entity, or in a separate string linked to the entity by a dedicated predicate.

Most external vocabularies have an IRI scheme within which an identifier may be provided to yield a canonical reference for a particular entity.
For instance, in the KnowWhereGraph, if an identifier is prefixed with the string "http://stko-kwg.geog.ucsb.edu/lod/resource/", the result is a standard reference to the concept with that identifier.
This reference may then be used as the subject of other RDF triples to define relationships involving that concept.

Some external vocabularies may instead refer to identifiers in other external vocabularies or ontologies through the use of dedicated predicates.
If a vocabulary like the National Cancer Institute Thesaurus (NCIt) wanted to provide a reference on its 'Drosophila' entity to that genus's NCBI taxon database entry, it might use a triple like the following (where the subject, predicate, and object are separated by '⸻' for clarity):

- <http://purl.obolibrary.org/obo/NCIT_C14202> ⸻ <http://purl.obolibrary.org/obo/NCIT_P331> ⸻ "7215"

Here the predicate used indicates that the object of the triple is an NCBI taxon ID.

Because different vocabularies may end up defining the same concepts for whatever reason, it is helpful to have correspondences, however indirect, between IRIs.
One way to do this is to use a [SKOS mapping property](https://www.w3.org/TR/skos-reference/#mapping) to link the two IRIs together:

- <http://purl.obolibrary.org/obo/NCIT_C14202> ⸻ <http://www.w3.org/2004/02/skos/core#exactMatch> ⸻ <http://purl.uniprot.org/taxonomy/7215>
- <http://purl.uniprot.org/taxonomy/7215> ⸻ <http://www.w3.org/2004/02/skos/core#exactMatch> ⸻ <http://www.wikidata.org/entity/Q312154>

## Identifiers in the Proto-OKN

It is preferred throughout the Proto-OKN that entities be referred to using IRIs that encode different identifiers (that is, the first representation described in the previous section).
Thus the city of Lancaster, Pennsylvania should be referred to with the IRI <http://stko-kwg.geog.ucsb.edu/lod/resource/statisticalArea.29540>, rather than using some other arbitrary IRI that is merely connected to the string "statisticalArea.29540".

The Proto-OKN Fabric provides as a starting point for linkages Wikidata's data and the Ubergraph, which contain definitions for different concepts using different identifiers in their IRIs:

- The entity in the NCIt (provided in the Ubergraph) for that same county is referred to with <http://purl.obolibrary.org/obo/NCIT_C109967>, where "C109967" is the NCIt ID for that county.
- The Wikidata entity for Lancaster County, Pennsylvania is referred to with <http://www.wikidata.org/entity/Q142369>, where "Q142369" is the Wikidata item ID for that county.
  - The 'Identifier Mappings' component graph provides SKOS exact match pairings between different identifier IRIs and Wikidata items, allowing for conversion between some identifier schemes through Wikidata.

Different preferences for identifiers in different domains are listed in separate pages of this book.
