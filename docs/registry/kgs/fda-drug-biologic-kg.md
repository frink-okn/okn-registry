---
template: overrides/kg.html
shortname: fda-drug-biologic-kg
title: FDA Drug and Biologic Knowledge Graph
description: FDA drug and biologic regulatory data as RDF, keyed on the application number (NDA, ANDA, BLA): Drugs@FDA, the NDC Directory, the Orange Book, the Purple Book, NSDE, drug shortages and complete response letters, linked to FDA substances.
stats: https://registry.okn.us/kg-stats/fda-drug-biologic-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-drug-biologic-kg
  documentation-path: fda-drug-biologic-kg
  kgf:
    semantics:
      prefixes:
        fdadrug: "https://bmedesign.org/fda-drug-biologic-kg/ns/"
        fdadrug-id: "https://bmedesign.org/fda-drug-biologic-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdadrug
        - fdadrug-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Drug and Biologic Knowledge Graph publishes the U.S. Food and Drug Administration's drug and biologic approval, listing and marketing data as linked data, about 36.5 million triples in the first release. Every source field is kept, and every record carries its source dataset, record ID, source URL and download date.

**The hub is the application.** `fdadrug:DrugApplication`, IRI `https://bmedesign.org/fda-drug-biologic-kg/id/application/<nda|anda|bla><6 digits>` (for example `.../application/nda021234`). Every source that names an application number is normalized to this one IRI, so a query can start from any of them: Drugs@FDA (29,383 applications from openFDA and the Drugs@FDA data files), the NDC Directory (`fdadrug:hasApplication`), the Orange Book, the Purple Book (BLAs), NSDE and drug shortages. About 30,000 distinct application IRIs are referenced in the first release.

**Products, submissions and documents.** Under each application: `.../product/<product number>` (`fdadrug:DrugProduct` from the Drugs@FDA files, also typed `fdadrug:OrangeBookProduct` when the Orange Book lists it) with marketing status and therapeutic-equivalence codes; `.../submission/<type>-<number>` (`fdadrug:Submission`, with status, status date, class and review priority) and its documents (`fdadrug:ApplicationDocument`, with the accessdata URL of each letter, label or review); Orange Book patents (`fdadrug:OrangeBookPatent`, with expiry date and use code) and exclusivities under their product (`fdadrug:OrangeBookExclusivityRecord` for the Orange Book data-file rows; `fdadrug:OrangeBookExclusivity` is the matching openFDA child node). From the Purple Book, both the monthly change rows (`fdadrug:PurpleBookChange`, 5,505) and the current licensed-product list (`fdadrug:PurpleBookProduct`, 2,251) sit under their BLA.

**NDC listings.** `fdadrug:NdcProduct` (138,419 products, IRI `.../ndc-product/<product_id>`) with labeler, dosage form, route, marketing category, active ingredients and openFDA's harmonized fields (RxCUI, SPL set ID, pharmacologic class). Package NDCs are shared nodes, `.../ndc-package/<package ndc>` (`fdadrug:NdcPackage`): the NDC Directory packaging list, the NSDE listing (670,521 packages, with marketing start and end dates) and drug shortages all point at the same node.

**Shortages and letters.** `fdadrug:DrugShortage` (1,580 rows: status, reason, availability, update dates) linked to package NDCs and applications; `fdadrug:CompleteResponseLetter` (458 letters from FDA's transparency release, with the letter text).

**Every link resolves.** Stub nodes (`fdadrug:isStub true`) stand in for 2,373 applications and 1,201 package NDCs that other sources reference but Drugs@FDA and the NDC Directory do not list, so no link points to an untyped IRI.

**Links to other graphs.** `fdadrug:hasSubstance` links products, applications and shortages to `fda-substance-kg` by UNII (about 200,000 links in the first release). Drug recalls live in `fda-compliance-kg` and link back here through the same UNII and application IRIs.

**Not yet included.** DailyMed SPL labels and FAERS adverse-event reports. Both are large (SPL labels roughly 0.3 to 0.5 billion triples; FAERS likely 3 to 5 billion) and are planned for a later release after sizing with the FRINK team. FAERS may be proposed as its own graph.

**Source and license.** openFDA (drug/drugsfda, drug/ndc, drug/orangebook, drug/shortages, other/nsde, transparency/crl), the Drugs@FDA data files, the Orange Book data files and the Purple Book monthly downloads: public domain U.S. government works. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA drug endpoints (drugsfda, ndc, orangebook, shortages) and other/nsde, transparency/crl
      uri: https://open.fda.gov/apis/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: Drugs@FDA data files
      uri: https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: Orange Book data files
      uri: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
  - derivedFrom:
      label: Purple Book monthly downloads
      uri: https://purplebooksearch.fda.gov/downloads
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```
