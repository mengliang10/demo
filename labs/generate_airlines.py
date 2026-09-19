import os, json, csv

air_dir = "/run/media/ml/Storage/Labs/airlines"
os.makedirs(os.path.join(air_dir, "data"), exist_ok=True)
os.makedirs(os.path.join(air_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(air_dir, "js"), exist_ok=True)

metrics = {
    "global_gbv_billions": 800.0,
    "total_distribution_cost_billions": 46.4,
    "net_airline_revenue_billions": 753.6,
    "base_fare_revenue_billions": 640.0,
    "ancillary_revenue_billions": 160.0,
    "direct_share_pct": 52.5,
    "gds_ndc_agency_share_pct": 47.5,
    "blended_distribution_take_rate_pct": 5.8,
    "annual_passengers_billions": 4.6,
    "blended_revenue_per_passenger_usd": 173.91
}

nodes = [
    # Tier 0: Supply (0-3)
    {"id": "sup_legacy", "name": "Network Legacy Carriers", "tier": 0, "category": "Supply", "color": "#3b82f6", "value": 480.0, "desc": "Delta, United, American, Lufthansa, Emirates, Singapore Airlines, BA"},
    {"id": "sup_lcc", "name": "Low-Cost Carriers (LCCs)", "tier": 0, "category": "Supply", "color": "#06b6d4", "value": 240.0, "desc": "Ryanair, Southwest, EasyJet, IndiGo, AirAsia, Spirit, Wizz Air"},
    {"id": "sup_regional", "name": "Regional & Hybrid Airlines", "tier": 0, "category": "Supply", "color": "#8b5cf6", "value": 55.0, "desc": "Alaska Airlines, JetBlue, Azul, SkyWest, Republic Airways"},
    {"id": "sup_charter", "name": "Charter, ACMI & VIP Private", "tier": 0, "category": "Supply", "color": "#10b981", "value": 25.0, "desc": "TUI fly charter, Atlas Air, NetJets, VistaJet, government transports"},

    # Tier 1: Tech & Distribution Infrastructure (4-7)
    {"id": "tech_pss", "name": "Passenger Service Systems (PSS)", "tier": 1, "category": "Tech", "color": "#6366f1", "value": 400.0, "desc": "Amadeus Altéa, SabreSonic, Navitaire, Radixx, Hitit (Inventory & DCS)"},
    {"id": "tech_ndc", "name": "IATA NDC Direct Connect APIs", "tier": 1, "category": "Tech", "color": "#ec4899", "value": 180.0, "desc": "Accelya, Farelogix, Datalex, direct XML/JSON Open APIs bypassing legacy EDIFACT"},
    {"id": "tech_gds", "name": "GDS EDIFACT Core Switches", "tier": 1, "category": "Tech", "color": "#f59e0b", "value": 160.0, "desc": "Sabre, Amadeus, Travelport legacy PNR message switches & ATPCO fare filings"},
    {"id": "tech_direct_web", "name": "Native Web & Mobile Booking Engines", "tier": 1, "category": "Tech", "color": "#14b8a6", "value": 60.0, "desc": "LCC in-house reservation stacks with direct credit card settlement"},

    # Tier 2: Primary Distribution Channels (8-12)
    {"id": "chan_direct_digital", "name": "Direct Airline.com & Mobile App", "tier": 2, "category": "Direct", "color": "#22c55e", "value": 420.0, "desc": "Airline branded websites, mobile apps, airport kiosks, call centers"},
    {"id": "chan_gds_edifact", "name": "Global Distribution Systems (EDIFACT)", "tier": 2, "category": "GDS", "color": "#a855f7", "value": 180.0, "desc": "Traditional GDS terminal distribution (subject to airline GDS surcharges)"},
    {"id": "chan_ndc_api", "name": "IATA NDC Aggregators & Direct APIs", "tier": 2, "category": "NDC", "color": "#f97316", "value": 100.0, "desc": "Modern rich-content NDC feeds with personalized ancillary bundles"},
    {"id": "chan_ota_channel", "name": "Online Travel Agencies (OTAs)", "tier": 2, "category": "OTAs", "color": "#fb923c", "value": 65.0, "desc": "Expedia, Booking.com, Trip.com, eDreams ODIGEO, CheapOair"},
    {"id": "chan_consolidator", "name": "Air Consolidators & Wholesalers", "tier": 2, "category": "Wholesale", "color": "#d946ef", "value": 35.0, "desc": "Mondee, Centrav, Picasso Travel (unpublished net bulk airfares)"},

    # Tier 3: Intermediaries, Retailers & Desks (13-17)
    {"id": "ret_airline_fe", "name": "Direct Passenger Front-Ends", "tier": 3, "category": "Retail", "color": "#16a34a", "value": 420.0, "desc": "Airline.com, mobile app boarding pass wallets, airport check-in desks"},
    {"id": "ret_corp_tmc", "name": "Corporate TMCs & OBTs", "tier": 3, "category": "Corporate", "color": "#9333ea", "value": 175.0, "desc": "Amex GBT, BCD, CWT, Navan, SAP Concur, Cytric, TravelPerk"},
    {"id": "ret_ota_apps", "name": "OTA Consumer Sites & Metas", "tier": 3, "category": "OTA", "color": "#ea580c", "value": 125.0, "desc": "Consumer flight comparison apps, Google Flights & Skyscanner click-throughs"},
    {"id": "ret_trade_agents", "name": "Retail Agencies & Consortia", "tier": 3, "category": "Retail", "color": "#c026d3", "value": 45.0, "desc": "Independent travel agents, Virtuoso luxury advisors, high-street shops"},
    {"id": "ret_wholesale_brokers", "name": "Consolidator Ticket Brokers", "tier": 3, "category": "Brokers", "color": "#db2777", "value": 35.0, "desc": "Ethnic travel agents, sub-agencies booking unpublished net fares"},

    # Tier 4: Passenger & Demand Segments (18-23)
    {"id": "seg_corp_managed", "name": "Corporate Managed Travelers", "tier": 4, "category": "Segments", "color": "#4338ca", "value": 175.0, "desc": "Mandated travel policy, premium cabins, corporate negotiated discounts"},
    {"id": "seg_corp_sme", "name": "Corporate Unmanaged / SME", "tier": 4, "category": "Segments", "color": "#6366f1", "value": 105.0, "desc": "Small business travelers buying flexible economy or premium economy"},
    {"id": "seg_leisure_vacation", "name": "Leisure Vacationers", "tier": 4, "category": "Segments", "color": "#0284c7", "value": 260.0, "desc": "Holidaymakers, resort beach travelers, family vacation flights"},
    {"id": "seg_vfr", "name": "VFR (Visiting Friends & Relatives)", "tier": 4, "category": "Segments", "color": "#06b6d4", "value": 140.0, "desc": "High price elasticity, heavy baggage check-in, seasonal holiday spikes"},
    {"id": "seg_loyalty_elites", "name": "Frequent Flyer Loyalty Elites", "tier": 4, "category": "Segments", "color": "#15803d", "value": 80.0, "desc": "Medallion / Executive Platinum / HON Circle members redeeming miles & upgrades"},
    {"id": "seg_group_charter", "name": "Group, Sports & Charters", "tier": 4, "category": "Segments", "color": "#ca8a04", "value": 40.0, "desc": "Sports teams, concert tour crews, student groups, pilgrimages"}
]

node_indices = {n["id"]: i for i, n in enumerate(nodes)}

links = [
    # Tier 0 -> Tier 1
    {"source": "sup_legacy", "target": "tech_pss", "value": 270.0, "label": "Altéa/SabreSonic core"},
    {"source": "sup_legacy", "target": "tech_ndc", "value": 120.0, "label": "Legacy NDC APIs"},
    {"source": "sup_legacy", "target": "tech_gds", "value": 90.0, "label": "GDS EDIFACT links"},

    {"source": "sup_lcc", "target": "tech_pss", "value": 100.0, "label": "Navitaire LCC PSS"},
    {"source": "sup_lcc", "target": "tech_ndc", "value": 50.0, "label": "LCC direct connect API"},
    {"source": "sup_lcc", "target": "tech_gds", "value": 30.0, "label": "LCC light GDS participation"},
    {"source": "sup_lcc", "target": "tech_direct_web", "value": 60.0, "label": "Pure direct web stack"},

    {"source": "sup_regional", "target": "tech_pss", "value": 20.0, "label": "Regional PSS"},
    {"source": "sup_regional", "target": "tech_ndc", "value": 10.0, "label": "Regional NDC"},
    {"source": "sup_regional", "target": "tech_gds", "value": 25.0, "label": "Major codeshare GDS"},

    {"source": "sup_charter", "target": "tech_pss", "value": 10.0, "label": "Charter booking engine"},
    {"source": "sup_charter", "target": "tech_gds", "value": 15.0, "label": "ACM / Charter GDS"},

    # Tier 1 -> Tier 2
    {"source": "tech_pss", "target": "chan_direct_digital", "value": 280.0, "label": "Airline.com & App booking"},
    {"source": "tech_pss", "target": "chan_gds_edifact", "value": 80.0, "label": "PSS to GDS switch"},
    {"source": "tech_pss", "target": "chan_ota_channel", "value": 25.0, "label": "OTA direct connect"},
    {"source": "tech_pss", "target": "chan_consolidator", "value": 15.0, "label": "Bulk net fare desk"},

    {"source": "tech_ndc", "target": "chan_ndc_api", "value": 100.0, "label": "IATA NDC 21.3 standard API"},
    {"source": "tech_ndc", "target": "chan_direct_digital", "value": 80.0, "label": "NDC dynamic packaging"},

    {"source": "tech_gds", "target": "chan_gds_edifact", "value": 100.0, "label": "Sabre/Amadeus EDIFACT"},
    {"source": "tech_gds", "target": "chan_ota_channel", "value": 40.0, "label": "OTA GDS booking"},
    {"source": "tech_gds", "target": "chan_consolidator", "value": 20.0, "label": "Consolidator GDS queue"},

    {"source": "tech_direct_web", "target": "chan_direct_digital", "value": 60.0, "label": "Ryanair/Southwest direct"},

    # Tier 2 -> Tier 3
    {"source": "chan_direct_digital", "target": "ret_airline_fe", "value": 420.0, "label": "Direct consumer portal"},
    {"source": "chan_gds_edifact", "target": "ret_corp_tmc", "value": 115.0, "label": "GDS to TMCs"},
    {"source": "chan_gds_edifact", "target": "ret_trade_agents", "value": 35.0, "label": "Traditional agents GDS"},
    {"source": "chan_gds_edifact", "target": "ret_ota_apps", "value": 30.0, "label": "OTA GDS fulfillment"},

    {"source": "chan_ndc_api", "target": "ret_corp_tmc", "value": 60.0, "label": "NDC to Concur/Navan"},
    {"source": "chan_ndc_api", "target": "ret_ota_apps", "value": 30.0, "label": "NDC to Skyscanner/Kayak"},
    {"source": "chan_ndc_api", "target": "ret_trade_agents", "value": 10.0, "label": "Agent NDC portals"},

    {"source": "chan_ota_channel", "target": "ret_ota_apps", "value": 65.0, "label": "Expedia/Booking OTA apps"},

    {"source": "chan_consolidator", "target": "ret_wholesale_brokers", "value": 35.0, "label": "Wholesale consolidator"},

    # Tier 3 -> Tier 4
    {"source": "ret_airline_fe", "target": "seg_leisure_vacation", "value": 160.0, "label": "Direct leisure flights"},
    {"source": "ret_airline_fe", "target": "seg_corp_sme", "value": 75.0, "label": "SME direct booking"},
    {"source": "ret_airline_fe", "target": "seg_loyalty_elites", "value": 80.0, "label": "Frequent flyer award flights"},
    {"source": "ret_airline_fe", "target": "seg_vfr", "value": 80.0, "label": "Direct VFR travelers"},
    {"source": "ret_airline_fe", "target": "seg_group_charter", "value": 25.0, "label": "Direct group sales"},

    {"source": "ret_corp_tmc", "target": "seg_corp_managed", "value": 160.0, "label": "Corporate managed policy"},
    {"source": "ret_corp_tmc", "target": "seg_corp_sme", "value": 15.0, "label": "SME business travel"},

    {"source": "ret_ota_apps", "target": "seg_leisure_vacation", "value": 80.0, "label": "OTA leisure booking"},
    {"source": "ret_ota_apps", "target": "seg_vfr", "value": 30.0, "label": "OTA price comparison"},
    {"source": "ret_ota_apps", "target": "seg_corp_sme", "value": 15.0, "label": "Unmanaged business"},

    {"source": "ret_trade_agents", "target": "seg_corp_managed", "value": 15.0, "label": "Executive travel"},
    {"source": "ret_trade_agents", "target": "seg_leisure_vacation", "value": 20.0, "label": "Package holidays"},
    {"source": "ret_trade_agents", "target": "seg_group_charter", "value": 10.0, "label": "Tour groups"},

    {"source": "ret_wholesale_brokers", "target": "seg_vfr", "value": 30.0, "label": "Ethnic VFR consolidator"},
    {"source": "ret_wholesale_brokers", "target": "seg_group_charter", "value": 5.0, "label": "Pilgrimage groups"}
]

sankey_links = []
for l in links:
    sankey_links.append({
        "source": node_indices[l["source"]],
        "target": node_indices[l["target"]],
        "value": l["value"],
        "source_id": l["source"],
        "target_id": l["target"],
        "label": l["label"]
    })

revenue_cost_split = {
    "gross_booking_value": 800.0,
    "intermediary_friction": [
        {"item": "Credit Card Merchant Interchange", "amount": 18.0, "pct_of_gbv": 2.25, "rate_pct": "2.25% blended", "desc": "Card-not-present acquiring fees on high-ticket airline tickets"},
        {"item": "GDS Segment & Booking Fees", "amount": 7.2, "pct_of_gbv": 0.90, "rate_pct": "$4.50-$8.50/segment", "desc": "Amadeus, Sabre, Travelport legacy EDIFACT booking fees"},
        {"item": "TMC Corporate Overrides & Incentives", "amount": 6.4, "pct_of_gbv": 0.80, "rate_pct": "3.5% blended", "desc": "Volume kickbacks and corporate account performance bonuses"},
        {"item": "OTA Commissions & Markup Deductions", "amount": 5.8, "pct_of_gbv": 0.72, "rate_pct": "7-12% blended", "desc": "Expedia, Booking.com, eDreams commissions on international/LCC"},
        {"item": "Metasearch Referral Ad Spend (CPC)", "amount": 4.8, "pct_of_gbv": 0.60, "rate_pct": "$1.50-$4.00/click", "desc": "Google Flights & Skyscanner cost-per-click traffic acquisition"},
        {"item": "PSS & NDC Tech SaaS Fees", "amount": 4.2, "pct_of_gbv": 0.53, "rate_pct": "$0.90/pax", "desc": "Altéa/SabreSonic PSS hosting and NDC API transaction fees"}
    ],
    "net_airline_revenue": 753.6,
    "airline_operating_costs": [
        {"item": "Aviation Jet Fuel (A1 / SAF)", "amount": 224.0, "pct_of_net": 29.7, "desc": "Volatile kerosene jet fuel and sustainable aviation fuel mandates"},
        {"item": "Flight & Cabin Crew & Tech Labor", "amount": 192.0, "pct_of_net": 25.5, "desc": "Pilots, flight attendants, maintenance engineers, dispatchers"},
        {"item": "Aircraft Ownership, Lease & Depreciation", "amount": 96.0, "pct_of_net": 12.7, "desc": "Operating leases (Aercap, SMBC), Boeing/Airbus debt service"},
        {"item": "Airport Landing, Security & ATC Charges", "amount": 72.0, "pct_of_net": 9.5, "desc": "Runway landing fees, Eurocontrol/FAA air navigation, terminal slots"},
        {"item": "Maintenance, Repair & Overhaul (MRO)", "amount": 64.0, "pct_of_net": 8.5, "desc": "CFM/Pratt/Rolls engine overhauls, C-checks, avionics upgrades"},
        {"item": "In-Flight Catering & Passenger Amenities", "amount": 24.0, "pct_of_net": 3.2, "desc": "Catering (Gate Gourmet, LSG Sky Chefs), IFE content licensing"},
        {"item": "Selling, Marketing & Corporate G&A", "amount": 26.0, "pct_of_net": 3.4, "desc": "Global advertising, loyalty program management, executive overhead"}
    ],
    "operating_profit_ebit": 55.6,
    "ebit_margin_pct_of_net": 7.38,
    "ebit_margin_pct_of_gbv": 6.95
}

journey_archetypes = [
    {
        "id": "air_path_1",
        "title": "Corporate Managed GDS Journey",
        "formula": "Airline ➔ PSS (Altéa) ➔ GDS (Sabre) ➔ Corporate TMC (Amex GBT) ➔ Concur OBT ➔ Corporate Executive",
        "category": "Corporate Legacy GDS",
        "ticket_example": 650.0,
        "ancillary_example": 50.0,
        "steps": [
            {"node": "Airline Supply", "entity": "Network Flag Carrier (Delta/Lufthansa)", "role": "Publishes $650 corporate fare with flexible change rules", "cost": 0.0, "retained": 700.0},
            {"node": "Passenger Service System", "entity": "Amadeus Altéa / SabreSonic", "role": "Validates inventory availability and ticket ticketing limits", "cost": 1.5, "retained": 698.5},
            {"node": "GDS EDIFACT Switch", "entity": "Sabre / Amadeus GDS", "role": "Processes 2 flight segments, charges airline $15 GDS fee (kicks back $4 to TMC)", "cost": 15.0, "retained": 683.5},
            {"node": "Corporate TMC & OBT", "entity": "Amex GBT / SAP Concur", "role": "Enforces corporate travel policy, books negotiated discount", "cost": 8.0, "retained": 675.5},
            {"node": "Corporate Traveler", "entity": "Business Executive", "role": "Flies business class / flexible economy, buys Wi-Fi ($50)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 700.0,
            "base_fare": 650.0,
            "ancillary": 50.0,
            "gds_fee": 15.0,
            "tmc_incentive": 8.0,
            "credit_card_fee": 15.4,
            "airline_net_received": 660.1,
            "distribution_friction_pct": 5.7,
            "net_yield_pct": 94.3
        },
        "tech_stack": "Altéa PSS ➔ ATPCO Fares ➔ Sabre EDIFACT ➔ Concur Travel OBT API",
        "key_characteristics": "High yield ($700+ fare); high GDS transaction cost; GDS kickbacks fund TMC corporate rebates."
    },
    {
        "id": "air_path_2",
        "title": "IATA NDC Direct Connect Corporate",
        "formula": "Airline ➔ NDC API Gateway ➔ Corporate OBT (Navan / Concur) ➔ Corporate Traveler",
        "category": "Modern NDC Direct Connect",
        "ticket_example": 450.0,
        "ancillary_example": 60.0,
        "steps": [
            {"node": "Airline Supply", "entity": "American / British Airways", "role": "Offers continuous pricing NDC fare (exempt from $21 GDS EDIFACT surcharge)", "cost": 0.0, "retained": 510.0},
            {"node": "NDC API Hub", "entity": "Accelya / Farelogix", "role": "Delivers personalized bundle (Seat + Checked Bag + Wi-Fi) via JSON API", "cost": 2.5, "retained": 507.5},
            {"node": "Modern OBT / TMC", "entity": "Navan / TravelPerk", "role": "Presents rich seat map and bundled fare inside mobile app", "cost": 5.0, "retained": 502.5},
            {"node": "Corporate Traveler", "entity": "Tech Consultant", "role": "Selects extra-legroom seat bundle directly via NDC", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 510.0,
            "ndc_tech_fee": 2.5,
            "tmc_tech_fee": 5.0,
            "credit_card_fee": 11.2,
            "airline_net_received": 491.3,
            "distribution_friction_pct": 3.7,
            "net_yield_pct": 96.3
        },
        "tech_stack": "IATA NDC 21.3 XML/JSON ➔ ONE Order Engine ➔ Dynamic Offer Creation Platform",
        "key_characteristics": "Bypasses legacy GDS fees; allows dynamic continuous pricing; enables rich graphical seat and meal merchandising."
    },
    {
        "id": "air_path_3",
        "title": "Ultra-Low-Cost Carrier Pure Direct App",
        "formula": "LCC Supply ➔ In-House Reservation Engine ➔ Native Mobile App ➔ Budget Vacationer",
        "category": "LCC Pure Direct & Unbundled",
        "ticket_example": 49.0,
        "ancillary_example": 85.0,
        "steps": [
            {"node": "LCC Airline Supply", "entity": "Ryanair / Spirit Airlines", "role": "Unbundled base seat priced at bare minimum ($49)", "cost": 0.0, "retained": 134.0},
            {"node": "Proprietary Booking Stack", "entity": "Navitaire / In-House Cloud", "role": "Optimized ancillary checkout flow with aggressive upselling", "cost": 0.8, "retained": 133.2},
            {"node": "Direct Mobile App", "entity": "Ryanair App / Spirit.com", "role": "Passenger adds carry-on bag ($35), seat pick ($15), priority boarding ($20), insurance ($15)", "cost": 0.0, "retained": 133.2},
            {"node": "Budget Vacationer", "entity": "Price-Conscious Traveler", "role": "Pays $49 ticket + $85 ancillaries = $134 total (Ancillaries > Base Fare!)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 134.0,
            "base_fare": 49.0,
            "ancillary_revenue": 85.0,
            "tech_cost": 0.8,
            "credit_card_fee": 2.9,
            "airline_net_received": 130.3,
            "distribution_friction_pct": 2.8,
            "net_yield_pct": 97.2
        },
        "tech_stack": "Proprietary Cloud PSS ➔ Direct Payment Gateway ➔ Native Mobile App with QR Boarding Pass",
        "key_characteristics": "Ancillary revenue exceeds base ticket price (63% of total spend!); 0% GDS dependency; lowest distribution cost in aviation (<3%)."
    },
    {
        "id": "air_path_4",
        "title": "Metasearch Referral to Airline.com",
        "formula": "Airline ➔ Google Flights / Skyscanner ➔ Airline.com Booking Engine ➔ Leisure Passenger",
        "category": "Metasearch Direct Acquisition",
        "ticket_example": 280.0,
        "ancillary_example": 45.0,
        "steps": [
            {"node": "Airline Supply", "entity": "United / Lufthansa", "role": "Provides live QPX / real-time fare cache to Google Flights", "cost": 0.0, "retained": 325.0},
            {"node": "Metasearch Engine", "entity": "Google Flights / Skyscanner", "role": "Compares flight schedules, deep-links user to Airline.com (charges CPC $2.50)", "cost": 2.5, "retained": 322.5},
            {"node": "Airline.com Checkout", "entity": "Airline Direct Web Engine", "role": "Captures direct customer data, upsells Economy Plus seat", "cost": 1.2, "retained": 321.3},
            {"node": "Leisure Passenger", "entity": "Independent Tourist", "role": "Completes booking directly on airline site", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 325.0,
            "google_flights_cpc": 2.5,
            "booking_engine_cost": 1.2,
            "credit_card_fee": 7.15,
            "airline_net_received": 314.15,
            "distribution_friction_pct": 3.3,
            "net_yield_pct": 96.7
        },
        "tech_stack": "Google ITA QPX Engine ➔ Deep-Linking API ➔ Airline Direct NDC/PSS Checkout",
        "key_characteristics": "Bypasses OTA commissions; low acquisition cost ($2.50 CPC); airline retains full passenger contact info for re-marketing."
    },
    {
        "id": "air_path_5",
        "title": "OTA Dynamic Flight + Hotel Packaging",
        "formula": "Airline ➔ GDS / NDC ➔ Mega-OTA (Expedia) ➔ Package Holidaymaker",
        "category": "OTA Bundled Leisure",
        "ticket_example": 320.0,
        "ancillary_example": 30.0,
        "steps": [
            {"node": "Airline Supply", "entity": "Legacy International Carrier", "role": "Provides opaque package airfare discount ($290 vs $320 retail)", "cost": 0.0, "retained": 350.0},
            {"node": "GDS / NDC Pipe", "entity": "Amadeus GDS / Expedia Direct Connect", "role": "Streams flight schedules into Expedia packaging engine", "cost": 8.0, "retained": 342.0},
            {"node": "Mega-OTA", "entity": "Expedia Group / Booking.com", "role": "Bundles flight with 5-night hotel, takes 8% commission on air portion", "cost": 25.6, "retained": 316.4},
            {"node": "Package Holidaymaker", "entity": "Vacationer", "role": "Buys bundled flight + hotel trip (airfare price opaque)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 350.0,
            "ota_commission": 25.6,
            "gds_fee": 8.0,
            "merchant_fee": 7.7,
            "airline_net_received": 308.7,
            "distribution_friction_pct": 11.8,
            "net_yield_pct": 88.2
        },
        "tech_stack": "Amadeus Web Services ➔ Expedia Packaging Algorithm ➔ Virtual Credit Card Settlement",
        "key_characteristics": "Opaque airfare protects published fare integrity; higher distribution friction (11.8%) due to OTA margin + GDS fee."
    },
    {
        "id": "air_path_6",
        "title": "Air Consolidator Unpublished Net Fare",
        "formula": "Airline ➔ Air Consolidator (Mondee) ➔ Ethnic Sub-Agent ➔ VFR Traveler",
        "category": "Wholesale Net Consolidator",
        "ticket_example": 750.0,
        "ancillary_example": 0.0,
        "steps": [
            {"node": "Airline Fleet", "entity": "Transpacific / Transatlantic Carrier", "role": "Releases unsold long-haul seats to consolidator at $620 net rate", "cost": 0.0, "retained": 750.0},
            {"node": "Air Consolidator", "entity": "Mondee / Centrav", "role": "Distributes unpublished net fare to network of ethnic travel agencies", "cost": 50.0, "retained": 700.0},
            {"node": "Ethnic Travel Agency", "entity": "Community Travel Specialist", "role": "Marks up net fare by $80, sells ticket for $750 with 2 free checked bags", "cost": 80.0, "retained": 620.0},
            {"node": "VFR Traveler", "entity": "Visiting Family Abroad", "role": "Pays cash/card to local agent for international holiday flight", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 750.0,
            "consolidator_markup": 50.0,
            "agent_markup": 80.0,
            "clearing_fee": 5.0,
            "airline_net_received": 615.0,
            "distribution_friction_pct": 18.0,
            "net_yield_pct": 82.0
        },
        "tech_stack": "Consolidator Private Extranet ➔ ARC / IATA BSP Net Fare Ticketing ➔ Sub-Agent Portal",
        "key_characteristics": "Fills back-of-plane seats on long-haul routes; completely invisible to open web scrapers; high baggage allowance demand."
    },
    {
        "id": "air_path_7",
        "title": "Frequent Flyer Loyalty Award Redemption",
        "formula": "Airline Loyalty Program ➔ Member Portal / App ➔ Frequent Flyer Elite",
        "category": "Loyalty Program & Miles",
        "ticket_example": 400.0,
        "ancillary_example": 35.0,
        "steps": [
            {"node": "Airline Operations", "entity": "Major Alliance Carrier", "role": "Releases Saver Award seat for 25,000 miles + $5.60 TSA tax", "cost": 0.0, "retained": 435.0},
            {"node": "Loyalty Program Treasury", "entity": "SkyMiles / MileagePlus Treasury", "role": "Reimburses flight operations department at internal transfer rate ($0.012/mile = $300)", "cost": 0.0, "retained": 300.0},
            {"node": "Loyalty Member", "entity": "Elite Status Flyer", "role": "Redeems miles earned via co-branded Amex/Chase credit card", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "imputed_ticket_value": 400.0,
            "miles_reimbursement": 300.0,
            "cash_tax_paid": 5.6,
            "internal_processing_cost": 2.0,
            "airline_net_received": 303.6,
            "distribution_friction_pct": 0.5,
            "net_yield_pct": 99.5
        },
        "tech_stack": "Loyalty Ledger ➔ PSS Award Seat Inventory Engine ➔ Native Mobile App",
        "key_characteristics": "The most profitable part of modern airlines (co-brand bank mileage sales generate billions in upfront cash with near-zero marginal seat cost)."
    },
    {
        "id": "air_path_8",
        "title": "Traditional Travel Agency First Class Journey",
        "formula": "Airline ➔ GDS ➔ Virtuoso Luxury Agent ➔ Premium International Passenger",
        "category": "High-Yield First Class",
        "ticket_example": 5500.0,
        "ancillary_example": 0.0,
        "steps": [
            {"node": "Airline Fleet", "entity": "Emirates / Singapore Airlines", "role": "Publishes $5,500 First Class Suite round-trip", "cost": 0.0, "retained": 5500.0},
            {"node": "GDS Terminal", "entity": "Amadeus Selling Platform", "role": "Luxury agent books specific seat suite 1A and orders special champagne", "cost": 20.0, "retained": 5480.0},
            {"node": "Luxury Travel Advisor", "entity": "Virtuoso Air Specialist", "role": "Manages chauffeur transfers, receives 7% agency commission ($385)", "cost": 385.0, "retained": 5095.0},
            {"node": "First Class Traveler", "entity": "High-Net-Worth Individual", "role": "Flies long-haul luxury suite", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 5500.0,
            "advisor_commission": 385.0,
            "gds_fee": 20.0,
            "card_processing": 110.0,
            "airline_net_received": 4985.0,
            "distribution_friction_pct": 9.4,
            "net_yield_pct": 90.6
        },
        "tech_stack": "Amadeus Selling Platform Connect ➔ PSS First Class Inventory ➔ Chauffeur Dispatch API",
        "key_characteristics": "Tremendous absolute profit per passenger ($4,985 net); requires white-glove VIP disruption handling."
    },
    {
        "id": "air_path_9",
        "title": "Airport Ticket Desk Distress / Standby",
        "formula": "Airline Station ➔ Airport Departure Control System (DCS) ➔ Same-Day Walk-Up Passenger",
        "category": "Airport Counter Direct",
        "ticket_example": 420.0,
        "ancillary_example": 40.0,
        "steps": [
            {"node": "Airport Ticket Counter", "entity": "Hub Airport Gate / Ticket Desk", "role": "Same-day walk-up passenger needs immediate flight due to family emergency", "cost": 0.0, "retained": 460.0},
            {"node": "Departure Control System", "entity": "Altéa DCS / Sabre Airport Services", "role": "Agent issues immediate electronic ticket and printed boarding pass", "cost": 1.0, "retained": 459.0},
            {"node": "Airport EMV Terminal", "entity": "Verifone Card Terminal", "role": "Card-present chip transaction (1.6% interchange)", "cost": 7.36, "retained": 451.64},
            {"node": "Walk-Up Passenger", "entity": "Emergency Traveler", "role": "Boards flight departing in 45 minutes", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 460.0,
            "dcs_transaction_cost": 1.0,
            "card_present_interchange": 7.36,
            "airline_net_received": 451.64,
            "distribution_friction_pct": 1.8,
            "net_yield_pct": 98.2
        },
        "tech_stack": "DCS Check-in Terminal ➔ ATB Boarding Pass Printer ➔ EMV Chip Terminal",
        "key_characteristics": "Highest price per seat (Y-class full fare); zero third-party commission; lowest payment friction (card present)."
    },
    {
        "id": "air_path_10",
        "title": "Sports Team & Corporate Full Charter",
        "formula": "Airline Charter Division ➔ Enterprise Charter Desk ➔ Sports Franchise / Tour Group",
        "category": "Private Aviation & Group",
        "ticket_example": 120000.0,
        "ancillary_example": 15000.0,
        "steps": [
            {"node": "Airline Fleet", "entity": "Delta / United Charter Operations", "role": "Dedicated Boeing 757 VIP-configured charter for professional sports team", "cost": 0.0, "retained": 135000.0},
            {"node": "Charter Contracts Team", "entity": "Airline Special Flights Division", "role": "Negotiates season-long 25-city charter contract with custom catering", "cost": 1500.0, "retained": 133500.0},
            {"node": "Sports Franchise", "entity": "Major League Sports Team", "role": "Pays $135,000 per flight leg via bank wire (0% card fees!)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_spend": 135000.0,
            "contract_admin_cost": 1500.0,
            "bank_wire_fee": 35.0,
            "airline_net_received": 133465.0,
            "distribution_friction_pct": 1.1,
            "net_yield_pct": 98.9
        },
        "tech_stack": "FOS Flight Operations System ➔ Custom Charter Manifest Engine ➔ FBO Ground Handling",
        "key_characteristics": "Near-zero distribution friction (1.1%); 100% upfront payment via wire; utilizes aircraft during off-peak scheduling windows."
    }
]

benchmarks = [
    {
        "type": "Airline Direct Web & App",
        "key_players": "Delta.com, Ryanair App, United.com",
        "take_rate_pct": "2% - 3% (card & tech)",
        "channel_share_pct": "52.5%",
        "cancellation_rate_pct": "3% - 6%",
        "lead_time_days": "25 - 45 days",
        "guest_data_ownership": "100% Owned by Airline",
        "pros": "Lowest cost, highest ancillary conversion (seats, bags, Wi-Fi), direct loyalty capture",
        "cons": "Requires heavy ongoing digital ad spend and continuous mobile app R&D"
    },
    {
        "type": "IATA NDC Direct Connect",
        "key_players": "Accelya, Farelogix, Navan, Concur",
        "take_rate_pct": "3% - 5% blended",
        "channel_share_pct": "12.5%",
        "cancellation_rate_pct": "5% - 8%",
        "lead_time_days": "18 - 30 days",
        "guest_data_ownership": "Full Traveler Data",
        "pros": "Exempt from GDS surcharges, continuous dynamic pricing, rich media seat maps",
        "cons": "Fragmented airline API implementations, ongoing integration maintenance"
    },
    {
        "type": "Global Distribution Systems (GDS)",
        "key_players": "Amadeus, Sabre, Travelport",
        "take_rate_pct": "$4.50 - $8.50 / segment",
        "channel_share_pct": "22.5%",
        "cancellation_rate_pct": "10% - 15%",
        "lead_time_days": "12 - 20 days",
        "guest_data_ownership": "PNR Shared with Agency",
        "pros": "Indispensable access to high-yield managed corporate travel accounts",
        "cons": "High segment fees, rigid legacy EDIFACT constraints, lack of ancillary retailing"
    },
    {
        "type": "Online Travel Agencies (OTAs)",
        "key_players": "Expedia, Booking.com, eDreams, Trip.com",
        "take_rate_pct": "6% - 12% blended",
        "channel_share_pct": "8.1%",
        "cancellation_rate_pct": "12% - 18%",
        "lead_time_days": "30 - 60 days",
        "guest_data_ownership": "Masked Email",
        "pros": "Captures international leisure travelers and multi-airline dynamic packaging",
        "cons": "Masked customer data, complex schedule change communication, chargeback exposure"
    },
    {
        "type": "Air Consolidators & Net Fares",
        "key_players": "Mondee, Centrav, Picasso Travel",
        "take_rate_pct": "12% - 18% markup",
        "channel_share_pct": "4.4%",
        "cancellation_rate_pct": "4% - 6%",
        "lead_time_days": "45 - 90 days",
        "guest_data_ownership": "Consolidator Ticket Record",
        "pros": "Monetizes hard-to-fill long-haul economy seats without breaking public fare rules",
        "cons": "High revenue haircut (15-20% below retail), manual ticketing workflows"
    }
]

output_data = {
    "airline_metrics": metrics,
    "nodes": nodes,
    "links": sankey_links,
    "revenue_cost_split": revenue_cost_split,
    "journey_archetypes": journey_archetypes,
    "intermediary_benchmarks": benchmarks
}

with open(os.path.join(air_dir, "data", "airline_distribution_data.json"), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

with open(os.path.join(air_dir, "data", "channel_breakdown.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Source Node", "Target Node", "Value ($ Billions)", "Share of Global GBV (%)", "Flow Description"])
    for l in sankey_links:
        src_name = nodes[l["source"]]["name"]
        tgt_name = nodes[l["target"]]["name"]
        val = l["value"]
        pct = round((val / 800.0) * 100, 2)
        writer.writerow([src_name, tgt_name, val, f"{pct}%", l["label"]])

print("Airline data generated successfully!")
