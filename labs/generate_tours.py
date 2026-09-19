import os, json, csv

tours_dir = "/run/media/ml/Storage/Labs/tours"
os.makedirs(os.path.join(tours_dir, "data"), exist_ok=True)
os.makedirs(os.path.join(tours_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(tours_dir, "js"), exist_ok=True)

metrics = {
    "global_gbv_billions": 160.0,
    "total_distribution_cost_billions": 27.4,
    "net_operator_revenue_billions": 132.6,
    "direct_share_pct": 56.3,
    "ota_trade_share_pct": 43.7,
    "blended_distribution_take_rate_pct": 17.13,
    "annual_bookings_billions": 1.4,
    "blended_spend_per_booking_usd": 114.28
}

nodes = [
    # Tier 0: Supply (0-3)
    {"id": "sup_attractions", "name": "Iconic Attractions & Theme Parks", "tier": 0, "category": "Supply", "color": "#3b82f6", "value": 55.0, "desc": "Disneyland, Universal, Louvre, Colosseum, Empire State Building, observation wheels"},
    {"id": "sup_day_tours", "name": "Independent Day Tour Operators", "tier": 0, "category": "Supply", "color": "#06b6d4", "value": 60.0, "desc": "Walking tours, boat charters, food tasting tours, city sightseeing hop-on buses"},
    {"id": "sup_adventure", "name": "Outdoor, Adventure & Sports", "tier": 0, "category": "Supply", "color": "#8b5cf6", "value": 25.0, "desc": "Scuba diving, zip-lining, skydiving, rafting, ski lift tickets, surf lessons"},
    {"id": "sup_multiday", "name": "Multi-Day Guided Expeditions", "tier": 0, "category": "Supply", "color": "#10b981", "value": 20.0, "desc": "Intrepid Travel, G Adventures, Trafalgar, safari camps, Arctic expeditions"},

    # Tier 1: Tech & ResTech Infrastructure (4-7)
    {"id": "tech_restech", "name": "Cloud ResTech Platforms", "tier": 1, "category": "Tech", "color": "#6366f1", "value": 75.0, "desc": "FareHarbor (Booking Holdings), Bókun (Tripadvisor), Peek Pro, Rezdy, Xola, TrekkSoft"},
    {"id": "tech_turnstile", "name": "Turnstile & Enterprise Ticketing", "tier": 1, "category": "Tech", "color": "#ec4899", "value": 45.0, "desc": "Roller, Gateway Ticketing, Accesso, Vivaticket (automated gates & RFID barcode scanners)"},
    {"id": "tech_offline_pos", "name": "Offline POS / Cash Register", "tier": 1, "category": "Tech", "color": "#f59e0b", "value": 25.0, "desc": "Manual paper ticket pads, cash boxes, standalone credit card terminals at ticket booths"},
    {"id": "tech_dmc_erp", "name": "Tour Operator ERP & Inbound PSS", "tier": 1, "category": "Tech", "color": "#14b8a6", "value": 15.0, "desc": "Tourplan, Lemax, Dolphin, custom DMC reservation engines for group manifests"},

    # Tier 2: Primary Channels (8-13)
    {"id": "chan_offline_direct", "name": "Direct Offline Ticket Booth & Walk-Up", "tier": 2, "category": "Direct", "color": "#eab308", "value": 50.0, "desc": "Physical ticket counters, attraction turnstiles, harbour pier walk-up sales"},
    {"id": "chan_online_direct", "name": "Direct Website & Mobile Booking", "tier": 2, "category": "Direct", "color": "#22c55e", "value": 40.0, "desc": "Operator's direct website powered by ResTech embedded booking widget / app"},
    {"id": "chan_experience_ota", "name": "Experience Mega-OTAs", "tier": 2, "category": "OTA", "color": "#f97316", "value": 38.0, "desc": "Viator (Tripadvisor), GetYourGuide, Klook, Tiqets, Musement (TUI), Headout"},
    {"id": "chan_cruise_shorex", "name": "Cruise Line Shore Excursions", "tier": 2, "category": "Shorex", "color": "#a855f7", "value": 12.0, "desc": "Shorex desks on cruise ships selling port tours with 40-100% markups"},
    {"id": "chan_inbound_dmc", "name": "Inbound DMCs & Receptive Operators", "tier": 2, "category": "Wholesale", "color": "#d946ef", "value": 12.0, "desc": "Destination Management Companies contracting group packages for international tour groups"},
    {"id": "chan_concierge", "name": "Hotel Concierge & In-Room QR", "tier": 2, "category": "Local", "color": "#c026d3", "value": 8.0, "desc": "Hotel concierges, front desk recommendations, in-room tablet & TV excursion booking"},

    # Tier 3: Intermediaries & Front-Ends (14-19)
    {"id": "ret_box_office", "name": "On-Site Box Office & Gates", "tier": 3, "category": "Front-End", "color": "#ca8a04", "value": 50.0, "desc": "Physical turnstile scanning, queue ticketing, cash/card payment"},
    {"id": "ret_direct_widgets", "name": "ResTech Web Checkouts", "tier": 3, "category": "Front-End", "color": "#16a34a", "value": 40.0, "desc": "Mobile-optimized booking widget with real-time calendar & waiver signing"},
    {"id": "ret_ota_marketplaces", "name": "OTA Consumer Marketplaces", "tier": 3, "category": "Front-End", "color": "#ea580c", "value": 38.0, "desc": "Viator & GetYourGuide mobile apps with instant digital barcode vouchers"},
    {"id": "ret_shorex_desks", "name": "Cruise Shorex Desks & Port Teams", "tier": 3, "category": "Front-End", "color": "#9333ea", "value": 12.0, "desc": "Shipboard shore excursion consultants, pier dispatch coordinators"},
    {"id": "ret_dmc_portals", "name": "DMC Tour Wholesale Desks", "tier": 3, "category": "Front-End", "color": "#db2777", "value": 12.0, "desc": "B2B package tour dispatchers managing private coaches and multilingual guides"},
    {"id": "ret_concierge_desks", "name": "Concierge Desks & Tablet Apps", "tier": 3, "category": "Front-End", "color": "#a21caf", "value": 8.0, "desc": "Hotel lobby concierge booking screens and affiliate tablet commissions"},

    # Tier 4: Guest & Visitor Segments (20-25)
    {"id": "seg_fit_sightseers", "name": "Independent Sightseers (FIT)", "tier": 4, "category": "Segments", "color": "#0284c7", "value": 65.0, "desc": "Couples, backpackers & solo travelers exploring cities and cultural landmarks"},
    {"id": "seg_family_parks", "name": "Family Vacationers & Theme Parks", "tier": 4, "category": "Segments", "color": "#3b82f6", "value": 40.0, "desc": "Families visiting theme parks, aquariums, zoos, and kid-friendly experiences"},
    {"id": "seg_adventure_seekers", "name": "Adventure & Adrenaline Seekers", "tier": 4, "category": "Segments", "color": "#8b5cf6", "value": 18.0, "desc": "Divers, skydivers, surfers, hikers booking guided outdoor technical excursions"},
    {"id": "seg_cruise_visitors", "name": "Cruise Ship Day Visitors (Shorex)", "tier": 4, "category": "Segments", "color": "#ec4899", "value": 15.0, "desc": "Cruise passengers with strictly limited 6-8 hour port windows"},
    {"id": "seg_multiday_tourists", "name": "Multi-Day Cultural Tour Groups", "tier": 4, "category": "Segments", "color": "#10b981", "value": 14.0, "desc": "Escorted bus tour passengers on 7-14 day comprehensive regional itineraries"},
    {"id": "seg_corp_groups", "name": "Corporate Teambuilding & Groups", "tier": 4, "category": "Segments", "color": "#0d9488", "value": 8.0, "desc": "Company offsites, conference team activities, VIP private charters"}
]

node_indices = {n["id"]: i for i, n in enumerate(nodes)}

links = [
    # Tier 0 -> Tier 1
    {"source": "sup_attractions", "target": "tech_turnstile", "value": 40.0, "label": "Enterprise turnstile system"},
    {"source": "sup_attractions", "target": "tech_restech", "value": 10.0, "label": "ResTech API integration"},
    {"source": "sup_attractions", "target": "tech_offline_pos", "value": 5.0, "label": "Cash gate admissions"},

    {"source": "sup_day_tours", "target": "tech_restech", "value": 45.0, "label": "FareHarbor/Bókun booking"},
    {"source": "sup_day_tours", "target": "tech_offline_pos", "value": 15.0, "label": "Street kiosk cash/card"},

    {"source": "sup_adventure", "target": "tech_restech", "value": 20.0, "label": "Peek/Rezdy digital waiver"},
    {"source": "sup_adventure", "target": "tech_offline_pos", "value": 5.0, "label": "Beach hut walk-up"},

    {"source": "sup_multiday", "target": "tech_dmc_erp", "value": 15.0, "label": "Tourplan group PSS"},
    {"source": "sup_multiday", "target": "tech_turnstile", "value": 5.0, "label": "Charter manifest"},

    # Tier 1 -> Tier 2
    {"source": "tech_restech", "target": "chan_online_direct", "value": 40.0, "label": "Direct website widget"},
    {"source": "tech_restech", "target": "chan_experience_ota", "value": 25.0, "label": "Viator/GYG 2-way API"},
    {"source": "tech_restech", "target": "chan_concierge", "value": 5.0, "label": "Hotel concierge API"},
    {"source": "tech_restech", "target": "chan_cruise_shorex", "value": 5.0, "label": "Port Shorex feed"},

    {"source": "tech_turnstile", "target": "chan_offline_direct", "value": 30.0, "label": "Attraction box office"},
    {"source": "tech_turnstile", "target": "chan_experience_ota", "value": 13.0, "label": "Tiqets/GetYourGuide barcode"},
    {"source": "tech_turnstile", "target": "chan_inbound_dmc", "value": 2.0, "label": "Group voucher entry"},

    {"source": "tech_offline_pos", "target": "chan_offline_direct", "value": 20.0, "label": "Manual cash ticket booth"},
    {"source": "tech_offline_pos", "target": "chan_concierge", "value": 3.0, "label": "Concierge phone call"},
    {"source": "tech_offline_pos", "target": "chan_cruise_shorex", "value": 2.0, "label": "Pier taxi/van walk-up"},

    {"source": "tech_dmc_erp", "target": "chan_inbound_dmc", "value": 10.0, "label": "Wholesale group contract"},
    {"source": "tech_dmc_erp", "target": "chan_cruise_shorex", "value": 5.0, "label": "Contracted shore excursion"},

    # Tier 2 -> Tier 3
    {"source": "chan_offline_direct", "target": "ret_box_office", "value": 50.0, "label": "Physical box office"},
    {"source": "chan_online_direct", "target": "ret_direct_widgets", "value": 40.0, "label": "ResTech widget"},
    {"source": "chan_experience_ota", "target": "ret_ota_marketplaces", "value": 38.0, "label": "Viator/GYG/Klook"},
    {"source": "chan_cruise_shorex", "target": "ret_shorex_desks", "value": 12.0, "label": "Cruise Shorex team"},
    {"source": "chan_inbound_dmc", "target": "ret_dmc_portals", "value": 12.0, "label": "DMC wholesale desk"},
    {"source": "chan_concierge", "target": "ret_concierge_desks", "value": 8.0, "label": "Hotel lobby concierge"},

    # Tier 3 -> Tier 4
    {"source": "ret_box_office", "target": "seg_family_parks", "value": 25.0, "label": "Theme park gate tickets"},
    {"source": "ret_box_office", "target": "seg_fit_sightseers", "value": 15.0, "label": "Walk-up museum visitors"},
    {"source": "ret_box_office", "target": "seg_adventure_seekers", "value": 5.0, "label": "Rental beach walk-up"},
    {"source": "ret_box_office", "target": "seg_cruise_visitors", "value": 5.0, "label": "Independent cruise walk-up"},

    {"source": "ret_direct_widgets", "target": "seg_fit_sightseers", "value": 25.0, "label": "Direct tour bookings"},
    {"source": "ret_direct_widgets", "target": "seg_adventure_seekers", "value": 8.0, "label": "Direct outdoor sports"},
    {"source": "ret_direct_widgets", "target": "seg_family_parks", "value": 5.0, "label": "Advance family tickets"},
    {"source": "ret_direct_widgets", "target": "seg_corp_groups", "value": 2.0, "label": "Private party charters"},

    {"source": "ret_ota_marketplaces", "target": "seg_fit_sightseers", "value": 20.0, "label": "OTA city activities"},
    {"source": "ret_ota_marketplaces", "target": "seg_family_parks", "value": 8.0, "label": "Skip-the-line attraction"},
    {"source": "ret_ota_marketplaces", "target": "seg_adventure_seekers", "value": 5.0, "label": "OTA adventure sports"},
    {"source": "ret_ota_marketplaces", "target": "seg_cruise_visitors", "value": 5.0, "label": "Third-party port tour"},

    {"source": "ret_shorex_desks", "target": "seg_cruise_visitors", "value": 5.0, "label": "Official cruise shorex"},
    {"source": "ret_shorex_desks", "target": "seg_family_parks", "value": 2.0, "label": "Family cruise beach club"},
    {"source": "ret_shorex_desks", "target": "seg_adventure_seekers", "value": 0.0, "label": "Adventure shorex"},
    {"source": "ret_shorex_desks", "target": "seg_multiday_tourists", "value": 5.0, "label": "Pre/post cruise package"},

    {"source": "ret_dmc_portals", "target": "seg_multiday_tourists", "value": 9.0, "label": "Escorted group travel"},
    {"source": "ret_dmc_portals", "target": "seg_corp_groups", "value": 3.0, "label": "Corporate MICE tour"},

    {"source": "ret_concierge_desks", "target": "seg_fit_sightseers", "value": 5.0, "label": "Concierge recommended"},
    {"source": "ret_concierge_desks", "target": "seg_corp_groups", "value": 3.0, "label": "Corporate VIP dinner tour"}
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
    "gross_booking_value": 160.0,
    "intermediary_friction": [
        {"item": "Experience OTA Commissions", "amount": 9.88, "pct_of_gbv": 6.18, "rate_pct": "22-30% on OTA GBV", "desc": "Viator, GetYourGuide, Klook (highest commission friction in travel!)"},
        {"item": "Cruise Line Shorex Markups", "amount": 5.40, "pct_of_gbv": 3.38, "rate_pct": "45% wholesale markup", "desc": "Cruise lines retain 40-100% markup on local operator net rates"},
        {"item": "ResTech Platform SaaS & Fees", "amount": 4.20, "pct_of_gbv": 2.62, "rate_pct": "4-6% booking fee", "desc": "FareHarbor, Bókun, Peek Pro booking engine & consumer fees"},
        {"item": "Payment Processing & Cards", "amount": 4.56, "pct_of_gbv": 2.85, "rate_pct": "2.85% blended", "desc": "Stripe, Adyen, card terminals at remote outdoor locations"},
        {"item": "Inbound DMC Wholesale Margins", "amount": 2.16, "pct_of_gbv": 1.35, "rate_pct": "18% package margin", "desc": "Destination Management Companies package markups"},
        {"item": "Hotel Concierge Commissions", "amount": 1.20, "pct_of_gbv": 0.75, "rate_pct": "15% desk commission", "desc": "Direct cash/credit commission paid to hotel concierge"}
    ],
    "net_operator_revenue": 132.6,
    "operator_operating_costs": [
        {"item": "Tour Guides, Drivers & Staff Labor", "amount": 38.5, "pct_of_net": 29.0, "desc": "Licensed guides, boat captains, bus drivers, scuba divemasters"},
        {"item": "Vehicles, Boats, Fuel & Equipment", "amount": 23.9, "pct_of_net": 18.0, "desc": "Sprinter vans, catamarans, diesel fuel, scuba gear, bikes, helmets"},
        {"item": "National Parks & Concession Permits", "amount": 15.9, "pct_of_net": 12.0, "desc": "National park entry fees, marine park permits, municipal landing dues"},
        {"item": "Commercial Liability Insurance", "amount": 9.3, "pct_of_net": 7.0, "desc": "High-risk adventure activity public liability insurance policies"},
        {"item": "Basecamp, Warehouse & Marina Rent", "amount": 7.9, "pct_of_net": 6.0, "desc": "Boat slip marina leases, equipment sheds, shopfront rental"},
        {"item": "Marketing, Signage & Corporate G&A", "amount": 8.7, "pct_of_net": 6.5, "desc": "Google Local Services ads, TripAdvisor listing, administrative accounting"}
    ],
    "operator_operating_profit": 28.4,
    "ebitda_margin_pct_of_net": 21.4,
    "ebitda_margin_pct_of_gbv": 17.75
}

journey_archetypes = [
    {
        "id": "tour_path_1",
        "title": "Experience Mega-OTA to Independent Day Tour",
        "formula": "Local Operator ➔ ResTech (FareHarbor) ➔ Viator (Tripadvisor) ➔ Colosseum Sightseer",
        "category": "Experience OTA Retail",
        "ticket_example": 120.0,
        "steps": [
            {"node": "Tour Operator", "entity": "Rome Walking Tours LLC", "role": "Supplies 3-hour VIP Colosseum Skip-the-Line tour ($120)", "cost": 0.0, "retained": 120.0},
            {"node": "ResTech Hub", "entity": "FareHarbor (Booking Holdings)", "role": "Syncs live guide capacity, charges 2.0% API connect fee", "cost": 2.4, "retained": 117.6},
            {"node": "Experience Mega-OTA", "entity": "Viator / GetYourGuide", "role": "Promotes tour with Google PPC ads, takes 25% commission ($30.00)", "cost": 30.0, "retained": 87.6},
            {"node": "Payment Processing", "entity": "Stripe / VCC Gateway", "role": "Merchant interchange fee (2.5%)", "cost": 3.0, "retained": 84.6},
            {"node": "Sightseer", "entity": "Independent Traveler", "role": "Presents digital QR voucher on smartphone to guide at gate", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "ticket_price": 120.0,
            "ota_commission": 30.0,
            "restech_fee": 2.4,
            "payment_processing": 3.0,
            "operator_net_received": 84.6,
            "distribution_friction_pct": 29.5,
            "net_yield_pct": 70.5
        },
        "tech_stack": "FareHarbor Open API ➔ OCTO Standard ➔ Viator Supplier API ➔ Traveler Mobile App",
        "key_characteristics": "Highest distribution friction in travel (nearly 30%!); operator sacrifices margin in exchange for global tourist discovery."
    },
    {
        "id": "tour_path_2",
        "title": "Direct Operator Website via ResTech Widget",
        "formula": "Local Operator ➔ Direct Website ➔ Peek Pro / Bókun ➔ Adventure Traveler",
        "category": "Direct ResTech Digital",
        "ticket_example": 150.0,
        "steps": [
            {"node": "Operator Supply", "entity": "Maui Sea Kayak & Snorkel Co", "role": "Publishes 4-hour turtle reef sea kayak tour", "cost": 0.0, "retained": 150.0},
            {"node": "ResTech Engine", "entity": "Peek Pro / Bókun Widget", "role": "Embedded iframe checkout, processes digital liability waiver, charges 6% fee to consumer ($9.00)", "cost": 0.0, "retained": 150.0},
            {"node": "Credit Card Merchant", "entity": "Adyen / Stripe Terminal", "role": "Processes card-not-present online transaction (2.5%)", "cost": 3.75, "retained": 146.25},
            {"node": "Adventure Traveler", "entity": "Direct Tourist", "role": "Discovers operator via Google Search, signs online waiver, pays $159 ($150 + $9 booking fee)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_paid": 159.0,
            "operator_base_price": 150.0,
            "restech_fee_consumer_paid": 9.0,
            "card_processing": 3.75,
            "operator_net_received": 146.25,
            "distribution_friction_pct": 8.0,
            "net_yield_pct": 92.0
        },
        "tech_stack": "WordPress/Webflow Site ➔ Peek Pro JavaScript Widget ➔ Smartwaiver Digital Signature API",
        "key_characteristics": "ResTech shifts 6% booking fee directly onto consumer; operator retains 97.5% of gross base price; full customer data capture."
    },
    {
        "id": "tour_path_3",
        "title": "Cruise Line Shore Excursion (Shorex)",
        "formula": "Local Operator ➔ Cruise Shorex Department ➔ Shipboard Desk ➔ Cruise Passenger",
        "category": "Cruise Line Shorex Wholesale",
        "ticket_example": 140.0,
        "steps": [
            {"node": "Local Excursion Operator", "entity": "Cozumel Eco-Jeep Tours", "role": "Agrees to wholesale net contract rate of $75.00 per person", "cost": 0.0, "retained": 75.0},
            {"node": "Cruise Line Shorex Dept", "entity": "Royal Caribbean Shore Excursions", "role": "Vets $2M liability insurance, guarantees ship won't leave without guests, marks up to $140.00", "cost": 65.0, "retained": 75.0},
            {"node": "Cruise Passenger", "entity": "Ship Passenger", "role": "Purchases tour onboard ship at $140.00 for peace of mind", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "guest_paid_to_cruise": 140.0,
            "cruise_line_markup": 65.0,
            "operator_net_received": 75.0,
            "distribution_friction_pct": 46.4,
            "net_yield_pct": 53.6
        },
        "tech_stack": "Shoreside PSS Shorex Module ➔ Custom Port Manifest File ➔ Pier Dispatch Clipboard",
        "key_characteristics": "Extreme markup (46% friction!); cruise line guarantees return to ship; massive volume (hundreds of passengers per port call)."
    },
    {
        "id": "tour_path_4",
        "title": "Attraction On-Site Box Office Walk-Up",
        "formula": "Attraction Turnstile ➔ Gateway Ticketing / Roller ➔ Walk-Up Visitor",
        "category": "Immediate On-Site Walk-Up",
        "ticket_example": 45.0,
        "steps": [
            {"node": "Attraction Facility", "entity": "Metropolitan Aquarium", "role": "Adult general admission ticket", "cost": 0.0, "retained": 45.0},
            {"node": "Enterprise Gate System", "entity": "Roller Software / Gateway", "role": "Issues barcode paper ticket and triggers RFID turnstile gate", "cost": 0.5, "retained": 44.5},
            {"node": "Box Office EMV Terminal", "entity": "Card Terminal at Gate", "role": "Card-present transaction fee (1.5%)", "cost": 0.68, "retained": 43.82},
            {"node": "Walk-Up Visitor", "entity": "Local Family on Weekend", "role": "Buys ticket at physical booth, enters immediately", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "ticket_price": 45.0,
            "ticketing_system_cost": 0.5,
            "card_present_fee": 0.68,
            "operator_net_received": 43.82,
            "distribution_friction_pct": 2.6,
            "net_yield_pct": 97.4
        },
        "tech_stack": "Gateway Galaxy POS ➔ Automated Optical Turnstile ➔ EMV Chip Reader",
        "key_characteristics": "Lowest distribution cost in tours sector (<3%); susceptible to long queue friction and weather cancellations."
    },
    {
        "id": "tour_path_5",
        "title": "Hotel Concierge Luxury Wine Tour",
        "formula": "Operator ➔ Concierge Portal ➔ Luxury Hotel Concierge ➔ High-End Guest",
        "category": "Hotel Concierge Referral",
        "ticket_example": 350.0,
        "steps": [
            {"node": "Boutique Tour Operator", "entity": "Napa Valley Private Wine Tours", "role": "Offers $350 private sommelier chauffeured tasting", "cost": 0.0, "retained": 350.0},
            {"node": "Concierge Desk", "entity": "Five-Star Luxury Hotel Concierge", "role": "Recommends operator, books via concierge portal, receives 15% commission ($52.50)", "cost": 52.5, "retained": 297.5},
            {"node": "Hotel Guest Folio", "entity": "PMS Room Charge / Card", "role": "Charged to room folio with 2.5% card fee", "cost": 8.75, "retained": 288.75},
            {"node": "Luxury Guest", "entity": "Affluent Hotel Guest", "role": "Departs directly from hotel lobby", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "ticket_price": 350.0,
            "concierge_commission": 52.5,
            "card_fee": 8.75,
            "operator_net_received": 288.75,
            "distribution_friction_pct": 17.5,
            "net_yield_pct": 82.5
        },
        "tech_stack": "Concierge Booking Portal ➔ Hotel PMS Charge Routing ➔ Operator SMS Dispatch",
        "key_characteristics": "High ADR ($350+); relationship-driven sales; concierge expects cash or bi-weekly check commission payments."
    },
    {
        "id": "tour_path_6",
        "title": "Inbound DMC Package Group Tour",
        "formula": "Local Operator ➔ Receptive DMC (Tourplan) ➔ Overseas Travel Agency ➔ Tour Group",
        "category": "Inbound Wholesale B2B",
        "ticket_example": 80.0,
        "steps": [
            {"node": "Local Operator", "entity": "City Sightseeing River Cruise", "role": "Contracts wholesale net rate of $55 per group ticket", "cost": 0.0, "retained": 55.0},
            {"node": "Inbound DMC", "entity": "Destination Management Company", "role": "Bundles cruise with hotel and coach, sells to overseas operator at $70", "cost": 15.0, "retained": 55.0},
            {"node": "Overseas Tour Agency", "entity": "International Travel Wholesaler", "role": "Sells complete 10-day European tour package at retail price", "cost": 10.0, "retained": 55.0},
            {"node": "Package Group", "entity": "45-Passenger Inbound Coach Tour", "role": "Arrives via coach, group leader presents master voucher", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "imputed_retail_value": 80.0,
            "dmc_markup": 15.0,
            "retail_agent_markup": 10.0,
            "operator_net_received": 55.0,
            "distribution_friction_pct": 31.25,
            "net_yield_pct": 68.75
        },
        "tech_stack": "Tourplan DMC System ➔ XML B2B Group Exchange ➔ Printed Master Voucher",
        "key_characteristics": "Guaranteed group coach capacity; zero individual marketing expense; payment settled via 30-day corporate credit."
    },
    {
        "id": "tour_path_7",
        "title": "Multi-Day Expedition Guided Tour",
        "formula": "Expedition Operator ➔ Direct Web / Agent ➔ Outdoor Explorer",
        "category": "Multi-Day Adventure",
        "ticket_example": 2800.0,
        "steps": [
            {"node": "Multi-Day Operator", "entity": "G Adventures / Intrepid Travel", "role": "8-day Inca Trail & Machu Picchu guided trek ($2,800)", "cost": 0.0, "retained": 2800.0},
            {"node": "Adventure Travel Agency", "entity": "Specialist Outdoor Agent", "role": "Advises on physical conditioning, receives 12% commission ($336)", "cost": 336.0, "retained": 2464.0},
            {"node": "Payment Processing", "entity": "Wire / Credit Card Installments", "role": "Deposit & balance merchant fee (2.2%)", "cost": 61.6, "retained": 2402.4},
            {"node": "Outdoor Explorer", "entity": "Trekker", "role": "Completes high-altitude guided expedition", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "trip_price": 2800.0,
            "agent_commission": 336.0,
            "payment_processing": 61.6,
            "operator_net_received": 2402.4,
            "distribution_friction_pct": 14.2,
            "net_yield_pct": 85.8
        },
        "tech_stack": "Custom ERP ➔ Medical Clearance Engine ➔ Trail Permit Authority API",
        "key_characteristics": "High order value ($2,800); involves permit quotas (e.g. Inca Trail 500 permits/day); low cancellation rates."
    },
    {
        "id": "tour_path_8",
        "title": "Hotel In-Room QR Code Upsell",
        "formula": "Operator ➔ Rezdy / Bókun ➔ In-Room Tablet / TV QR Code ➔ Hotel Guest",
        "category": "In-Stay Digital QR",
        "ticket_example": 95.0,
        "steps": [
            {"node": "Local Operator", "entity": "Sunset Catamaran Sailing", "role": "Publishes 2-hour open bar sunset cruise", "cost": 0.0, "retained": 95.0},
            {"node": "ResTech QR Engine", "entity": "Rezdy In-Stay Concierge", "role": "Generates dynamic QR code on hotel smart TV, attributes 10% affiliate fee to hotel", "cost": 9.5, "retained": 85.5},
            {"node": "Payment Gateway", "entity": "Apple Pay / Google Pay via Mobile", "role": "Instant mobile payment interchange (2.5%)", "cost": 2.38, "retained": 83.12},
            {"node": "Hotel Guest", "entity": "Relaxing In-Room Guest", "role": "Scans TV QR code with phone, books same-day sunset cruise", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "ticket_price": 95.0,
            "hotel_affiliate_commission": 9.5,
            "mobile_card_fee": 2.38,
            "operator_net_received": 83.12,
            "distribution_friction_pct": 12.5,
            "net_yield_pct": 87.5
        },
        "tech_stack": "Hotel Hospitality TV App ➔ Rezdy Affiliate Link ➔ Apple Pay Mobile Checkout",
        "key_characteristics": "Captures in-destination impulse bookings; replaces manual concierge paperwork with automated digital attribution."
    },
    {
        "id": "tour_path_9",
        "title": "Visitor Information Center (VIC) Desk",
        "formula": "Operator ➔ Local Tourism Board VIC ➔ Walk-In Tourist",
        "category": "Official Tourism Bureau",
        "ticket_example": 60.0,
        "steps": [
            {"node": "Local Tour Operator", "entity": "Historic City Trolley Tours", "role": "Provides brochure inventory to downtown Visitor Center", "cost": 0.0, "retained": 60.0},
            {"node": "Visitor Information Center", "entity": "City Convention & Visitors Bureau (CVB)", "role": "Staffs information desk, prints ticket voucher, takes 10% commission ($6.00)", "cost": 6.0, "retained": 54.0},
            {"node": "Tourist", "entity": "Day Visitor", "role": "Asks for city map, buys trolley tour ticket at counter", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "ticket_price": 60.0,
            "vic_commission": 6.0,
            "card_fee": 1.2,
            "operator_net_received": 52.8,
            "distribution_friction_pct": 12.0,
            "net_yield_pct": 88.0
        },
        "tech_stack": "Local CVB Box Office POS ➔ Thermal Receipt Ticket ➔ Cashier Drawer",
        "key_characteristics": "High consumer trust; modest commission (10%); heavily dependent on foot traffic location of visitor center."
    },
    {
        "id": "tour_path_10",
        "title": "Corporate Teambuilding Private Charter",
        "formula": "Operator ➔ Corporate Event Sales ➔ Enterprise Planner ➔ Corporate Team",
        "category": "Private Corporate Buyout",
        "ticket_example": 7500.0,
        "steps": [
            {"node": "Activity Operator", "entity": "Offshore Sailing & Regatta Academy", "role": "Exclusive 6-boat match race regatta for corporate company offsite", "cost": 0.0, "retained": 7500.0},
            {"node": "Internal Group Sales", "entity": "Operator Group Coordinator", "role": "Quotes custom contract, handles catering and insurance waivers ($150 admin)", "cost": 150.0, "retained": 7350.0},
            {"node": "Enterprise Client", "entity": "Tech Company HR Department", "role": "Pays $7,500 via ACH direct bank transfer (0% credit card fees!)", "cost": 10.0, "retained": 7340.0},
            {"node": "Corporate Employees", "entity": "40 Company Staff", "role": "Participates in half-day competitive sailing regatta", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "contract_value": 7500.0,
            "admin_sales_cost": 150.0,
            "bank_ach_fee": 10.0,
            "operator_net_received": 7340.0,
            "distribution_friction_pct": 2.1,
            "net_yield_pct": 97.9
        },
        "tech_stack": "Pipedrive/HubSpot CRM ➔ PandaDoc Electronic Contract ➔ Bank ACH Transfer",
        "key_characteristics": "Lowest distribution friction in tours (<2.5%); high dollar value; high weekday utilization when leisure demand is low."
    }
]

benchmarks = [
    {
        "type": "Direct On-Site Box Office",
        "key_players": "Physical Ticket Booths, Turnstiles, Cashier",
        "take_rate_pct": "1.5% - 2.5% (card fee)",
        "channel_share_pct": "31.3%",
        "cancellation_rate_pct": "0% (non-refundable)",
        "lead_time_days": "0 days (same-day)",
        "guest_data_ownership": "Minimal (Anonymous)",
        "pros": "Zero commission, instant cash flow, captive audience at destination",
        "cons": "Long queues, weather vulnerability, staff payroll cost for ticket windows"
    },
    {
        "type": "Direct Website (ResTech Widget)",
        "key_players": "FareHarbor, Peek Pro, Bókun, Rezdy",
        "take_rate_pct": "3% - 6% (or consumer fee)",
        "channel_share_pct": "25.0%",
        "cancellation_rate_pct": "5% - 8%",
        "lead_time_days": "7 - 21 days",
        "guest_data_ownership": "100% Owned by Operator",
        "pros": "Digital liability waivers, automated SMS reminders, lowest online cost",
        "cons": "Requires local SEO, Google Business profile optimization, digital ad spend"
    },
    {
        "type": "Experience Mega-OTAs",
        "key_players": "Viator, GetYourGuide, Klook, Tiqets",
        "take_rate_pct": "20% - 30% commission",
        "channel_share_pct": "23.8%",
        "cancellation_rate_pct": "15% - 22%",
        "lead_time_days": "3 - 14 days",
        "guest_data_ownership": "Masked / Restricted",
        "pros": "Massive global tourist reach, multilingual customer support, fills open slots",
        "cons": "Brutal commission take rate (up to 30%), strict 24-hour free cancellation policies"
    },
    {
        "type": "Cruise Shore Excursions (Shorex)",
        "key_players": "Royal Caribbean, Carnival, NCL Shorex",
        "take_rate_pct": "40% - 60% markup",
        "channel_share_pct": "7.5%",
        "cancellation_rate_pct": "2% - 4%",
        "lead_time_days": "60 - 120 days",
        "guest_data_ownership": "Cruise Line Owned",
        "pros": "Guaranteed large passenger volume (hundreds per call), ship return guarantee",
        "cons": "Enormous margin loss (cruise line keeps 45%+), strict insurance and indemnity rules"
    },
    {
        "type": "Inbound DMCs & Wholesale",
        "key_players": "Destination Management Companies, Tourplan",
        "take_rate_pct": "15% - 22% net markup",
        "channel_share_pct": "7.5%",
        "cancellation_rate_pct": "4% - 6%",
        "lead_time_days": "90 - 180 days",
        "guest_data_ownership": "Wholesale Manifest",
        "pros": "Predictable seasonal coach groups, advance financial commitments",
        "cons": "Lower net price per person, long payment settlement terms (30-60 days)"
    },
    {
        "type": "Hotel Concierge & Lobby QR",
        "key_players": "Luxury Concierges, In-Room Tablets",
        "take_rate_pct": "10% - 15% commission",
        "channel_share_pct": "5.0%",
        "cancellation_rate_pct": "3% - 5%",
        "lead_time_days": "1 - 3 days",
        "guest_data_ownership": "Direct Guest Details",
        "pros": "High ADR luxury travelers, personalized recommendation trust",
        "cons": "Highly fragmented, relationship-dependent, requires manual commission checks"
    }
]

output_data = {
    "tours_metrics": metrics,
    "nodes": nodes,
    "links": sankey_links,
    "revenue_cost_split": revenue_cost_split,
    "journey_archetypes": journey_archetypes,
    "intermediary_benchmarks": benchmarks
}

with open(os.path.join(tours_dir, "data", "tours_distribution_data.json"), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

with open(os.path.join(tours_dir, "data", "channel_breakdown.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Source Node", "Target Node", "Value ($ Billions)", "Share of Global GBV (%)", "Flow Description"])
    for l in sankey_links:
        src_name = nodes[l["source"]]["name"]
        tgt_name = nodes[l["target"]]["name"]
        val = l["value"]
        pct = round((val / 160.0) * 100, 2)
        writer.writerow([src_name, tgt_name, val, f"{pct}%", l["label"]])

print("Tours data generated successfully!")
