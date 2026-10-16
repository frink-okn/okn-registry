---
template: overrides/kg.html
shortname: fda-substance-kg
title: FDA Substance Knowledge Graph
description: FDA's Global Substance Registration System (GSRS) and UNII substance identifiers as RDF, with CAS, PubChem, DSSTox, RxCUI and other cross-references for linking drugs, foods, cosmetics, devices and chemical-safety graphs.
stats: https://registry.okn.us/kg-stats/fda-substance-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-substance-kg
  documentation-path: fda-substance-kg
  kgf:
    semantics:
      prefixes:
        fdasub: "https://bmedesign.org/fda-substance-kg/ns/"
        fdasub-id: "https://bmedesign.org/fda-substance-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdasub
        - fdasub-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Substance Knowledge Graph publishes the U.S. Food and Drug Administration's substance registry as linked data. It is built from two public openFDA datasets: the Global Substance Registration System (GSRS, 167,385 substance records) and the Unique Ingredient Identifier list (UNII, 176,619 identifiers), about 54 million triples in the first release. Every source field is kept, and every record carries its source dataset, record ID, source URL and download date.

**Main class.** `fdasub:Substance`, one node per substance. A substance with a UNII has the IRI `https://bmedesign.org/fda-substance-kg/id/unii/<unii in lowercase>`. A GSRS substance without a UNII uses its GSRS UUID: `.../id/gsrs/<uuid>`. Each substance has `rdfs:label` (the GSRS display name), `fdasub:unii`, `fdasub:substanceClass` (chemical, protein, nucleicAcid, polymer, mixture, structurallyDiverse, concept, specifiedSubstanceG1, mention) and the full GSRS record as child nodes.

**Child nodes** sit under their substance's IRI and are typed by GSRS section: `fdasub:GsrsNames` (all names, with type, language and preferred flags), `fdasub:GsrsCodes` (every external code with `fdasub:codeSystem` and `fdasub:code`), `fdasub:GsrsStructure` and `fdasub:GsrsMoieties` (SMILES, formula, molecular weight, stereochemistry, molfile), `fdasub:GsrsProtein`, `fdasub:GsrsNucleicAcid`, `fdasub:GsrsPolymer`, `fdasub:GsrsMixture`, `fdasub:GsrsStructurallyDiverse` (organism and part for natural products), `fdasub:GsrsRelationships`, `fdasub:GsrsProperties`, `fdasub:GsrsNotes` and `fdasub:GsrsReferences` (citations).

**Links between substances.** `fdasub:GsrsRelationships` nodes carry the relationship `fdasub:type` (for example ACTIVE MOIETY, SALT/SOLVATE->PARENT, METABOLITE->PARENT, ENANTIOMER->RACEMATE, TARGET->INHIBITOR) and point to the related substance with `fdasub:relatedSubstanceSubstance`. Natural products link to their parent organism substance with `fdasub:parentSubstanceSubstance`, mixture components with `fdasub:substanceSubstance`, polymer monomers with `fdasub:monomerSubstanceSubstance`, structural modifications with `fdasub:molecularFragmentSubstance` and `fdasub:agentSubstanceSubstance`, and relationship mediators with `fdasub:mediatorSubstanceSubstance`.

**Shortcut identifiers for joins** (PRIMARY codes only, directly on the substance): `fdasub:casNumber`, `fdasub:pubchemCid`, `fdasub:dtxsid` (EPA CompTox), `fdasub:rxcui`, `fdasub:drugbankId`, `fdasub:chebiId`, `fdasub:chemblId`, `fdasub:ecNumber`, `fdasub:meshId`, `fdasub:nciThesaurusCode`, `fdasub:innId`. Use `fdasub:dtxsid` to join to biobricks-ice and other EPA CompTox graphs, `fdasub:pubchemCid` for PubChem-based graphs, and `fdasub:unii` for Wikidata (P652).

**Related graphs.** Other FDA graphs in this family link to these substance IRIs. For example, drug recalls in `fda-compliance-kg` point to the recalled product's ingredients with `hasSubstance`, and food ingredients in `fda-food-cosmetic-kg` link here by CAS number.

**Source and license.** GSRS and UNII data are public domain U.S. government works distributed by openFDA (https://open.fda.gov/license/). Refreshed from openFDA bulk downloads. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA other/substance (GSRS)
      uri: https://open.fda.gov/apis/other/substance/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: openFDA other/unii
      uri: https://open.fda.gov/apis/other/unii/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
```
