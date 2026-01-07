# Guidelines for ingesting new sources of identifiers

These guidelines are relevant for graphs that are considering including, as part of their own graph data, the entirety or a significant subset of another external knowledge graph.

## Reasonable sizes

If an external database is of a reasonable size, the Fabric may ingest it if your graph requires it.
A “reasonable size” is one that does not cause the external database to form the plurality of triples in the Proto-OKN.
UniProt and SemOpenAlex are great examples of databases of an unreasonable size.
(Note that Wikidata and the Ubergraph are exempt from this restriction.)

## Text metadata (labels, descriptions)

Graphs should not try to reproduce the labels/descriptions of entities from external sources.
(While such reproduction is not inherently a problem for the FRINK Federated SPARQL endpoint, since duplicate triples are simply merged there, it can cause consistency issues when federating between graphs.)

Graphs may attach auxiliary information (e.g. the five predicates [listed here whose names end with 'note'](https://www.w3.org/TR/skos-reference/#notes)) to such entities to clarify their use in those graphs; such notes must make clear to which graph they apply.

## Re-expression of existing relationships

Graphs should not publish *as part of their graphs* triple data that is simply re-expressed from another external knowledge graph (e.g. using different equivalent classes, predicates, or string value representations).
If a graph finds such re-expression desirable, then they may either provide the re-expressed information to the Fabric as a separate data store from the rest of the graph, or they may describe to the Fabric what needs to happen so that this re-expression may be performed by the Fabric themselves.

(An exception may be granted for information from Wikidata, given the abstractions in how data is represented there (e.g. by surfacing the types of entities as [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) in addition to [wdt:P31](http://www.wikidata.org/prop/direct/P31)), *so long as the Fabric are notified in advance of these re-expressions*.)

## Redefinition of existing entities

Graphs should not try to redefine an external entity *using the URI for that entity* if there is no particularly compelling reason to do so.
The Fabric expects the same entity that appears in multiple graphs to be referred to in much the same way, according to set forth best practices, for cross-graph consistency, clarity, and query performance.

If for whatever reason the Fabric allows the redefinition of a class of entities, those entities must all use a novel IRI prefix, the circumstances of this redefinition must be [documented in the graph itself](https://github.com/frink-okn/graph-descriptions/blob/main/README.md), and those entities must all be mapped (using one of the SKOS mapping relations) to their external equivalents.

## Supplementation of existing entities

Graphs may ascribe *new information* to external entities if such information is not present elsewhere, either in the external source of those entities or in other Proto-OKN graphs.
