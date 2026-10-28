---
template: overrides/kg.html
shortname: fda-drug-event-kg
title: FDA Drug and Vaccine Adverse Event Knowledge Graph
description: FDA Adverse Event Reporting System (FAERS) and Vaccine Adverse Event Reporting System (VAERS) reports as RDF, with patient, drug, vaccine, reaction and outcome fields, linked to FDA applications, package NDCs and substances.
stats: https://registry.okn.us/kg-stats/fda-drug-event-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-drug-event-kg
  documentation-path: fda-drug-event-kg
  kgf:
    semantics:
      prefixes:
        fdaevent: "https://bmedesign.org/fda-drug-event-kg/ns/"
        fdaevent-id: "https://bmedesign.org/fda-drug-event-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdaevent
        - fdaevent-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Drug and Vaccine Adverse Event Knowledge Graph publishes the two largest U.S. post-market safety reporting systems for human medical products as linked data: FAERS (openFDA drug/event, 20.7 million reports) and VAERS (vaers.hhs.gov, 3.6 million reports from 1990 on, domestic and non-domestic). Every source field is kept except licensed terminology text (below), and every report carries its source dataset, report ID, source URL and download date. It is the seventh graph of the FDA regulated-products family and the one expected to be large: VAERS is 201 million triples; FAERS is expected at 2 to 3 billion.

**FAERS.** `fdaevent:AdverseEventReport`, IRI `https://bmedesign.org/fda-drug-event-kg/id/report/<safetyreportid>`, with receive, receipt and transmission dates (xsd:date), seriousness flags, report source, sender and primary source qualification. Child nodes per report: the patient (age, sex, weight, death date), one `fdaevent:FaersDrug` per drug (characterization, product name, dosage, route, indication, start and end dates, action taken, openFDA harmonized fields) and one `fdaevent:FaersReaction` per reaction (MedDRA version and outcome code).

**VAERS.** `fdaevent:VaersReport`, IRI `.../vaers-report/<VAERS_ID>`, with all columns of the VAERS data file (receive date, state, age, sex, outcome flags, recovery, onset interval, reporter narrative text, lab data, medical history, allergies). `fdaevent:VaersVaccination` (one per vaccine: type, manufacturer, lot, dose series, route, site, name) and `fdaevent:VaersSymptomSet` (one per symptom row: term count and MedDRA versions) link back to their report.

**Links to other graphs.** `fdaevent:hasApplication`, `fdaevent:hasPackageNdc` and `fdaevent:hasSubstance` on FAERS reports point at the application, package NDC and UNII substance IRIs of `fda-drug-biologic-kg` and `fda-substance-kg`, lifted from each drug entry's openFDA block.

**Licensed terminology.** Reaction and symptom terms in both sources are MedDRA preferred terms. MedDRA term text is withheld from the published graph pending the MedDRA license review (MedDRA codes, versions, outcomes and every non-MedDRA field are published in full). The terms will be added once the subscription and the MSSO's written answer on publication are in hand.

**Responsible use.** These are passive, voluntary reports: counts are not incidence rates, and a report does not establish that a product caused the event. VAERS reports are accepted without verification.

**Source and license.** openFDA drug/event and the VAERS data downloads (HHS, CDC and FDA): public domain U.S. government works. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA drug/event (FAERS)
      uri: https://open.fda.gov/apis/drug/event/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: VAERS data downloads
      uri: https://vaers.hhs.gov/data/datasets.html
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```
