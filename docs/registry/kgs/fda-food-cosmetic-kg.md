---
template: overrides/kg.html
shortname: fda-food-cosmetic-kg
title: FDA Food and Cosmetic Knowledge Graph
description: FDA adverse event reports for foods, dietary supplements and cosmetics (CAERS and the cosmetic event reports), FDA's food ingredient inventories (Substances Added to Food, GRAS notices, food contact notifications, SCOGS, food-contact regulations, color additives and others), new dietary ingredient notifications and Total Diet Study results as RDF.
stats: https://registry.okn.us/kg-stats/fda-food-cosmetic-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-food-cosmetic-kg
  documentation-path: fda-food-cosmetic-kg
  kgf:
    semantics:
      prefixes:
        fdafood: "https://bmedesign.org/fda-food-cosmetic-kg/ns/"
        fdafood-id: "https://bmedesign.org/fda-food-cosmetic-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdafood
        - fdafood-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Food and Cosmetic Knowledge Graph publishes the U.S. Food and Drug Administration's consumer adverse event reports for foods, dietary supplements and cosmetics, FDA's food ingredient inventories, new dietary ingredient notifications and the Total Diet Study results as linked data, 7.9 million triples. Every source field is kept, and every record carries its source dataset, record ID, source URL and download date. Reports are de-identified by FDA before release; the graph adds no identifying data.

**Adverse event reports.**
- `fdafood:CaersReport`: one CFSAN Adverse Event Reporting System report (151,589), IRI `https://bmedesign.org/fda-food-cosmetic-kg/id/caers-report/<report number>`. Properties: `fdafood:dateCreated` and `fdafood:dateStarted` (xsd:date), `fdafood:outcomes` (one value per outcome, for example Hospitalization, Visited a Health Care Provider), the consumer's age and gender as a child node, and one `fdafood:CaersProducts` child per product with `fdafood:role` (SUSPECT or CONCOMITANT), `fdafood:nameBrand`, `fdafood:industryCode` and `fdafood:industryName` (FDA's food industry codes, for example 54 Vit/Min/Prot/Unconv Diet).
- `fdafood:CosmeticEvent`: one cosmetic adverse event report (85,511), IRI `.../cosmetic-event/<report number>`, with `fdafood:reportType` (Pre-MoCRA or MoCRA), received and event dates, outcomes, patient gender and age, and one `fdafood:CosmeticProducts` child per product (`fdafood:role`, `fdafood:productName`).
- Reaction terms: both sources code reactions with MedDRA preferred terms. The term text is withheld from the published graph under the MedDRA license; outcomes and product fields are published in full. Links from each report to MedDRA codes are built and will be added once the MSSO confirms in writing what may be published.

**Food ingredient inventories.** Fourteen FDA inventories from the food ingredient and packaging site: Substances Added to Food (3,971), GRAS notices (1,360), effective food contact substance notifications (1,768), Select Committee on GRAS Substances reviews (381), 21 CFR food-contact substances (3,646), color additives (304), the Cumulative Estimated Daily Intake database, threshold-of-regulation exemptions, recycled plastics opinions, the seafood list, new plant variety and new protein consultations, genome-edited plant meetings and post-market assessments. CAS numbers link ingredients to `fda-substance-kg` (5,203 links).

**Notifications and monitoring.** `fdafood:NdiNotification` (new dietary ingredient notifications, with submission and response dates) and `fdafood:TdsResult` (72,899 analyte measurements from the Total Diet Study, fiscal years 2018 to 2020).

**Links to other graphs.** Food and cosmetic recalls are in `fda-compliance-kg`. Ingredient CAS numbers resolve to substance nodes in `fda-substance-kg`.

**Source and license.** openFDA food/event and cosmetic/event, FDA's food ingredient inventories, the NDI notification list and the Total Diet Study data files: public domain U.S. government works. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA food/event (CAERS)
      uri: https://open.fda.gov/apis/food/event/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: openFDA cosmetic/event
      uri: https://open.fda.gov/apis/cosmetic/event/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: FDA food ingredient and packaging inventories (Substances Added to Food, GRAS notices, FCN, SCOGS, color additives and others)
      uri: https://www.fda.gov/food/food-ingredients-packaging
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: FDA Total Diet Study results
      uri: https://www.fda.gov/food/science-research-food/total-diet-study
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```