# spoke





## Schema Diagram

```mermaid
erDiagram
Neo4jCompound {
    string neo4j_sources  
    string neo4j_identifier  
    string neo4j_name  
}
Neo4jDisease {
    string neo4j_identifier  
    string neo4j_source  
    string neo4j_name  
}
Neo4jEnvironment {
    string neo4j_sources  
    string neo4j_identifier  
    string neo4j_name  
}
Neo4jLocation {
    string neo4j_identifier  
    string neo4j_name  
    string neo4j_sources  
}
Neo4jOrganism {
    string neo4j_sources  
    string neo4j_identifier  
    string neo4j_name  
}
Neo4jSDoH {
    string neo4j_sources  
    string neo4j_identifier  
    string neo4j_name  
}

Neo4jCompound ||--|o Neo4jCompound : "neo4j_ISA_CiC"
Neo4jCompound ||--|o Neo4jLocation : "neo4j_FOUNDIN_CfL"
Neo4jCompound ||--|o Neo4jCompound : "neo4j_INTERACTS_CiC"
Neo4jCompound ||--|o Neo4jCompound : "neo4j_PARTOF_CpC"
Neo4jCompound ||--|o Neo4jDisease : "neo4j_TREATS_CtD"
Neo4jCompound ||--|o Neo4jCompound : "neo4j_HASROLE_ChC"
Neo4jCompound ||--|o Neo4jDisease : "neo4j_CONTRAINDICATES_CcD"
Neo4jDisease ||--|o Neo4jDisease : "neo4j_RESEMBLES_DrD"
Neo4jDisease ||--|o Neo4jDisease : "neo4j_ISA_DiD"
Neo4jDisease ||--|o Neo4jLocation : "neo4j_MORTALITY_DmL"
Neo4jDisease ||--|o Neo4jLocation : "neo4j_PREVALENCE_DpL"
Neo4jEnvironment ||--|o Neo4jLocation : "neo4j_FOUNDIN_EfL"
Neo4jEnvironment ||--|o Neo4jEnvironment : "neo4j_ISA_EiE"
Neo4jLocation ||--|o Neo4jLocation : "neo4j_PARTOF_LpL"
Neo4jOrganism ||--|o Neo4jCompound : "neo4j_RESPONDS_TO_OrC"
Neo4jOrganism ||--|o Neo4jLocation : "neo4j_ISOLATEDIN_OiL"
Neo4jSDoH ||--|o Neo4jSDoH : "neo4j_ISA_SiS"
Neo4jSDoH ||--|o Neo4jLocation : "neo4j_PREVALENCEIN_SpL"
Neo4jSDoH ||--|o Neo4jDisease : "neo4j_ASSOCIATES_SaD"

```



## Imports


* linkml:types



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [Neo4jCompound](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jCompound.md) | None<br/>| 798 | 
| [Neo4jDisease](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jDisease.md) | None<br/>| 180 | 
| [Neo4jEnvironment](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jEnvironment.md) | None<br/>| 2 | 
| [Neo4jLocation](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jLocation.md) | None<br/>| 106067 | 
| [Neo4jOrganism](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jOrganism.md) | None<br/>| 321442 | 
| [Neo4jSDoH](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/classes/Neo4jSDoH.md) | None<br/>| 1426 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [neo4j_ASSOCIATES_SaD](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ASSOCIATES_SaD.md) | <br/>| 39 |
| [neo4j_CONTRAINDICATES_CcD](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_CONTRAINDICATES_CcD.md) | <br/>| 51 |
| [neo4j_FOUNDIN_CfL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_FOUNDIN_CfL.md) | <br/>| 563803 |
| [neo4j_FOUNDIN_EfL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_FOUNDIN_EfL.md) | <br/>| 11367 |
| [neo4j_HASROLE_ChC](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_HASROLE_ChC.md) | <br/>| 34 |
| [neo4j_identifier](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_identifier.md) | <br/>| 429915 |
| [neo4j_INTERACTS_CiC](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_INTERACTS_CiC.md) | <br/>| 1 |
| [neo4j_ISA_CiC](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ISA_CiC.md) | <br/>| 56 |
| [neo4j_ISA_DiD](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ISA_DiD.md) | <br/>| 41 |
| [neo4j_ISA_EiE](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ISA_EiE.md) | <br/>| 1 |
| [neo4j_ISA_SiS](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ISA_SiS.md) | <br/>| 999 |
| [neo4j_ISOLATEDIN_OiL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_ISOLATEDIN_OiL.md) | <br/>| 321442 |
| [neo4j_MORTALITY_DmL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_MORTALITY_DmL.md) | <br/>| 10802 |
| [neo4j_name](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_name.md) | <br/>| 429915 |
| [neo4j_PARTOF_CpC](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_PARTOF_CpC.md) | <br/>| 18 |
| [neo4j_PARTOF_LpL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_PARTOF_LpL.md) | <br/>| 119810 |
| [neo4j_PREVALENCE_DpL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_PREVALENCE_DpL.md) | <br/>| 275085 |
| [neo4j_PREVALENCEIN_SpL](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_PREVALENCEIN_SpL.md) | <br/>| 2999117 |
| [neo4j_RESEMBLES_DrD](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_RESEMBLES_DrD.md) | <br/>| 67 |
| [neo4j_RESPONDS_TO_OrC](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_RESPONDS_TO_OrC.md) | <br/>| 5138 |
| [neo4j_source](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_source.md) | <br/>| 180 |
| [neo4j_sources](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_sources.md) | <br/>| 432273 |
| [neo4j_TREATS_CtD](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-kg/slots/neo4j_TREATS_CtD.md) | <br/>| 163 |









## IRI prefixes

* linkml: https://w3id.org/linkml/
* neo4j: neo4j://graph.schema#
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* xsd: http://www.w3.org/2001/XMLSchema#
* shex: http://www.w3.org/ns/shex#
* schema: http://schema.org/
