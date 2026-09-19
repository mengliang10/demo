# Cruise Distribution Ecosystem & Revenue / Cost Splits

An interactive, multi-tier data visualization dashboard mapping the complete global cruise passenger journey, travel trade intermediaries, onboard spending mechanics, and maritime financial revenue/cost splits.

---

## Quick Start: Launching the Cruise Dashboard

Open [`index.html`](file:///run/media/ml/Storage/Labs/cruises/index.html) in your browser, or launch a local web server:

```bash
cd "/run/media/ml/Storage/Labs/cruises"
python3 -m http.server 8081
```

Then navigate to: **`http://localhost:8081`**

---

## Key Maritime & Cruise Economic Metrics

The model uses a global cruise baseline of **$38.0 Billion USD** in total gross passenger value, representing **33.5 Million cruise passengers** globally at a blended ticket + onboard spend of **$1,134.33** per passenger.

| Metric | Amount ($B) | Share (%) | Maritime Industry Context |
| :--- | :--- | :--- | :--- |
| **Global Cruise Gross Booking Value (GBV)** | **$38.0B** | **100.0%** | Total ticket fares ($25.0B) + onboard spend ($13.0B) |
| **Ticket Revenue** | **$25.0B** | **65.8%** | Base stateroom passage (subject to agency commission) |
| **Onboard Ancillary Revenue** | **$13.0B** | **34.2%** | Casino, beverage packages, dining, shore excursions (0% trade commission!) |
| **Trade & Distribution Cost** | **$4.75B** | **12.5%** | Agency commissions, OTA margins, consortia overrides, tech fees |
| **Net Cruise Line Revenue** | **$33.25B** | **87.5%** | Net retained by cruise lines |
| **Agency / Trade Intermediated Share** | **$29.0B** | **76.3%** | Cruises are the most agency-dominated sector in travel |
| **Direct Booking Share** | **$9.0B** | **23.7%** | Brand.com, mobile apps, and outbound PVP call centers |
| **Ship Operating Costs** | **$23.10B** | **60.8%** | Crew payroll, marine fuel, F&B provisions, port dues, drydocks |
| **Cruise EBITDA (Gross Operating Profit)** | **$10.15B** | **26.7%** | 30.5% margin on Net Cruise Revenue |

---

## Cruise 5-Tier Journey Architecture

1. **Tier 0: Cruise Fleet Supply ($38.0B)**: Mega-Ship Contemporary ($24.0B), Premium & Mid-Size ($8.5B), Luxury & Ultra-Luxury ($3.5B), Expedition & River ($2.0B).
2. **Tier 1: Tech & Reservation Infrastructure ($38.0B)**: Brand Reservation Engines (Polar, Espresso, BookSafe) ($21.0B), Cruise B2B Switches (Amadeus Cruise, Revelex, Versonix) ($12.0B), Onboard Future Cruise Desks ($3.5B), Charter Engines ($1.5B).
3. **Tier 2: Primary Channels ($38.0B)**: Travel Advisors & Host Agencies ($13.5B), Cruise Specialist OTAs ($7.0B), Direct Brand.com & PVP ($9.0B), Big Box Retailers ($3.5B), Luxury Consortia ($3.0B), Charters & MICE ($2.0B).
4. **Tier 3: Advisory & Booking Desks ($38.0B)**: Home-Based Advisors, OTA Call Centers, Brand Direct Desks, Club Travel Desks, Luxury Advisors, Corporate Organizers.
5. **Tier 4: Passenger Segments ($38.0B)**: Family & Multigen ($13.0B / 34.2%), Mature & Retiree ($10.5B / 27.6%), Luxury & World Cruisers ($4.5B / 11.8%), Couples & Honeymooners ($4.0B / 10.5%), Expedition Explorers ($3.0B / 7.9%), Corporate MICE ($2.0B / 5.3%), Solo Cruisers ($1.0B / 2.6%).
