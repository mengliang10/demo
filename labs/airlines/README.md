# Airline Distribution Ecosystem & Revenue / Cost Splits

An interactive, multi-tier data visualization dashboard mapping the complete global commercial passenger airline journey, GDS EDIFACT, IATA NDC Direct Connect, Passenger Service Systems (PSS), and aviation financial revenue/cost splits.

---

## Quick Start: Launching the Airline Dashboard

Open [`index.html`](file:///run/media/ml/Storage/Labs/airlines/index.html) in your browser, or launch a local web server:

```bash
cd "/run/media/ml/Storage/Labs/airlines"
python3 -m http.server 8082
```

Then navigate to: **`http://localhost:8082`**

---

## Key Aviation Economic Metrics

The model uses a global commercial passenger airline baseline of **$800.0 Billion USD** in Gross Booking Value (GBV), representing **4.6 Billion passenger departures** globally at a blended fare + ancillary spend of **$173.91** per passenger.

| Metric | Amount ($B) | Share (%) | Aviation Industry Context |
| :--- | :--- | :--- | :--- |
| **Global Airline Passenger GBV** | **$800.0B** | **100.0%** | Total gross passenger airfares ($640B) + ancillaries ($160B) |
| **Base Airfare Revenue** | **$640.0B** | **80.0%** | Base seat transport across legacy, LCC, regional, and charter fleets |
| **Ancillary Revenue** | **$160.0B** | **20.0%** | Baggage fees, seat selection, onboard Wi-Fi, food & co-brand credit cards |
| **Distribution & Intermediary Friction** | **$46.4B** | **5.8%** | GDS segment fees, credit card interchange, TMC overrides, OTA margins |
| **Net Airline Passenger Revenue** | **$753.6B** | **94.2%** | Net passenger revenue retained by commercial airlines |
| **Direct Digital Channel Share** | **$420.0B** | **52.5%** | Airline.com, native mobile apps, and airport check-in kiosks |
| **GDS, NDC & Agency Intermediated** | **$380.0B** | **47.5%** | Corporate TMCs, flight OTAs, travel agencies & consolidators |
| **Airline Operating Expenses (OpEx)** | **$698.0B** | **87.3%** | Jet fuel (28%), flight crew labor (24%), aircraft leases (12%), airport/ATC (9%), MRO (8%) |
| **Operating Profit (EBIT / GOP)** | **$55.6B** | **7.0%** | 7.4% margin on Net Airline Revenue |

---

## 5-Tier Aviation Journey Architecture

1. **Tier 0: Airline Supply ($800.0B)**: Network Legacy Carriers ($480B / 60%), Low-Cost Carriers ($240B / 30%), Regional & Hybrid ($55B / 6.9%), Charter & Private ($25B / 3.1%).
2. **Tier 1: Tech & Distribution Infrastructure ($800.0B)**: Passenger Service Systems / PSS (Altéa, SabreSonic, Navitaire) ($400B), IATA NDC APIs ($180B), GDS EDIFACT Switches ($160B), Direct Web Engines ($60B).
3. **Tier 2: Primary Channels ($800.0B)**: Direct Digital ($420B / 52.5%), GDS EDIFACT ($180B / 22.5%), IATA NDC Direct Connect ($100B / 12.5%), Flight OTAs ($65B / 8.1%), Air Consolidators ($35B / 4.4%).
4. **Tier 3: Intermediaries & Retail Front-Ends ($800.0B)**: Direct Passenger Front-Ends ($420B), Corporate TMCs & OBTs ($175B), OTA Consumer Sites ($125B), Travel Agencies ($45B), Consolidator Brokers ($35B).
5. **Tier 4: Passenger & Demand Segments ($800.0B)**: Leisure Vacationers ($260B / 32.5%), Corporate Managed ($175B / 21.9%), VFR ($140B / 17.5%), Corporate Unmanaged/SME ($105B / 13.1%), Frequent Flyer Elites ($80B / 10.0%), Group & Charters ($40B / 5.0%).
