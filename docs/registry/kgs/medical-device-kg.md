---
template: overrides/kg.html
shortname: medical-device-kg
title: Medical Device Knowledge Graph
description: Public FDA medical-device data in one linked graph, covering clearances and approvals, UDI device records, MAUDE adverse events, recalls, establishments, standards, and 21 CFR.
stats: https://registry.okn.us/kg-stats/medical-device-kg
homepage: https://bmedesign.org/knowledgegraph
funding: https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2535091
sparql: https://apps.okn.us/medical-device-kg/sparql
tpf: https://apps.okn.us/kgf/medical-device-kg/latest/tpf
kgf: https://apps.okn.us/kgf/medical-device-kg
license: "https://creativecommons.org/licenses/by/4.0/"
funding:
- https://reporter.nih.gov/search/LtUhe8KPaEiv4ffSLv4C0g/project-details/11261252
frink-options:
  lakefs-repo: medical-device-kg
  documentation-path: medical-device-kg
  kgf:
    semantics:
      prefixes:
        mdkg: "https://bmedesign.org/medical-device-kg/ns/"
        mdkg-id: "https://bmedesign.org/medical-device-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "https://bmedesign.org/medical-device-kg/ns/deviceName"
          - "https://bmedesign.org/medical-device-kg/ns/name"
      authoritative_namespaces:
        - mdkg
        - mdkg-id
contacts:
  - email: RocheRey.C.DeGuzman@hofstra.edu
    github: Roche619
    label: "Dr. Roche C. de Guzman"
  - email: Marco.Romanelli@hofstra.edu
    github: marcoromanelli-github
    label: "Dr. Marco Romanelli"
  - email: psingh37@pride.hofstra.edu
    github: Prabhadeus
    label: Prabhjot Singh
  - email: mbukhari1@pride.hofstra.edu
    github: MustafaSBny
    label: Mustafa Bukhari
---
The Medical Device Knowledge Graph converts public U.S. Food and Drug Administration (FDA) device data into one linked RDF graph of about 1.29 billion triples (release v0.0.5, October 2026). Sources include product classification, 510(k) and De Novo clearances, PMA approvals and supplements, Humanitarian Device Exemptions, Devices@FDA decisions, establishment registration and listing, the Global Unique Device Identification Database (5.2 million device records), the full MAUDE adverse-event history (26.1 million reports), recall enforcement reports and the recall database (59,471 recalls, 99% with a recall class), Total Product Life Cycle summaries, Section 522 postmarket studies, recognized consensus standards, CLIA test categorizations, home-use IVD tests, mammography facilities, X-ray assembler reports, and all of Title 21 of the Code of Federal Regulations.

Records join through shared nodes: FDA product code, regulation number, firm (FEI number), and device identifier (UDI-DI). Recall product descriptions that quote a GS1 barcode are linked to the matching UDI device record, so a recall can be traced to specific catalog items. Establishments carry Census geocodes, and product codes are mapped to NAICS industries. Vocabulary terms are under `https://bmedesign.org/medical-device-kg/ns/` and instances under `https://bmedesign.org/medical-device-kg/id/`.

Personal details are removed from MAUDE narrative text, and contact persons are not ingested from any source. The graph supports device safety surveillance, recall and adverse-event analysis, regulatory research, and teaching in biomedical engineering design.

**Main classes and keys.** `mdkg:RecallRecord` (recall number, `mdkg:recallClassification` "Class I/II/III", initiation and termination dates, root cause, `mdkg:codeInfo` lot text), `mdkg:MAUDEReport`, `mdkg:UDIDeviceRecord` and `mdkg:UDIIdentifier` (UDI-DI in `mdkg:identifierId`), `mdkg:K510Record`, `mdkg:PMARecord`, `mdkg:ProductCode` (FDA three-letter code in `mdkg:productCode`), `mdkg:Manufacturer` (FDA FEI number), `mdkg:RegistrationListingRecord` (registered establishments), and `mdkg:TPLCRecord` (MAUDE totals per product code). Recalls link to devices through `mdkg:hasProductCode`, `mdkg:relatedK510Record`, `mdkg:relatedPMARecord`, `mdkg:hasRecallingManufacturer` and, for quoted barcodes, `mdkg:mentionsDeviceIdentifier`.

**Joining with other OKN graphs.** Addresses carry `mdkg:postalCode` (ZIP), `mdkg:city` and `mdkg:state`; establishments carry `mdkg:name` and WGS84 coordinates from the US Census geocoder. Product codes and manufacturers map to NAICS industries through `sudokn:hasNAICSClassifier` (an inferred crosswalk, labelled as such). These support joins by ZIP code with place-based graphs and by NAICS industry or firm name with manufacturing graphs.

**Responsible use.** MAUDE is passive surveillance: report counts are not failure rates, FDA does not verify causation, and the absence of reports is not evidence of safety.
