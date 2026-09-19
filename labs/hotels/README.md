# Hospitality Distribution Ecosystem & Revenue / Cost Splits

An interactive, multi-tier data visualization dashboard mapping the complete global hospitality room journey, all distribution intermediaries, customer segments, and financial revenue/cost splits.

---

## Quick Start: Launching the Dashboard

You can view the dashboard by opening `index.html` in any web browser, or by running a local HTTP server:

```bash
cd "/run/media/ml/Storage/Labs"
python3 -m http.server 8080
```

Then open your browser to: **`http://localhost:8080`** (or open [`/run/media/ml/Storage/Labs/index.html`](file:///run/media/ml/Storage/Labs/index.html) directly).

---

## Key Executive Metrics & Global Sizing

The model uses a normalized global accommodation room market baseline of **$600.0 Billion USD** in Gross Booking Value (GBV), representing approximately **4.25 Billion room nights** globally at a blended ADR of **$141.18**.

| Metric | Amount ($B) | Share (%) | Industry Context |
| :--- | :--- | :--- | :--- |
| **Global Room Gross Booking Value (GBV)** | **$600.0B** | **100.0%** | Total guest spend on hotel room inventory globally |
| **Intermediary & Distribution Cost** | **$87.7B** | **14.6%** | Blended distribution friction (OTAs, GDS, Bedbanks, TMCs, Tech, Cards) |
| **Net Hotel Room Revenue** | **$512.3B** | **85.4%** | Net revenue retained by property owners / operators |
| **Direct Channels Share** | **$210.0B** | **35.0%** | Brand.com, Loyalty App, Central Voice (CRO), Property Walk-in |
| **Intermediated Channels Share** | **$390.0B** | **65.0%** | OTAs, GDS, Bedbanks, TMCs, Consortia, Tour Operators |
| **Hotel Operating Expenses** | **$317.7B** | **53.0%** | Rooms labor, utilities, maintenance, local marketing, taxes & G&A |
| **Gross Operating Profit (GOP / EBITDA)** | **$194.6B** | **32.4%** | 38.0% margin on Net Room Revenue |

---

## 5-Tier Journey Architecture

The master Sankey diagram maps 32 nodes across 5 distinct tiers connected by 55 proportional flows:

```
[Tier 0: Hotel Room Supply ($600B)]
   │
   ├── Branded & Chain Hotels ($270B / 45%)
   ├── Independent & Boutique Hotels ($250B / 42%)
   ├── Resorts, Casinos & Luxury Destinations ($50B / 8%)
   └── Serviced Apartments & Extended Stay ($30B / 5%)
   │
[Tier 1: Tech & Connectivity Infrastructure ($600B)]
   │
   ├── Central Reservation Systems / CRS ($280B) ── [Sabre SynXis, Amadeus iHotelier, Windsurfer, MARSHA, OnQ]
   ├── Channel Managers & Switches ($220B) ──────── [SiteMinder, RateGain, DerbySoft, D-EDGE, Pegasus]
   ├── Direct Property PMS & Front Desk ($70B) ───── [Oracle Opera, Cloudbeds, Mews, Protel]
   └── Group & MICE Sales Engines ($30B) ─────────── [Amadeus Delphi, Cvent, MeetingBroker]
   │
[Tier 2: Primary Channels & Aggregators ($600B)]
   │
   ├── Direct Brand.com Web & App ($130B)
   ├── Hotel Loyalty Platform / CUG ($35B)
   ├── Direct Voice & CRO ($20B)
   ├── Property Walk-in & Front Desk ($25B)
   ├── Global Mega-OTAs ($165B) ─────────────────── [Booking Holdings, Expedia Group, Trip.com Group]
   ├── Regional & Niche OTAs ($30B) ──────────────── [Traveloka, Despegar, MakeMyTrip, HRS, Rakuten]
   ├── Global Distribution Systems / GDS ($105B) ─── [Sabre, Amadeus, Travelport]
   ├── Bedbanks & Wholesalers ($60B) ────────────── [Hotelbeds, WebBeds, Travco]
   └── Direct Group & MICE Sales ($30B)
   │
[Tier 3: Secondary Intermediaries, Retailers & Front-Ends ($600B)]
   │
   ├── Direct Brand / Property Front-Ends ($195B)
   ├── Corporate Direct Portals ($15B)
   ├── OTA Consumer Apps & Sites ($195B)
   ├── Corporate TMCs & OBTs ($90B) ─────────────── [Amex GBT, BCD Travel, CWT, Navan, SAP Concur]
   ├── Retail Travel Agencies & Consortia ($40B) ─── [Virtuoso, Signature, Amex FHR, independent agents]
   ├── Tour Operators & Packaging ($35B) ────────── [TUI Group, Jet2holidays, Der Touristik, Airline Vacations]
   └── Group Event Planners & PCOs ($30B)
   │
[Tier 4: End Customer & Demand Segments ($600B)]
   │
   ├── Leisure FIT (Free Independent Travelers) ($230B / 38.3%)
   ├── Corporate Managed Business Travelers ($95B / 15.8%)
   ├── Corporate Unmanaged / SME Travelers ($55B / 9.2%)
   ├── Leisure Package & Holidaymakers ($55B / 9.2%)
   ├── Group, Conferences & MICE ($55B / 9.2%)
   ├── Loyalty Program Power Users ($50B / 8.3%)
   ├── Luxury & VIP Consortia Guests ($35B / 5.8%)
   └── Walk-in & Emergency Last-Minute ($25B / 4.2%)
```

---

## Financial Waterfall: Revenue to EBITDA Split

Modeled like an enterprise corporate earnings statement, tracking every dollar from gross consumer booking to hotel net profit:

```
Gross Booking Value (GBV) .............................. $600.0B  (100.0%)
  Less: Intermediary & Distribution Friction:
    - OTA Commissions (blended 18.0%) .................. -$35.1B  (-5.85%)
    - Bedbank & Wholesale Markups (22.0% net margin) ... -$13.2B  (-2.20%)
    - GDS Booking & Segment Fees ($4.50-$6/booking) ....  -$4.8B  (-0.80%)
    - TMC Management & Tech Fees (6.3% blended) ........  -$5.7B  (-0.95%)
    - Consortia & Retail Agent Commissions (10.0%) .....  -$4.5B  (-0.75%)
    - Metasearch Ad Spend / CPC (8.0% of influenced) ...  -$5.2B  (-0.87%)
    - Tech Stack SaaS & Per-Txn Fees (CRS/CM/PMS) ......  -$4.2B  (-0.70%)
    - Credit Card Merchant Processing (2.5% blended) ... -$15.0B  (-2.50%)
-------------------------------------------------------------------------
Net Hotel Room Revenue Retained ........................ $512.3B  (85.4% of GBV)

  Less: Hotel Operating Expenses (OpEx):
    - Rooms Department Labor & Linens (25.0% of Net) ... -$128.1B (-21.35%)
    - Brand Franchise & Royalty Fees (9.0% of Net) .....  -$46.1B  (-7.68%)
    - Property Operations, Maintenance & Utilities .....  -$51.2B  (-8.53%)
    - Local Sales & Property Marketing .................  -$35.9B  (-5.98%)
    - G&A, Property Taxes & Commercial Insurance .......  -$56.4B  (-9.40%)
-------------------------------------------------------------------------
Gross Operating Profit (GOP / EBITDA) .................. $194.6B  (32.4% of GBV / 38.0% of Net)
```

---

## 10 Specific Hospitality Distribution Archetypes

The dashboard includes detailed technical, operational, and financial breakdowns for 10 real-world channel pathways:

1. **Hotelbeds Wholesale to TMC Corporate**:
   - *Flow*: Hotel ➔ Channel Manager ➔ Hotelbeds (Bedbank) ➔ TMC ➔ Corporate Guest
   - *Economics ($200 ADR)*: Hotel receives **$154.00 (77.0% net yield)**; Bedbank markup $31.20, TMC fee $12.80, Channel Manager $2.00.
   - *Tech*: OpenTravel XML ➔ Bedbank B2B REST API ➔ Concur OBT.

2. **GDS to Consortia / Travel Agent Luxury Journey**:
   - *Flow*: Hotel ➔ GDS ➔ Travel Agent / Consortia ➔ Corporate / Luxury Guest
   - *Economics ($400 ADR)*: Hotel receives **$333.50 (83.4% net yield)**; Travel Agent commission $40.00, GDS fee $12.00, CRS fee $4.50, Card interchange $10.00.
   - *Tech*: CRS ➔ Pegasus / UltraSwitch ➔ GDS EDIFACT ➔ Sabre Red 360 / Amadeus Selling Platform.

3. **Channel Manager to Mega-OTA Leisure Journey**:
   - *Flow*: Hotel ➔ Channel Manager ➔ Mega-OTA (Booking/Expedia) ➔ Leisure Guest
   - *Economics ($150 ADR)*: Hotel receives **$117.00 (78.0% net yield)**; OTA commission $27.00 (18%), Virtual Credit Card (VCC) fee $4.50 (3%), Channel Manager $1.50.
   - *Tech*: PMS ➔ 2-way XML (OTA_HotelResNotifRQ) ➔ Booking.com Partner Central ➔ Native App.

4. **Metasearch Referral to Direct Brand.com**:
   - *Flow*: Hotel ➔ Metasearch (Google Hotels) ➔ Brand.com Booking Engine ➔ Guest
   - *Economics ($180 ADR)*: Hotel receives **$158.60 (88.1% net yield)**; Google Hotel Ads CPA $14.40 (8%), Booking engine fee $3.00, Merchant card fee $4.00.
   - *Tech*: CRS ARI Feed ➔ Google Price Match API ➔ Brand.com deep-link ➔ Tokenized Payment Gateway.

5. **Metasearch to OTA to Guest**:
   - *Flow*: Hotel ➔ Channel Manager ➔ OTA ➔ Metasearch (Trivago/Tripadvisor) ➔ Guest
   - *Economics ($160 ADR)*: Hotel receives **$125.90 (78.7% net yield)**; OTA pays $2-$5 CPC to Metasearch from its own 18% commission margin ($28.80).
   - *Tech*: Channel Manager ➔ OTA API ➔ Metasearch Bidding Engine ➔ OTA Landing Page.

6. **Bedbank to Tour Operator Package Holiday**:
   - *Flow*: Hotel ➔ Bedbank ➔ Tour Operator (TUI/Jet2) ➔ Package Tour Guest
   - *Economics ($120 ADR)*: Hotel receives **$90.00 (75.0% net yield)**; Bedbank markup $12.00, Tour Operator margin $18.00.
   - *Tech*: Extranet Contract ➔ Bedbank XML Cache ➔ Dynamic Packaging Engine.

7. **Direct Loyalty Closed User Group (CUG)**:
   - *Flow*: Hotel ➔ CRS ➔ Loyalty Platform (Points + Cash) ➔ Loyalty Power User
   - *Economics ($220 ADR)*: Hotel receives **$188.30 (91.9% net yield)**; Brand loyalty assessment $9.20 (4.5%), CRS fee $3.00, Card fee $4.50.
   - *Tech*: PMS ➔ Enterprise Bus ➔ Loyalty CRM ➔ Native App with BLE Digital Key.

8. **Property Direct / Walk-In**:
   - *Flow*: Hotel ➔ PMS Front Desk ➔ Walk-In Guest
   - *Economics ($160 ADR)*: Hotel receives **$157.10 (98.2% net yield)**; Card-present interchange $2.40 (1.5%), PMS cost $0.50.
   - *Tech*: Cloud PMS ➔ Keycard Encoder ➔ EMV Payment Terminal.

9. **GDS to Online Booking Tool (OBT) Corporate**:
   - *Flow*: Hotel ➔ GDS ➔ Concur / Cytric (OBT) ➔ Corporate Managed Guest
   - *Economics ($250 ADR)*: Hotel receives **$190.50 (90.7% net yield)**; GDS fee $5.00, Concur fee $3.00, TMC fee $7.00, Card fee $4.50.
   - *Tech*: CRS ➔ GDS Rate Access Code ➔ Concur Travel OBT ➔ Duty of Care Platform.

10. **Group & MICE Direct Contracting**:
    - *Flow*: Hotel ➔ Sales & Catering (Delphi) ➔ Corporate Event Planner ➔ Conference Delegate
    - *Economics ($180 ADR)*: Hotel receives **$171.50 (95.3% net yield)**; Sales CRM $2.00, Housing tool $3.00, Billing fee $3.50.
    - *Tech*: Amadeus Delphi.fdc ➔ Cvent Passkey API ➔ PMS Group Master Folio.

---

## Files in `/run/media/ml/Storage/Labs/`

- [`index.html`](file:///run/media/ml/Storage/Labs/index.html): Standalone interactive web dashboard with 5 tabs, responsive design, and Plotly.js/D3.js integration.
- [`css/styles.css`](file:///run/media/ml/Storage/Labs/css/styles.css): Modern financial dark-mode stylesheet with glassmorphism, responsive grids, and animations.
- [`js/app.js`](file:///run/media/ml/Storage/Labs/js/app.js): Application logic, Sankey rendering, waterfall charts, archetype explorer, and what-if sensitivity calculator.
- [`data/hospitality_distribution_data.json`](file:///run/media/ml/Storage/Labs/data/hospitality_distribution_data.json): Complete structured JSON containing all nodes, links, financial values, archetypes, and benchmarks.
- [`data/channel_breakdown.csv`](file:///run/media/ml/Storage/Labs/data/channel_breakdown.csv): Tabular export of all 55 flow links with values and share percentages.
- [`generate_data.py`](file:///run/media/ml/Storage/Labs/generate_data.py): Python generator script used to compute and export the data model.
