---
template: overrides/kg.html
shortname: fda-animal-health-kg
title: FDA Animal Health Knowledge Graph
description: FDA Center for Veterinary Medicine adverse event reports for animal drugs and devices as RDF, with the animal, the drugs and active ingredients, doses, routes and outcomes for 1.38 million reports.
stats: https://registry.okn.us/kg-stats/fda-animal-health-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-animal-health-kg
  documentation-path: fda-animal-health-kg
  kgf:
    semantics:
      prefixes:
        fdavet: "https://bmedesign.org/fda-animal-health-kg/ns/"
        fdavet-id: "https://bmedesign.org/fda-animal-health-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdavet
        - fdavet-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Animal Health Knowledge Graph publishes the Center for Veterinary Medicine's adverse event reports as linked data: 1,378,854 reports from 1987 to 2026, about 148 million triples. Every source field is kept, and every report carries its source dataset, report ID, source URL and download date.

**Main class.** `fdavet:AnimalEvent`, IRI `https://bmedesign.org/fda-animal-health-kg/id/animal-event/<unique AER id>` (for example `.../animal-event/usa_usfdacvm_2015_us_048928`). Properties include `fdavet:originalReceiveDate` and `fdavet:onsetDate` (xsd:date), `fdavet:numberOfAnimalsAffected`, `fdavet:numberOfAnimalsTreated`, `fdavet:primaryReporter`, `fdavet:typeOfInformation`, `fdavet:healthAssessmentPriorToExposure` and `fdavet:foreignOrDomestic`.

**Child nodes** under each report: `fdavet:AnimalEventAnimal` (species, breed, gender, age with unit, weight with unit, reproductive status), one `fdavet:AnimalEventDrug` per drug (brand name, dosage form, route, ATC vet code, manufacturer name and CVM registration number, lot numbers, dose and frequency, use according to label, previous exposure) with `fdavet:AnimalEventActiveIngredients` children (ingredient name and dose), `fdavet:AnimalEventOutcome` (medical status and number of animals), `fdavet:AnimalEventReceiver` (the receiving FDA office) and `fdavet:AnimalEventReaction` (VeDDRA version, term code and term name).

**Responsible use.** These are passive surveillance reports: counts are not incidence rates, and a report does not establish that a drug caused the event.

**Planned additions.** Animal Drugs @ FDA (NADA and ANADA applications, the Green Book), the VFD drug list and CVM recalls, which will give each drug node an application to link to.

**Source and license.** openFDA animalandveterinary/event: public domain U.S. government works. Reactions are coded in VeDDRA, which is maintained by the European Medicines Agency (EMA); VeDDRA term names are kept in the published graph with attribution to EMA, whose legal notice allows reuse with acknowledgement, and are not covered by the CC0 dedication. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA animalandveterinary/event
      uri: https://open.fda.gov/apis/animalandveterinary/event/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: VeDDRA (Veterinary Dictionary for Drug Regulatory Activities), European Medicines Agency
      uri: https://www.ema.europa.eu/en/veterinary-regulatory-overview/post-authorisation-veterinary-medicines/pharmacovigilance-veterinary-medicines/eudravigilance-veterinary
      kind: Terminology
      license:
        data:
          label: EMA legal notice (reuse with acknowledgement)
          uri: https://www.ema.europa.eu/en/about-us/legal-notice
```
