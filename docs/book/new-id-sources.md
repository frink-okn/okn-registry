# Guidelines for ingesting new sources of identifiers

These guidelines are relevant for graphs that are considering including, as part of their own graph data, the entirety or a significant subset of another external knowledge graph.

## Reasonable sizes

If an external database is of a reasonable size, the Fabric may ingest it if your graph requires it.
A “reasonable size” is one that does not cause the external database to form the plurality of triples in the Proto-OKN.
UniProt and SemOpenAlex are great examples of databases of an unreasonable size.
(Note that Wikidata and the Ubergraph are exempt from this restriction.)

## Text metadata (labels, descriptions)

Graphs should not reproduce the labels/descriptions of entities from external sources.
