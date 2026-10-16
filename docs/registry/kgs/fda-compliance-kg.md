---
template: overrides/kg.html
shortname: fda-compliance-kg
title: FDA Compliance Knowledge Graph
description: FDA recalls and enforcement reports for drugs and foods, the FDA warning-letter index and FDA historical documents as RDF, with recall events, firms and links to FDA substances. The shared compliance hub for the FDA regulated-products graphs.
stats: https://registry.okn.us/kg-stats/fda-compliance-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-compliance-kg
  documentation-path: fda-compliance-kg
  kgf:
    semantics:
      prefixes:
        fdacomp: "https://bmedesign.org/fda-compliance-kg/ns/"
        fdacomp-id: "https://bmedesign.org/fda-compliance-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdacomp
        - fdacomp-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Compliance Knowledge Graph publishes U.S. Food and Drug Administration enforcement and compliance data as linked data. The first release holds the openFDA drug enforcement reports (about 18,000 recalls) and food enforcement reports (about 29,500 recalls), the FDA warning-letter index (2,658 letters) and FDA historical documents (8,858), about 1.8 million triples, with every source field kept. Each record carries its source dataset, record ID, source URL and download date. Later releases add FDA inspections, inspection citations, compliance actions and import refusals from the FDA Data Dashboard, keyed on the FDA Establishment Identifier (FEI).

**Main classes.**
- `fdacomp:Recall`: one product recall, IRI `https://bmedesign.org/fda-compliance-kg/id/recall/<recall number, lowercase, punctuation as _>` (for example `.../recall/d_0862_2026`). A recall that FDA has published before assigning its number is keyed by its event instead, `.../recall/event_<event id>_<n>`, and takes the numbered IRI at the first rebuild after FDA assigns one. Properties include `fdacomp:recallNumber`, `fdacomp:classification` (Class I, II, III), `fdacomp:status`, `fdacomp:productType`, `fdacomp:productDescription`, `fdacomp:reasonForRecall`, `fdacomp:codeInfo`, `fdacomp:distributionPattern`, `fdacomp:voluntaryMandated`, the firm's address fields, and the dates `fdacomp:recallInitiationDate`, `fdacomp:centerClassificationDate`, `fdacomp:reportDate` and `fdacomp:terminationDate` as `xsd:date`.
- `fdacomp:RecallEvent`: the FDA recall event that groups several product recalls (`fdacomp:hasRecallEvent`, key `fdacomp:eventId`).
- `fdacomp:RecallingFirm`: the firm as named in the enforcement report (`fdacomp:hasRecallingFirm`). Enforcement data carries no FEI, so firms are keyed by name in this release. Spelling variants are separate nodes until FEI-based resolution is added.
- Warning letters (2,658, from FDA's warning-letter index). Each letter points to the same name-keyed firm node as the recalls, so a firm's recalls and warning letters join on one node.
- Historical documents (8,858 records from FDA's historical document collection).

**Harmonized drug fields.** For drug recalls, openFDA's harmonized fields are kept as `fdacomp:openfda*` properties (for example `fdacomp:openfdaApplicationNumber`, `fdacomp:openfdaBrandName`, `fdacomp:openfdaGenericName`, `fdacomp:openfdaProductNdc`, `fdacomp:openfdaRxcui`, `fdacomp:openfdaSplSetId`, `fdacomp:openfdaUnii`).

**Links to other graphs.** `fdacomp:hasSubstance` links a drug recall to each ingredient's substance in `fda-substance-kg` (`https://bmedesign.org/fda-substance-kg/id/unii/<unii>`). Device recalls stay in `medical-device-kg`. Recall numbers follow the same pattern in both graphs, so a query can match them on `recallNumber`.

**Source and license.** openFDA enforcement data, the FDA warning-letter index and FDA historical documents are public domain U.S. government works (https://open.fda.gov/license/). Contact persons are not ingested. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA drug/enforcement
      uri: https://open.fda.gov/apis/drug/enforcement/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: openFDA food/enforcement
      uri: https://open.fda.gov/apis/food/enforcement/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: FDA warning letters
      uri: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: openFDA other/historicaldocument
      uri: https://open.fda.gov/apis/other/historicaldocument/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
```
