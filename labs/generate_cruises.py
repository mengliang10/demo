import os, json, csv

cruise_dir = "/run/media/ml/Storage/Labs/cruises"
os.makedirs(os.path.join(cruise_dir, "data"), exist_ok=True)
os.makedirs(os.path.join(cruise_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(cruise_dir, "js"), exist_ok=True)

# 1. Cruise Metrics
metrics = {
    "global_gbv_billions": 38.0,
    "total_distribution_cost_billions": 4.75,
    "net_cruise_revenue_billions": 33.25,
    "ticket_revenue_billions": 25.0,
    "onboard_revenue_billions": 13.0,
    "agent_intermediated_share_pct": 76.3,
    "direct_share_pct": 23.7,
    "blended_distribution_take_rate_pct": 12.5,
    "annual_passengers_millions": 33.5,
    "blended_revenue_per_passenger_usd": 1134.33
}

# 2. Sankey Nodes
nodes = [
    # Tier 0: Supply (0-3)
    {"id": "sup_mega", "name": "Mega-Ship Contemporary Lines", "tier": 0, "category": "Supply", "color": "#3b82f6", "value": 24.0, "desc": "Carnival, Royal Caribbean, NCL, MSC (2,500 - 6,000+ guests)"},
    {"id": "sup_premium", "name": "Premium & Mid-Size Lines", "tier": 0, "category": "Supply", "color": "#06b6d4", "value": 8.5, "desc": "Celebrity, Princess, Holland America (1,500 - 3,000 guests)"},
    {"id": "sup_luxury", "name": "Luxury & Ultra-Luxury Lines", "tier": 0, "category": "Supply", "color": "#8b5cf6", "value": 3.5, "desc": "Silversea, Regent Seven Seas, Seabourn, Viking Ocean (300 - 900 guests)"},
    {"id": "sup_exped", "name": "Expedition & River Cruise Lines", "tier": 0, "category": "Supply", "color": "#10b981", "value": 2.0, "desc": "Viking River, Hurtigruten, Ponant, Lindblad, AmaWaterways"},

    # Tier 1: Tech & Reservation Infrastructure (4-7)
    {"id": "tech_brand_res", "name": "Brand Reservation Engines (Polar / Espresso)", "tier": 1, "category": "Tech", "color": "#6366f1", "value": 21.0, "desc": "Carnival Polar, RCG Espresso, NCL BookSafe, direct XML booking engines"},
    {"id": "tech_switch", "name": "Cruise B2B Switches & Aggregators", "tier": 1, "category": "Tech", "color": "#ec4899", "value": 12.0, "desc": "Amadeus Cruise, Sabre Cruise, Revelex, Versonix Seaware, Travelport Cruise"},
    {"id": "tech_onboard", "name": "Onboard Future Cruise Desks", "tier": 1, "category": "Tech", "color": "#f59e0b", "value": 3.5, "desc": "NextCruise / Future Cruise Consultation desks on operating vessels"},
    {"id": "tech_charter", "name": "MICE & Charter Sales Engines", "tier": 1, "category": "Tech", "color": "#14b8a6", "value": 1.5, "desc": "Full-ship charter contracting & corporate incentive management platforms"},

    # Tier 2: Primary Channels (8-13)
    {"id": "chan_host_agencies", "name": "Travel Advisors & Host Agencies", "tier": 2, "category": "Agents", "color": "#a855f7", "value": 13.5, "desc": "Cruise Planners, Avoya Travel, Dream Vacations, InteleTravel, independent agents"},
    {"id": "chan_cruise_ota", "name": "Cruise Specialist OTAs & Portals", "tier": 2, "category": "OTAs", "color": "#f97316", "value": 7.0, "desc": "Vacations To Go, Cruise.com, CruisesOnly (World Travel Holdings), Expedia Cruises"},
    {"id": "chan_direct_web", "name": "Direct Brand.com & Outbound PVP", "tier": 2, "category": "Direct", "color": "#22c55e", "value": 9.0, "desc": "Direct consumer websites, mobile apps, Personal Vacation Planners (PVP call centers)"},
    {"id": "chan_big_box", "name": "Big Box Retailers (Costco, AAA)", "tier": 2, "category": "Retail", "color": "#eab308", "value": 3.5, "desc": "Costco Travel, AAA / CAA Travel (cash-card rebates & member benefits)"},
    {"id": "chan_consortia", "name": "Luxury Consortia (Virtuoso, Signature)", "tier": 2, "category": "Consortia", "color": "#c026d3", "value": 3.0, "desc": "Virtuoso, Signature Travel Network, Ensemble, Amex Travel (exclusive shipboard credits)"},
    {"id": "chan_charters", "name": "Full-Ship Charters & Corporate MICE", "tier": 2, "category": "MICE", "color": "#0d9488", "value": 2.0, "desc": "Corporate incentive programs, music/theme charters, private buyout groups"},

    # Tier 3: Secondary Intermediaries & Desks (14-19)
    {"id": "ret_agent_desks", "name": "Home-Based Advisor Desks", "tier": 3, "category": "Desks", "color": "#9333ea", "value": 13.5, "desc": "Certified Cruise Counselors (CLIA MCC/ECC) booking via host portals"},
    {"id": "ret_ota_centers", "name": "Cruise OTA Portals & Call Centers", "tier": 3, "category": "Desks", "color": "#ea580c", "value": 7.0, "desc": "High-volume discount cruise aggregators with dedicated telephone cruise agents"},
    {"id": "ret_direct_touch", "name": "Brand Direct & Onboard Desks", "tier": 3, "category": "Desks", "color": "#16a34a", "value": 9.0, "desc": "Consumer web portals, PVP relationship managers, shipboard loyalty desks"},
    {"id": "ret_member_clubs", "name": "Club Travel Desks", "tier": 3, "category": "Desks", "color": "#ca8a04", "value": 3.5, "desc": "Costco member booking desks, AAA auto club regional offices"},
    {"id": "ret_lux_advisors", "name": "Bespoke Luxury Advisors", "tier": 3, "category": "Desks", "color": "#db2777", "value": 3.0, "desc": "High-touch luxury advisors arranging pre/post cruise flights, 5-star hotels & private transfers"},
    {"id": "ret_mice_organizers", "name": "Corporate Event Organizers", "tier": 3, "category": "Desks", "color": "#0f766e", "value": 2.0, "desc": "Enterprise meeting planners executing onboard corporate conferences"},

    # Tier 4: Passenger Demographics & Segments (20-26)
    {"id": "seg_family", "name": "Family & Multigen Cruisers", "tier": 4, "category": "Segments", "color": "#3b82f6", "value": 13.0, "desc": "Parents, kids & grandparents sailing on mega-ships with waterslides & kids clubs"},
    {"id": "seg_mature", "name": "Mature & Retiree Cruisers", "tier": 4, "category": "Segments", "color": "#0284c7", "value": 10.5, "desc": "Longer 10-14+ night itineraries, destination enrichment, cultural lecturers"},
    {"id": "seg_luxury", "name": "Luxury & World Cruisers", "tier": 4, "category": "Segments", "color": "#8b5cf6", "value": 4.5, "desc": "All-inclusive suites, fine wines, private butlers, 90-180 day world voyages"},
    {"id": "seg_couples", "name": "Couples & Honeymooners", "tier": 4, "category": "Segments", "color": "#ec4899", "value": 4.0, "desc": "Balcony cabins, specialty dining packages, romantic Caribbean / Mediterranean sailings"},
    {"id": "seg_adventure", "name": "Expedition & River Explorers", "tier": 4, "category": "Segments", "color": "#10b981", "value": 3.0, "desc": "Antarctic zodiac landings, Galapagos wildlife, Rhine/Danube cultural river voyages"},
    {"id": "seg_mice", "name": "Corporate Incentive & MICE", "tier": 4, "category": "Segments", "color": "#0d9488", "value": 2.0, "desc": "Presidents Club winners, tech corporate conferences, exclusive ship takeovers"},
    {"id": "seg_solo", "name": "Solo & Studio Cruisers", "tier": 4, "category": "Segments", "color": "#f59e0b", "value": 1.0, "desc": "Solo traveler studio cabins with no single supplement, dedicated solo lounges"}
]

node_indices = {n["id"]: i for i, n in enumerate(nodes)}

# Links
links = [
    # Tier 0 -> Tier 1
    {"source": "sup_mega", "target": "tech_brand_res", "value": 14.5, "label": "Mega-line direct engine"},
    {"source": "sup_mega", "target": "tech_switch", "value": 7.0, "label": "GDS & switch feed"},
    {"source": "sup_mega", "target": "tech_onboard", "value": 2.0, "label": "Onboard desk bookings"},
    {"source": "sup_mega", "target": "tech_charter", "value": 0.5, "label": "Theme charters"},

    {"source": "sup_premium", "target": "tech_brand_res", "value": 4.0, "label": "Premium line engine"},
    {"source": "sup_premium", "target": "tech_switch", "value": 3.0, "label": "Agency switch"},
    {"source": "sup_premium", "target": "tech_onboard", "value": 1.0, "label": "Onboard future cruise"},
    {"source": "sup_premium", "target": "tech_charter", "value": 0.5, "label": "Corporate groups"},

    {"source": "sup_luxury", "target": "tech_brand_res", "value": 1.5, "label": "Luxury direct portal"},
    {"source": "sup_luxury", "target": "tech_switch", "value": 1.2, "label": "Virtuoso/Signature switch"},
    {"source": "sup_luxury", "target": "tech_onboard", "value": 0.3, "label": "Luxury world cruise desk"},
    {"source": "sup_luxury", "target": "tech_charter", "value": 0.5, "label": "Luxury ship buyouts"},

    {"source": "sup_exped", "target": "tech_brand_res", "value": 1.0, "label": "Expedition direct res"},
    {"source": "sup_exped", "target": "tech_switch", "value": 0.8, "label": "Specialist agency switch"},
    {"source": "sup_exped", "target": "tech_onboard", "value": 0.2, "label": "Re-booking discount"},

    # Tier 1 -> Tier 2
    {"source": "tech_brand_res", "target": "chan_direct_web", "value": 7.0, "label": "Brand website & app"},
    {"source": "tech_brand_res", "target": "chan_host_agencies", "value": 8.0, "label": "Host agency direct API"},
    {"source": "tech_brand_res", "target": "chan_cruise_ota", "value": 3.5, "label": "OTA direct connect"},
    {"source": "tech_brand_res", "target": "chan_big_box", "value": 2.5, "label": "Big box wholesale feed"},

    {"source": "tech_switch", "target": "chan_host_agencies", "value": 5.5, "label": "Amadeus/Sabre Cruise to Agents"},
    {"source": "tech_switch", "target": "chan_cruise_ota", "value": 3.5, "label": "Revelex/Versonix to OTAs"},
    {"source": "tech_switch", "target": "chan_consortia", "value": 2.0, "label": "Consortia GDS terminal"},
    {"source": "tech_switch", "target": "chan_big_box", "value": 1.0, "label": "Costco Travel switch"},

    {"source": "tech_onboard", "target": "chan_direct_web", "value": 2.0, "label": "Onboard direct booking"},
    {"source": "tech_onboard", "target": "chan_consortia", "value": 1.0, "label": "Transferred to guest advisor"},
    {"source": "tech_onboard", "target": "chan_host_agencies", "value": 0.5, "label": "Assigned to booking agency"},

    {"source": "tech_charter", "target": "chan_charters", "value": 2.0, "label": "Full ship charter contracts"},

    # Tier 2 -> Tier 3
    {"source": "chan_host_agencies", "target": "ret_agent_desks", "value": 13.5, "label": "Home-based advisor execution"},
    {"source": "chan_cruise_ota", "target": "ret_ota_centers", "value": 7.0, "label": "Cruise OTA booking desk"},
    {"source": "chan_direct_web", "target": "ret_direct_touch", "value": 9.0, "label": "Consumer web & PVP call center"},
    {"source": "chan_big_box", "target": "ret_member_clubs", "value": 3.5, "label": "Club member booking"},
    {"source": "chan_consortia", "target": "ret_lux_advisors", "value": 3.0, "label": "Bespoke luxury advisory"},
    {"source": "chan_charters", "target": "ret_mice_organizers", "value": 2.0, "label": "Corporate meeting planners"},

    # Tier 3 -> Tier 4
    {"source": "ret_agent_desks", "target": "seg_family", "value": 5.5, "label": "Family cruise bookings"},
    {"source": "ret_agent_desks", "target": "seg_mature", "value": 5.0, "label": "Mature destination cruisers"},
    {"source": "ret_agent_desks", "target": "seg_couples", "value": 2.0, "label": "Romantic getaway sailings"},
    {"source": "ret_agent_desks", "target": "seg_adventure", "value": 1.0, "label": "River cruise bookings"},

    {"source": "ret_ota_centers", "target": "seg_family", "value": 3.5, "label": "Discount family packages"},
    {"source": "ret_ota_centers", "target": "seg_couples", "value": 1.5, "label": "Caribbean last-minute"},
    {"source": "ret_ota_centers", "target": "seg_mature", "value": 1.5, "label": "Alaska / Europe deals"},
    {"source": "ret_ota_centers", "target": "seg_solo", "value": 0.5, "label": "Solo studio promotions"},

    {"source": "ret_direct_touch", "target": "seg_family", "value": 3.0, "label": "Brand.com direct family"},
    {"source": "ret_direct_touch", "target": "seg_mature", "value": 2.5, "label": "Loyalty tier members"},
    {"source": "ret_direct_touch", "target": "seg_luxury", "value": 1.5, "label": "Viking / Silversea direct"},
    {"source": "ret_direct_touch", "target": "seg_adventure", "value": 1.5, "label": "Expedition direct web"},
    {"source": "ret_direct_touch", "target": "seg_solo", "value": 0.5, "label": "Direct solo bookings"},

    {"source": "ret_member_clubs", "target": "seg_family", "value": 1.0, "label": "Costco family buyers"},
    {"source": "ret_member_clubs", "target": "seg_mature", "value": 1.5, "label": "AAA member itineraries"},
    {"source": "ret_member_clubs", "target": "seg_couples", "value": 0.5, "label": "Costco honeymooners"},
    {"source": "ret_member_clubs", "target": "seg_luxury", "value": 0.5, "label": "Club luxury sailings"},

    {"source": "ret_lux_advisors", "target": "seg_luxury", "value": 2.5, "label": "Virtuoso world cruisers"},
    {"source": "ret_lux_advisors", "target": "seg_adventure", "value": 0.5, "label": "Luxury expedition yachts"},

    {"source": "ret_mice_organizers", "target": "seg_mice", "value": 2.0, "label": "Corporate incentive charter"}
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

# 3. Revenue & Cost Split (Earnings Waterfall)
revenue_cost_split = {
    "gross_booking_value": 38.0,
    "intermediary_friction": [
        {"item": "Travel Agency Commissions", "amount": 2.65, "pct_of_gbv": 6.97, "rate_pct": "12-16% on comm. fare", "desc": "Host agencies & travel agents (paid on cruise fare minus NCCF)"},
        {"item": "Cruise Specialist OTA Margins", "amount": 0.85, "pct_of_gbv": 2.24, "rate_pct": "10-14% blended", "desc": "Vacations To Go, Cruise.com, CruisesOnly"},
        {"item": "Consortia Overrides & Co-op Ad Funds", "amount": 0.35, "pct_of_gbv": 0.92, "rate_pct": "2-4% override", "desc": "Virtuoso, Signature, Ensemble annual volume kickbacks"},
        {"item": "Big Box Member Rebates / Cash Cards", "amount": 0.25, "pct_of_gbv": 0.66, "rate_pct": "8% member value", "desc": "Costco Shop Cards & AAA member amenity subsidies"},
        {"item": "GDS & Switch API Fees", "amount": 0.20, "pct_of_gbv": 0.53, "rate_pct": "$15-$25/booking", "desc": "Amadeus Cruise, Sabre Cruise, Revelex transaction fees"},
        {"item": "Credit Card Merchant Interchange", "amount": 0.45, "pct_of_gbv": 1.18, "rate_pct": "2.2% blended", "desc": "Deposit & final payment merchant processing (Visa/MC/Amex)"}
    ],
    "net_cruise_revenue": 33.25,
    "cruise_operating_costs": [
        {"item": "Shipboard Crew Payroll & Manning", "amount": 4.80, "pct_of_net": 14.4, "desc": "Officers, marine crew, hotel staff, entertainers, chefs (1,000-2,200 crew per ship)"},
        {"item": "Marine Fuel (HFO, MGO, LNG)", "amount": 4.20, "pct_of_net": 12.6, "desc": "Propulsion and ship hotel electrical load power"},
        {"item": "Food & Beverage Hotel Supplies", "amount": 3.10, "pct_of_net": 9.3, "desc": "Provisions, specialty ingredients, luxury hotel linens, amenities"},
        {"item": "Port Taxes, Dues, Pilotage & Tug Services", "amount": 3.40, "pct_of_net": 10.2, "desc": "Berthing fees, maritime pilotage, customs & immigration clearances"},
        {"item": "Ship Repairs, Drydock & Depreciation", "amount": 3.80, "pct_of_net": 11.4, "desc": "Scheduled 3-5 year drydocks, hull repainting, regulatory SOLAS maintenance"},
        {"item": "Onboard Entertainment & Production", "amount": 1.50, "pct_of_net": 4.5, "desc": "Broadway-style shows, ice skaters, aquatic acrobats, live musicians"},
        {"item": "Selling, Marketing & Corporate G&A", "amount": 2.30, "pct_of_net": 6.9, "desc": "Global advertising, shore-side headquarters, shoreside IT & reservations"}
    ],
    "gross_operating_profit": 10.15,
    "gop_margin_pct_of_net": 30.5,
    "gop_margin_pct_of_gbv": 26.7
}

# 4. Specific Cruise Distribution Archetypes
journey_archetypes = [
    {
        "id": "cruise_path_1",
        "title": "Host Agency Travel Advisor to Mega-Ship Family",
        "formula": "Cruise Line ➔ RCG Espresso / Polar ➔ Host Agency (Cruise Planners) ➔ Family Cruiser",
        "category": "Host Agency Retail B2B",
        "ticket_example": 2400.0,
        "onboard_example": 1100.0,
        "steps": [
            {"node": "Cruise Line Supply", "entity": "Royal Caribbean / Carnival", "role": "Supplies 7-night Caribbean balcony stateroom for family of 4", "cost": 0.0, "retained": 3500.0},
            {"node": "Reservation Engine", "entity": "RCG Espresso / Carnival Polar", "role": "Manages live deck plan stateroom inventory and dining seating", "cost": 25.0, "retained": 3475.0},
            {"node": "Host Agency & Advisor", "entity": "Cruise Planners / Avoya Agent", "role": "Advises family on cabin selection, receives 15% commission on $2,000 commissionable fare (excluding $400 NCCF)", "cost": 300.0, "retained": 3175.0},
            {"node": "Onboard Spend Generation", "entity": "Shipboard Point-of-Sale (SeaPass / Medallion)", "role": "Family spends $1,100 on drink packages, specialty dining, arcade & shore excursions (0% agent commission!)", "cost": 0.0, "retained": 3175.0},
            {"node": "Family Cruisers", "entity": "Family of Four", "role": "Pays $2,400 ticket + $1,100 onboard = $3,500 total vacation spend", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 3500.0,
            "ticket_fare": 2400.0,
            "onboard_spend": 1100.0,
            "agent_commission": 300.0,
            "tech_fee": 25.0,
            "credit_card_fee": 77.0,
            "cruise_net_received": 3098.0,
            "distribution_friction_pct": 11.5,
            "net_yield_pct": 88.5
        },
        "tech_stack": "Cruise PSS ➔ Polar/Espresso B2B API ➔ Host Agency CRM (Cruisearc/AgentConsole) ➔ Client Proposal Portal",
        "key_characteristics": "Agent receives 0% on onboard spend ($1,100 is 100% cruise margin!); Non-Commissionable Cruise Fares (NCCF) artificially reduce agent payout."
    },
    {
        "id": "cruise_path_2",
        "title": "Cruise Specialist OTA Discount Journey",
        "formula": "Cruise Line ➔ Revelex / Amadeus Cruise ➔ Cruise OTA (Vacations To Go) ➔ Deal-Seeking Cruiser",
        "category": "High-Volume OTA Specialist",
        "ticket_example": 1200.0,
        "onboard_example": 600.0,
        "steps": [
            {"node": "Cruise Line Supply", "entity": "NCL / MSC Cruises", "role": "Releases unsold balcony cabins 60 days before sailing at promotional rate", "cost": 0.0, "retained": 1800.0},
            {"node": "Cruise B2B Switch", "entity": "Revelex / Versonix", "role": "Pulls dynamic promotional rates into 90-Day Ticker", "cost": 18.0, "retained": 1782.0},
            {"node": "Cruise Specialist OTA", "entity": "Vacations To Go / Cruise.com", "role": "Discounts fare, rebates part of commission as $100 onboard credit (OBC)", "cost": 160.0, "retained": 1622.0},
            {"node": "Deal-Seeking Cruiser", "entity": "Value Vacationer", "role": "Books 7-night sailing, spends $600 onboard in casino and bars", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 1800.0,
            "ota_commission_net": 160.0,
            "tech_switch_fee": 18.0,
            "credit_card_fee": 39.6,
            "cruise_net_received": 1582.4,
            "distribution_friction_pct": 12.1,
            "net_yield_pct": 87.9
        },
        "tech_stack": "Cruise Line API ➔ Revelex PowerAgent ➔ Vacations To Go 90-Day Ticker Engine ➔ Outbound Call Desk",
        "key_characteristics": "Aggressive price parity workarounds via Onboard Credits (OBC) and free bottle of wine; clears distressed close-in inventory."
    },
    {
        "id": "cruise_path_3",
        "title": "Direct Brand.com to Repeat Loyalty Cruiser",
        "formula": "Cruise Line ➔ Brand.com Website ➔ Native Mobile App ➔ Loyalty Elite Member",
        "category": "Direct Digital & Loyalty",
        "ticket_example": 2000.0,
        "onboard_example": 900.0,
        "steps": [
            {"node": "Cruise Line Supply", "entity": "Princess / Celebrity Cruises", "role": "Targeted email offer with Past Guest Loyalty Discount", "cost": 0.0, "retained": 2900.0},
            {"node": "Brand.com Booking Engine", "entity": "Princess.com / Celebrity.com", "role": "Real-time cabin picker, interactive deck plans, dining reservation cross-sell", "cost": 10.0, "retained": 2890.0},
            {"node": "Direct Loyalty Member", "entity": "Captain's Club / MedallionClass Elite", "role": "Books directly online, pre-purchases Premier Beverage Package & Wi-Fi", "cost": 0.0, "retained": 2890.0}
        ],
        "financial_summary": {
            "total_guest_spend": 2900.0,
            "booking_engine_cost": 10.0,
            "merchant_card_fee": 63.8,
            "cruise_net_received": 2826.2,
            "distribution_friction_pct": 2.5,
            "net_yield_pct": 97.5
        },
        "tech_stack": "Direct Cloud PSS ➔ Brand.com React/Node Web App ➔ OceanMedallion / BLE IoT Shipboard Ecosystem",
        "key_characteristics": "Lowest distribution cost in cruise industry (<3%); pre-cruise ancillary conversion is 3x higher on direct web than via third-party agents."
    },
    {
        "id": "cruise_path_4",
        "title": "Luxury Consortia World Cruise Journey",
        "formula": "Luxury Cruise Line ➔ Versonix Seaware ➔ Virtuoso Luxury Advisor ➔ High-Net-Worth World Cruiser",
        "category": "Ultra-Luxury & World Voyages",
        "ticket_example": 45000.0,
        "onboard_example": 5000.0,
        "steps": [
            {"node": "Luxury Cruise Line", "entity": "Silversea / Regent Seven Seas", "role": "120-day Grand Voyage / World Cruise all-suite stateroom", "cost": 0.0, "retained": 50000.0},
            {"node": "Luxury Res Engine", "entity": "Versonix Seaware", "role": "Custom cabin customization, bespoke flight routing, butler assignment", "cost": 50.0, "retained": 49950.0},
            {"node": "Virtuoso Luxury Advisor", "entity": "Top-Tier Luxury Travel Advisor", "role": "Provides bespoke itinerary planning, receives 16% commission ($7,200) + exclusive Virtuoso shore gala", "cost": 7200.0, "retained": 42750.0},
            {"node": "High-Net-Worth Guest", "entity": "Ultra-HNW Retired Couple", "role": "Pays $50,000 all-inclusive fare (premium liquor, shore excursions, airfare included)", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 50000.0,
            "advisor_commission": 7200.0,
            "tech_fee": 50.0,
            "wire_merchant_fee": 500.0,
            "cruise_net_received": 42250.0,
            "distribution_friction_pct": 15.5,
            "net_yield_pct": 84.5
        },
        "tech_stack": "Seaware CRM ➔ Virtuoso Member Portal ➔ Dedicated Shoreside Concierge Desk",
        "key_characteristics": "Highest single-booking revenue in travel ($50k - $200k+); massive agent commissions; relationship-driven sales cycle (6-18 months)."
    },
    {
        "id": "cruise_path_5",
        "title": "Big Box Retailer Member Journey",
        "formula": "Cruise Line ➔ Direct B2B API ➔ Costco Travel ➔ Costco Member (Cash Card Buyer)",
        "category": "Big Box Volume Retail",
        "ticket_example": 2200.0,
        "onboard_example": 800.0,
        "steps": [
            {"node": "Cruise Line", "entity": "Celebrity / Royal Caribbean", "role": "Offers preferred group inventory block with exclusive member benefits", "cost": 0.0, "retained": 3000.0},
            {"node": "Costco Travel API", "entity": "Costco Travel Proprietary Switch", "role": "Syncs live pricing and bundles Costco Shop Card ($175 value)", "cost": 15.0, "retained": 2985.0},
            {"node": "Costco Travel Desk", "entity": "Costco Travel Phone & Web Portal", "role": "Charges membership wholesale rate, passes Shop Card rebate funded from commission", "cost": 220.0, "retained": 2765.0},
            {"node": "Costco Member", "entity": "Loyal Warehouse Club Member", "role": "Books cruise, receives $175 Costco gift card by mail after sailing", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 3000.0,
            "costco_commission_and_rebate": 220.0,
            "tech_fee": 15.0,
            "credit_card_fee": 66.0,
            "cruise_net_received": 2699.0,
            "distribution_friction_pct": 10.0,
            "net_yield_pct": 90.0
        },
        "tech_stack": "Cruise Line Direct API ➔ Costco Travel Custom Booking Engine ➔ Membership Verification Database",
        "key_characteristics": "High guest volume; high-income demographic; Costco Shop Card effectively acts as a closed-loop price discount without violating public rate parity."
    },
    {
        "id": "cruise_path_6",
        "title": "Onboard Future Cruise Booking Desk",
        "formula": "Cruise Line ➔ Shipboard NextCruise Desk ➔ Onboard Guest (Re-booking at Sea)",
        "category": "Shipboard Direct Retention",
        "ticket_example": 2600.0,
        "onboard_example": 900.0,
        "steps": [
            {"node": "Operating Cruise Ship", "entity": "Cruise Ship at Sea", "role": "NextCruise / Future Cruise Consultation Desk located in ship atrium", "cost": 0.0, "retained": 3500.0},
            {"node": "Onboard Sales Consultant", "entity": "Cruise Line Future Cruise Manager", "role": "Offers low $100 deposit + up to $600 onboard credit on next sailing", "cost": 20.0, "retained": 3480.0},
            {"node": "Original Booking Agent", "entity": "Guest's Original Travel Agency", "role": "Cruise line automatically credits original agent with booking (protects agent relationship!)", "cost": 260.0, "retained": 3220.0},
            {"node": "Captive Cruiser", "entity": "Sailing Guest", "role": "Re-books next year's vacation while euphoric on vacation at sea", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 3500.0,
            "agent_commission_protected": 260.0,
            "onboard_consultant_cost": 20.0,
            "card_fee": 57.2,
            "cruise_net_received": 3162.8,
            "distribution_friction_pct": 9.6,
            "net_yield_pct": 90.4
        },
        "tech_stack": "Satellite Starlink WAN ➔ Shoreside PSS ➔ Future Cruise Lead Generator ➔ Automated Agency Notification",
        "key_characteristics": "Incredible conversion rate (guests are currently enjoying their vacation); unique policy where cruise line gives full commission credit back to travel agent."
    },
    {
        "id": "cruise_path_7",
        "title": "European River Cruise Specialist Journey",
        "formula": "River Cruise Line ➔ Amadeus Cruise ➔ River Cruise Specialist Agent ➔ Mature Culture Cruiser",
        "category": "River & Cultural Cruising",
        "ticket_example": 4200.0,
        "onboard_example": 400.0,
        "steps": [
            {"node": "River Cruise Operator", "entity": "Viking River Cruises / AmaWaterways", "role": "190-passenger Longship sailing 8-day Rhine Getaway", "cost": 0.0, "retained": 4600.0},
            {"node": "B2B Cruise Switch", "entity": "Amadeus Cruise / Direct Extranet", "role": "Handles cabin category allocations and guided excursion bundles", "cost": 25.0, "retained": 4575.0},
            {"node": "River Cruise Specialist", "entity": "Specialist Travel Agency", "role": "Explains water level locks, included excursions, receives 14% commission ($588)", "cost": 588.0, "retained": 3987.0},
            {"node": "Mature Cultural Cruiser", "entity": "Active Retiree Couple", "role": "Pays $4,600 inclusive of daily guided walking tours, beer/wine with meals", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 4600.0,
            "agent_commission": 588.0,
            "tech_fee": 25.0,
            "card_fee": 101.2,
            "cruise_net_received": 3885.8,
            "distribution_friction_pct": 15.5,
            "net_yield_pct": 84.5
        },
        "tech_stack": "Viking Direct PSS ➔ Specialist Extranet ➔ Amadeus River Booking Engine",
        "key_characteristics": "Almost all shore excursions are included in base ticket; lower onboard spend ($400) because beer/wine with meals are complimentary."
    },
    {
        "id": "cruise_path_8",
        "title": "Full-Ship Corporate Incentive Charter",
        "formula": "Cruise Line ➔ Corporate Charter Sales Team ➔ Enterprise Meeting Planner ➔ Incentive Winners",
        "category": "Full Ship Buyout & MICE",
        "ticket_example": 3500000.0,
        "onboard_example": 500000.0,
        "steps": [
            {"node": "Cruise Line Fleet", "entity": "Norwegian / Royal Caribbean", "role": "Exclusive 4-night Bahamas charter of an entire 3,000-guest vessel", "cost": 0.0, "retained": 4000000.0},
            {"node": "Charter Contracts Team", "entity": "Cruise Corporate Events & Charters", "role": "Custom contract with 100% non-refundable payment schedule, custom onboard branding", "cost": 50000.0, "retained": 3950000.0},
            {"node": "Enterprise Incentive Planner", "entity": "Fortune 500 Corporate Events Group", "role": "Organizes annual President's Club recognition trip for top sales performers", "cost": 0.0, "retained": 3950000.0},
            {"node": "Incentive Attendees", "entity": "3,000 Corporate Winners & Spouses", "role": "Attends all-inclusive corporate celebration with private island party", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_contract_value": 4000000.0,
            "internal_sales_legal_cost": 50000.0,
            "wire_clearing_fee": 2000.0,
            "cruise_net_received": 3948000.0,
            "distribution_friction_pct": 1.3,
            "net_yield_pct": 98.7
        },
        "tech_stack": "Enterprise Sales CRM (Salesforce) ➔ Custom Manifest Upload API ➔ Group Keycard Encoding System",
        "key_characteristics": "Lowest distribution cost in the entire cruise sector (<2%); 100% ship occupancy guaranteed; 0% cancellation risk (contractual penalty 100%)."
    },
    {
        "id": "cruise_path_9",
        "title": "Antarctic Expedition Cruise Journey",
        "formula": "Expedition Operator ➔ Direct Web / Specialist Agent ➔ Adventure Traveler",
        "category": "Polar & Remote Expedition",
        "ticket_example": 14000.0,
        "onboard_example": 1500.0,
        "steps": [
            {"node": "Expedition Operator", "entity": "Hurtigruten Expeditions / Ponant / Lindblad", "role": "PC6 ice-class expedition vessel sailing 12-day Antarctic Peninsula", "cost": 0.0, "retained": 15500.0},
            {"node": "Specialist Expedition Desk", "entity": "Polar Travel Specialist", "role": "Vets passenger medical fitness, validates polar gear requirements, receives 15% commission", "cost": 2100.0, "retained": 13400.0},
            {"node": "Adventure Traveler", "entity": "High-Net-Worth Explorer", "role": "Books voyage with kayak excursions, science lectures, and polar plunges", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 15500.0,
            "agent_commission": 2100.0,
            "tech_fee": 35.0,
            "card_fee": 341.0,
            "cruise_net_received": 13024.0,
            "distribution_friction_pct": 16.0,
            "net_yield_pct": 84.0
        },
        "tech_stack": "Expedition PSS ➔ Medical Clearance Portal ➔ Zodiac Dispatch Management",
        "key_characteristics": "Very high ticket prices ($10k-$30k+); rigorous medical pre-screening; heavy dependence on specialist adventure travel agencies."
    },
    {
        "id": "cruise_path_10",
        "title": "Outbound Personal Vacation Planner (PVP)",
        "formula": "Cruise Line CRM ➔ Outbound PVP Call Center ➔ Direct Past Guest",
        "category": "Direct Outbound Telesales",
        "ticket_example": 1900.0,
        "onboard_example": 850.0,
        "steps": [
            {"node": "Cruise Line CRM", "entity": "Carnival / NCL Customer Database", "role": "Identifies unbooked past guest who browsed Alaska sailings 3 times this week", "cost": 0.0, "retained": 2750.0},
            {"node": "Personal Vacation Planner (PVP)", "entity": "Shoreside Outbound Call Center Agent", "role": "Calls past guest directly with personalized cabin upgrade offer, earns $50 internal bonus", "cost": 50.0, "retained": 2700.0},
            {"node": "Past Guest", "entity": "Repeat Vacationer", "role": "Accepts phone offer, books balcony stateroom over the phone", "cost": 0.0, "retained": 0.0}
        ],
        "financial_summary": {
            "total_guest_spend": 2750.0,
            "pvp_internal_incentive": 50.0,
            "telephony_crm_cost": 15.0,
            "card_fee": 60.5,
            "cruise_net_received": 2624.5,
            "distribution_friction_pct": 4.6,
            "net_yield_pct": 95.4
        },
        "tech_stack": "Customer Data Platform (CDP) ➔ Predictive Outbound Dialer (Five9/Genesys) ➔ Cruise PSS",
        "key_characteristics": "High conversion on dormant past guests; costs a fraction of third-party agency commissions (under 5% friction)."
    }
]

# 5. Cruise Benchmark Matrix
benchmarks = [
    {
        "type": "Travel Advisors & Host Agencies",
        "key_players": "Cruise Planners, Avoya, Dream Vacations",
        "take_rate_pct": "12% - 16% of fare",
        "channel_share_pct": "35.5%",
        "cancellation_rate_pct": "8% - 12%",
        "lead_time_days": "180 - 270 days",
        "guest_data_ownership": "Shared with Agency",
        "pros": "Core distribution engine of cruise industry, sells complex multi-cabin family bookings",
        "cons": "High commission cost, requires constant trade marketing and agent training"
    },
    {
        "type": "Direct Brand.com & Mobile App",
        "key_players": "RoyalCaribbean.com, Carnival.com, NCL.com",
        "take_rate_pct": "2% - 3% (tech & card)",
        "channel_share_pct": "18.4%",
        "cancellation_rate_pct": "10% - 15%",
        "lead_time_days": "120 - 180 days",
        "guest_data_ownership": "100% Owned by Line",
        "pros": "Lowest distribution cost, 3x higher pre-cruise ancillary conversion, direct relationship",
        "cons": "Requires multi-million dollar television and digital ad budgets to drive traffic"
    },
    {
        "type": "Cruise Specialist OTAs",
        "key_players": "Vacations To Go, Cruise.com, CruisesOnly",
        "take_rate_pct": "10% - 14% of fare",
        "channel_share_pct": "18.4%",
        "cancellation_rate_pct": "14% - 18%",
        "lead_time_days": "60 - 120 days",
        "guest_data_ownership": "Masked / Shared",
        "pros": "Superb at clearing distressed, close-in shoulder season inventory",
        "cons": "Erodes price integrity via unapproved Onboard Credit (OBC) cash rebates"
    },
    {
        "type": "Big Box Retailers",
        "key_players": "Costco Travel, AAA / CAA Travel",
        "take_rate_pct": "8% - 11% blended",
        "channel_share_pct": "9.2%",
        "cancellation_rate_pct": "5% - 8%",
        "lead_time_days": "150 - 210 days",
        "guest_data_ownership": "Member Record Shared",
        "pros": "Access to high-net-worth warehouse club demographic, very low cancellation rate",
        "cons": "Requires exclusive value-add concessions (Costco Shop Cards, AAA member gifts)"
    },
    {
        "type": "Luxury Consortia",
        "key_players": "Virtuoso, Signature, Ensemble",
        "take_rate_pct": "15% - 18% + overrides",
        "channel_share_pct": "7.9%",
        "cancellation_rate_pct": "5% - 7%",
        "lead_time_days": "240 - 365 days",
        "guest_data_ownership": "Advisor Relationship",
        "pros": "Generates the highest ADRs in the industry, dominates world cruise suite sales",
        "cons": "Requires expensive consortia marketing fees and complimentary shipboard perks"
    },
    {
        "type": "Onboard Future Cruise Desks",
        "key_players": "NextCruise, Future Cruise Consultants",
        "take_rate_pct": "4% - 6% (bonus & admin)",
        "channel_share_pct": "5.3%",
        "cancellation_rate_pct": "4% - 6%",
        "lead_time_days": "300 - 450 days",
        "guest_data_ownership": "100% Owned",
        "pros": "Captures customer at the absolute peak of brand satisfaction while on ship",
        "cons": "Requires onboard staffing and credit assignment back to retail agents"
    },
    {
        "type": "Full-Ship Charters & Corporate MICE",
        "key_players": "Corporate Events, Theme Cruise Producers",
        "take_rate_pct": "1% - 2% (sales admin)",
        "channel_share_pct": "5.3%",
        "cancellation_rate_pct": "0% (100% non-refundable)",
        "lead_time_days": "365 - 730 days",
        "guest_data_ownership": "Corporate Manifest",
        "pros": "Guarantees 100% ship occupancy and revenue 12-24 months in advance",
        "cons": "Displaces regular loyal cruisers from preferred itineraries and dates"
    }
]

output_data = {
    "cruise_metrics": metrics,
    "nodes": nodes,
    "links": sankey_links,
    "revenue_cost_split": revenue_cost_split,
    "journey_archetypes": journey_archetypes,
    "intermediary_benchmarks": benchmarks
}

with open(os.path.join(cruise_dir, "data", "cruise_distribution_data.json"), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

with open(os.path.join(cruise_dir, "data", "channel_breakdown.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Source Node", "Target Node", "Value ($ Billions)", "Share of Global GBV (%)", "Flow Description"])
    for l in sankey_links:
        src_name = nodes[l["source"]]["name"]
        tgt_name = nodes[l["target"]]["name"]
        val = l["value"]
        pct = round((val / 38.0) * 100, 2)
        writer.writerow([src_name, tgt_name, val, f"{pct}%", l["label"]])

print("Cruise data generated successfully!")
