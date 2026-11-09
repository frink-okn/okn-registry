---
template: overrides/kg.html
shortname: fda-compliance-kg
title: FDA Compliance Knowledge Graph
description: FDA recalls and enforcement reports for drugs and foods, warning letters, inspections, compliance actions, import refusals, Import Alerts and the import product code taxonomy as RDF, keyed on the FDA Establishment Identifier (FEI). The shared compliance hub for the FDA regulated-products graphs.
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
The FDA Compliance Knowledge Graph publishes U.S. Food and Drug Administration enforcement and compliance data as linked data, 79.6 million triples, with every source field kept. Each record carries its source dataset, record ID, source URL and download date. Contact persons are never ingested.

**Recalls and letters.**
- `fdacomp:Recall`: one product recall from the openFDA drug (about 18,000) and food (about 29,500) enforcement reports, IRI `https://bmedesign.org/fda-compliance-kg/id/recall/<recall number, lowercase, punctuation as _>` (for example `.../recall/d_0862_2026`). A recall FDA publishes before assigning its number is keyed by its event, `.../recall/event_<event id>_<n>`. Properties include `fdacomp:recallNumber`, `fdacomp:classification` (Class I, II, III), `fdacomp:status`, `fdacomp:productType`, `fdacomp:productDescription`, `fdacomp:reasonForRecall`, `fdacomp:codeInfo`, `fdacomp:distributionPattern`, `fdacomp:voluntaryMandated`, the firm's address fields, and the dates `fdacomp:recallInitiationDate`, `fdacomp:centerClassificationDate`, `fdacomp:reportDate` and `fdacomp:terminationDate` as `xsd:date`.
- `fdacomp:RecallEvent` groups the product recalls of one event (`fdacomp:hasRecallEvent`); `fdacomp:RecallingFirm` is the firm as named in the report (`fdacomp:hasRecallingFirm`); `fdacomp:RecallAnnouncement` holds FDA's recall press announcements.
- `fdacomp:WarningLetter` (2,658 letters from FDA's warning-letter index) and `fdacomp:HistoricalDocument` (8,858 records from FDA's historical document collection).
- `fdacomp:Debarment` (157 persons on the statutory debarment list) and `fdacomp:InvestigatorDisqualification` (232 clinical investigator disqualification proceedings).

**Firms keyed on FEI (FDA Data Dashboard).** `fdacomp:Firm`, IRI `.../firm/<FEI>`, 308,281 nodes, the hub the drug, biologic and device establishment registries point at. Under them: `fdacomp:Inspection` (277,629), `fdacomp:InspectionClassification` (344,801: NAI, VAI, OAI), `fdacomp:InspectionCitation` (282,639, with the 21 CFR citation), `fdacomp:ComplianceAction` (178,208: warning letters, seizures, injunctions, import alerts as actions) and `fdacomp:ImportRefusal` (211,920 refused entry lines with product code, refusal charges and date). Firms that other graphs reference but the Dashboard does not list (9,583, mostly DECRS and CBER establishments) are stub nodes with `fdacomp:isStub true`.

**Import Alerts and the product code taxonomy.** `fdacomp:ImportAlert` (154 alerts), each with its listed firms per list color (`fdacomp:ImportAlertFirm`, 24,164, red, yellow or green) and the products under each firm (`fdacomp:ImportAlertFirmProduct`, 128,106). The Product Code Builder taxonomy gives import product codes a home: `fdacomp:ImportIndustry` (89), `fdacomp:ImportProductClass` (1,159), `fdacomp:ImportProductSubclass` (117), `fdacomp:ImportProcessIndicator` (80), `fdacomp:ImportProduct` (26,357) and `fdacomp:ImportProductCode` (3,041,333 full seven-character codes, each linked to its industry, class, subclass, process indicator and product). Import refusals (211,919 of 211,920) and Import Alert product rows (128,106 of 128,686) link into this taxonomy with `fdacomp:hasProductCode`, `fdacomp:hasImportIndustry`, `fdacomp:hasImportClass` and `fdacomp:hasImportProduct`.

**Harmonized drug fields.** For drug recalls, openFDA's harmonized fields are kept as `fdacomp:openfda*` properties (for example `fdacomp:openfdaApplicationNumber`, `fdacomp:openfdaBrandName`, `fdacomp:openfdaProductNdc`, `fdacomp:openfdaRxcui`, `fdacomp:openfdaSplSetId`, `fdacomp:openfdaUnii`).

**Links to other graphs.** `fdacomp:hasSubstance` links a drug recall to each ingredient's substance in `fda-substance-kg`. FEI firm nodes are the join point for the drug establishment registry (DECRS), the CBER blood and HCT/P establishment registries in `fda-drug-biologic-kg`, and for device manufacturers in `medical-device-kg`, which carries the same FEI numbers. Device recalls stay in `medical-device-kg`; recall numbers follow the same pattern in both graphs.

**Source and license.** openFDA enforcement data, the FDA warning-letter index, FDA historical documents, the FDA Data Dashboard and Product Code Builder APIs, the Import Alerts site and the debarment and disqualification lists are public domain U.S. government works (https://open.fda.gov/license/). Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


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
  - derivedFrom:
      label: FDA Data Dashboard API (inspections, citations, compliance actions, import refusals)
      uri: https://datadashboard.fda.gov/ora/api/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: FDA Product Code Builder API
      uri: https://www.accessdata.fda.gov/scripts/ora/pcb/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: FDA Import Alerts
      uri: https://www.accessdata.fda.gov/cms_ia/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```