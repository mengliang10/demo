/**
 * Hospitality Room Distribution & Revenue Split Dashboard
 * Main Application Logic & Visualizations
 */

let globalData = null;
let currentFilter = 'all';
let currentArchetypeIndex = 0;

async function init() {
  try {
    globalData = window.HOSPITALITY_DATA;
    if (!globalData) {
      const res = await fetch('data/hospitality_distribution_data.json');
      globalData = await res.json();
    }
    
    initTabs();
    // Support direct linking to tabs via URL hash
    if (window.location.hash) {
      const tabId = window.location.hash.substring(1);
      const targetBtn = document.querySelector('.tab-btn[data-tab="' + tabId + '"]');
      if (targetBtn) {
        targetBtn.click();
      }
    }
    renderKPIs();
    renderMasterSankey('all');
    renderRevenueWaterfall();
    renderCostSankey();
    renderArchetypeExplorer(0);
    renderBenchmarkTable();
    initSimulator();
  } catch (err) {
    console.error('Error loading hospitality distribution data:', err);
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

// Tab Switching Logic
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-tab');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
      }

      // Trigger Plotly relayout to ensure proper dimensions on tab reveal
      window.dispatchEvent(new Event('resize'));
    });
  });

  // Filter Buttons for Master Sankey
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.getAttribute('data-filter');
      renderMasterSankey(currentFilter);
    });
  });
}

// Render Top Metric Cards
function renderKPIs() {
  const m = globalData.global_metrics;
  document.getElementById('kpi-gbv').textContent = `$${m.global_gbv_billions.toFixed(1)}B`;
  document.getElementById('kpi-friction').textContent = `$${m.total_distribution_cost_billions.toFixed(1)}B`;
  document.getElementById('kpi-net').textContent = `$${m.net_hotel_revenue_billions.toFixed(1)}B`;
  document.getElementById('kpi-direct').textContent = `${m.direct_channel_share_pct.toFixed(1)}%`;
  document.getElementById('kpi-rate').textContent = `${m.blended_distribution_take_rate_pct.toFixed(1)}%`;
}

// 1. Master 5-Tier Journey Sankey
function renderMasterSankey(filterMode) {
  const nodes = globalData.nodes;
  let links = globalData.links;

  // Filter logic
  if (filterMode === 'direct') {
    const directKeywords = ['direct', 'loyalty', 'voice', 'walkin', 'portal', 'supply_'];
    links = links.filter(l => {
      return directKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  } else if (filterMode === 'corporate') {
    const corpKeywords = ['gds', 'tmc', 'corp', 'bedbanks'];
    links = links.filter(l => {
      return corpKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  } else if (filterMode === 'leisure') {
    const leisureKeywords = ['ota', 'leisure', 'tour_ops', 'direct_web', 'bedbanks'];
    links = links.filter(l => {
      return leisureKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  } else if (filterMode === 'wholesale') {
    const wsKeywords = ['bedbanks', 'tour_ops', 'pkg'];
    links = links.filter(l => {
      return wsKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  } else if (filterMode === 'luxury') {
    const luxKeywords = ['consortia', 'luxury', 'resort'];
    links = links.filter(l => {
      return luxKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  } else if (filterMode === 'mice') {
    const miceKeywords = ['group', 'mice', 'event'];
    links = links.filter(l => {
      return miceKeywords.some(k => l.source_id.includes(k) || l.target_id.includes(k));
    });
  }

  // Build Plotly Sankey trace
  const nodeLabels = nodes.map(n => `<b>${n.name}</b><br>$${n.value.toFixed(1)}B (${((n.value / 600.0) * 100).toFixed(1)}%)`);
  const nodeColors = nodes.map(n => n.color);

  // Link colors with transparency
  const linkColors = links.map(l => {
    const srcNode = nodes[l.source];
    return srcNode.color.replace(')', ', 0.35)').replace('rgb', 'rgba').replace('#', '');
  }).map(c => {
    // Hex to rgba conversion
    if (c.length === 6) {
      const r = parseInt(c.slice(0, 2), 16);
      const g = parseInt(c.slice(2, 4), 16);
      const b = parseInt(c.slice(4, 6), 16);
      return `rgba(${r}, ${g}, ${b}, 0.35)`;
    }
    return 'rgba(100, 116, 139, 0.35)';
  });

  const trace = {
    type: "sankey",
    orientation: "h",
    arrangement: "snap",
    valueformat: ".1f",
    valuesuffix: "B USD",
    node: {
      pad: 14,
      thickness: 20,
      line: { color: "rgba(255, 255, 255, 0.25)", width: 1 },
      label: nodeLabels,
      color: nodeColors,
      hovertemplate: '<b>%{label}</b><br>Throughput: $%{value}B<extra></extra>'
    },
    link: {
      source: links.map(l => l.source),
      target: links.map(l => l.target),
      value: links.map(l => l.value),
      color: linkColors,
      customdata: links.map(l => l.label),
      hovertemplate: '<b>%{source.label}</b> ➔ <b>%{target.label}</b><br>Flow: <b>$%{value}B USD</b><br>Type: %{customdata}<extra></extra>'
    }
  };

  const layout = {
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      size: 11,
      color: "#e2e8f0"
    },
    margin: { l: 20, r: 20, t: 25, b: 25 }
  };

  const config = {
    responsive: true,
    displayModeBar: true,
    modeBarButtonsToRemove: ['lasso2d', 'select2d']
  };

  Plotly.react('master-sankey-chart', [trace], layout, config);
}

// 2. Financial Revenue & Cost Split (Waterfall & Cost Sankey)
function renderRevenueWaterfall() {
  const data = globalData.revenue_cost_split;
  
  // Waterfall items
  const x = [
    "Gross Booking Value",
    "OTA Commissions",
    "Bedbank Markups",
    "GDS Fees",
    "TMC Fees",
    "Consortia/Agent Comm",
    "Metasearch Ad Spend",
    "Tech Stack (CRS/CM)",
    "Payment Processing",
    "Net Hotel Room Revenue",
    "Rooms Dept Labor & Ops",
    "Brand Franchise Royalty",
    "Property Ops & Utilities",
    "Sales & Marketing",
    "G&A, Taxes & Insurance",
    "Gross Operating Profit (GOP)"
  ];

  const y = [
    600.0,
    -35.1,
    -13.2,
    -4.8,
    -5.7,
    -4.5,
    -5.2,
    -4.2,
    -15.0,
    0, // Total
    -128.1,
    -46.1,
    -51.2,
    -35.9,
    -56.4,
    0  // Final Total
  ];

  const measure = [
    "absolute",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "total",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "total"
  ];

  const text = y.map((val, idx) => {
    if (idx === 0) return "$600.0B";
    if (idx === 9) return "$512.3B";
    if (idx === 15) return "$194.6B";
    return `-$${Math.abs(val).toFixed(1)}B`;
  });

  const trace = {
    type: "waterfall",
    orientation: "v",
    measure: measure,
    x: x,
    y: y,
    text: text,
    textposition: "outside",
    connector: { line: { color: "rgba(255, 255, 255, 0.25)" } },
    increasing: { marker: { color: "#3b82f6" } },
    decreasing: { marker: { color: "#ef4444" } },
    totals: { marker: { color: "#10b981" } }
  };

  const layout = {
    title: {
      text: "Global Hospitality Revenue to EBITDA Waterfall ($ Billions)",
      font: { color: "#f9fafb", size: 16 }
    },
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      color: "#9ca3af",
      size: 11
    },
    yaxis: {
      title: "Billions USD ($B)",
      gridcolor: "rgba(75, 85, 99, 0.25)",
      zerolinecolor: "rgba(75, 85, 99, 0.5)"
    },
    xaxis: {
      tickangle: -30
    },
    margin: { l: 60, r: 40, t: 60, b: 120 }
  };

  Plotly.react('revenue-waterfall-chart', [trace], layout, { responsive: true });
}

function renderCostSankey() {
  // Simplified corporate cost split sankey
  const nodes = [
    { name: "Gross Booking Value ($600.0B)", color: "#3b82f6" },       // 0
    { name: "Intermediary Distribution ($87.7B)", color: "#ef4444" },  // 1
    { name: "Net Hotel Revenue ($512.3B)", color: "#10b981" },         // 2
    { name: "OTA Commissions ($35.1B)", color: "#f97316" },           // 3
    { name: "Bedbank Markups ($13.2B)", color: "#ec4899" },            // 4
    { name: "GDS & TMC Fees ($10.5B)", color: "#a855f7" },             // 5
    { name: "Payment & Tech Fees ($19.2B)", color: "#f59e0b" },        // 6
    { name: "Metasearch & Agent ($9.7B)", color: "#06b6d4" },          // 7
    { name: "Rooms Dept Labor ($128.1B)", color: "#64748b" },          // 8
    { name: "Franchise Royalties ($46.1B)", color: "#475569" },        // 9
    { name: "POM & Utilities ($51.2B)", color: "#334155" },            // 10
    { name: "Sales & Marketing ($35.9B)", color: "#1e293b" },          // 11
    { name: "G&A, Taxes, Ins ($56.4B)", color: "#0f172a" },            // 12
    { name: "Gross Operating Profit ($194.6B)", color: "#22c55e" }     // 13
  ];

  const links = [
    { source: 0, target: 1, value: 87.7 },
    { source: 0, target: 2, value: 512.3 },
    
    // Split of Intermediary
    { source: 1, target: 3, value: 35.1 },
    { source: 1, target: 4, value: 13.2 },
    { source: 1, target: 5, value: 10.5 },
    { source: 1, target: 6, value: 19.2 },
    { source: 1, target: 7, value: 9.7 },

    // Split of Net Revenue
    { source: 2, target: 8, value: 128.1 },
    { source: 2, target: 9, value: 46.1 },
    { source: 2, target: 10, value: 51.2 },
    { source: 2, target: 11, value: 35.9 },
    { source: 2, target: 12, value: 56.4 },
    { source: 2, target: 13, value: 194.6 }
  ];

  const trace = {
    type: "sankey",
    orientation: "h",
    node: {
      pad: 12,
      thickness: 18,
      label: nodes.map(n => n.name),
      color: nodes.map(n => n.color)
    },
    link: {
      source: links.map(l => l.source),
      target: links.map(l => l.target),
      value: links.map(l => l.value),
      color: "rgba(148, 163, 184, 0.3)"
    }
  };

  const layout = {
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      color: "#e2e8f0",
      size: 11
    },
    margin: { l: 20, r: 20, t: 20, b: 20 }
  };

  Plotly.react('cost-sankey-chart', [trace], layout, { responsive: true });
}

// 3. Journey Pathway Explorer (10 Specific Archetypes)
function renderArchetypeExplorer(index) {
  currentArchetypeIndex = index;
  const archetypes = globalData.journey_archetypes;
  const item = archetypes[index];

  // Render buttons
  const selector = document.getElementById('pathway-buttons');
  selector.innerHTML = archetypes.map((a, i) => `
    <div class="pathway-btn ${i === index ? 'active' : ''}" onclick="renderArchetypeExplorer(${i})">
      <div class="pathway-btn-cat">${a.category}</div>
      <div class="pathway-btn-title">${a.title}</div>
      <div style="font-size: 0.72rem; color: #9ca3af;">${a.formula}</div>
    </div>
  `).join('');

  // Update Detail Card
  document.getElementById('arch-title').textContent = item.title;
  document.getElementById('arch-formula').textContent = item.formula;
  document.getElementById('arch-category').textContent = item.category;
  document.getElementById('arch-tech').textContent = item.tech_stack;
  document.getElementById('arch-char').textContent = item.key_characteristics;

  // Render Step Progression Box
  const stepsContainer = document.getElementById('arch-steps');
  stepsContainer.innerHTML = item.steps.map((step, idx) => `
    <div class="flow-step-box">
      <div style="font-size: 0.7rem; color: #9ca3af; text-transform: uppercase;">Step ${idx + 1}</div>
      <div style="font-weight: 700; color: #f9fafb; font-size: 0.95rem; margin-top: 0.2rem;">${step.node}</div>
      <div style="font-size: 0.8rem; color: #60a5fa; font-weight: 600;">${step.entity}</div>
      <div style="font-size: 0.75rem; color: #d1d5db; margin-top: 0.4rem;">${step.role}</div>
      ${step.cost > 0 ? `<div style="font-size: 0.75rem; color: #f87171; margin-top: 0.3rem;">Friction: -$${step.cost.toFixed(2)}</div>` : ''}
    </div>
    ${idx < item.steps.length - 1 ? '<div class="flow-step-arrow">➔</div>' : ''}
  `).join('');

  // Render ADR Dollar Breakdown Chart
  renderADRChart(item);
}

function renderADRChart(item) {
  const summary = item.financial_summary;
  const guestPaid = summary.guest_pays || summary.imputed_room_value || summary.negotiated_rate_paid || summary.group_rate_paid;
  const hotelNet = summary.hotel_net_received;
  const friction = guestPaid - hotelNet;

  const data = [
    {
      x: ['Hotel Net Retained', 'Intermediary Friction'],
      y: [hotelNet, friction],
      type: 'bar',
      marker: {
        color: ['#10b981', '#ef4444']
      },
      text: [`$${hotelNet.toFixed(2)} (${summary.net_yield_pct}%)`, `$${friction.toFixed(2)} (${summary.distribution_friction_pct}%)`],
      textposition: 'auto'
    }
  ];

  const layout = {
    title: {
      text: `Where does every dollar go? (Base ADR: $${guestPaid.toFixed(2)})`,
      font: { color: "#f9fafb", size: 14 }
    },
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      color: "#9ca3af",
      size: 11
    },
    yaxis: {
      title: "USD ($)",
      gridcolor: "rgba(75, 85, 99, 0.25)"
    },
    margin: { l: 50, r: 20, t: 50, b: 40 }
  };

  Plotly.react('adr-breakdown-chart', data, layout, { responsive: true });
}

// 4. Intermediary Benchmark Table
function renderBenchmarkTable() {
  const benchmarks = globalData.intermediary_benchmarks;
  const tbody = document.getElementById('benchmark-table-body');
  tbody.innerHTML = benchmarks.map(b => `
    <tr>
      <td style="font-weight: 600; color: #f9fafb;">${b.type}</td>
      <td style="color: #93c5fd;">${b.key_players}</td>
      <td><span class="badge-tag badge-orange">${b.take_rate_pct}</span></td>
      <td style="font-weight: 600;">${b.channel_share_pct}</td>
      <td><span class="badge-tag badge-purple">${b.cancellation_rate_pct}</span></td>
      <td>${b.lead_time_days}</td>
      <td><span class="badge-tag badge-green">${b.guest_data_ownership}</span></td>
      <td style="font-size: 0.78rem; color: #a7f3d0;">${b.pros}</td>
      <td style="font-size: 0.78rem; color: #fca5a5;">${b.cons}</td>
    </tr>
  `).join('');
}

// 5. What-If Sensitivity Simulator
function initSimulator() {
  const directShiftSlider = document.getElementById('sim-direct-shift');
  const otaCommSlider = document.getElementById('sim-ota-comm');
  const gdsFeeSlider = document.getElementById('sim-gds-fee');

  function calculateSimulation() {
    const directShift = parseFloat(directShiftSlider.value); // e.g. -10% to +15%
    const otaComm = parseFloat(otaCommSlider.value);         // e.g. 15% to 25%
    const gdsFee = parseFloat(gdsFeeSlider.value);           // e.g. $3 to $15

    document.getElementById('val-direct-shift').textContent = `${directShift > 0 ? '+' : ''}${directShift}%`;
    document.getElementById('val-ota-comm').textContent = `${otaComm}%`;
    document.getElementById('val-gds-fee').textContent = `$${gdsFee.toFixed(2)}`;

    // Baseline numbers
    const baseGBV = 600.0;
    const baseDirectGBV = 210.0;
    const baseOtaGBV = 195.0;
    const baseGdsGBV = 105.0;

    // Shift GBV from OTA to Direct
    const shiftedGBV = (baseGBV * (directShift / 100.0));
    const newDirectGBV = Math.max(0, baseDirectGBV + shiftedGBV);
    const newOtaGBV = Math.max(0, baseOtaGBV - shiftedGBV);

    // Costs
    const directCostRate = 0.035; // 3.5% direct cost (tech + meta + card)
    const otaCostRate = otaComm / 100.0;
    
    // GDS booking count (assume $150 ADR average, ~700M GDS room nights, ~2.5 nights per booking = 280M bookings)
    const gdsBookingsMillions = 280.0;
    const newGdsTotalCost = (gdsBookingsMillions * gdsFee) / 1000.0; // in Billions

    const baseFriction = globalData.global_metrics.total_distribution_cost_billions; // 87.7B
    
    // Calculate new friction
    const newOtaCost = newOtaGBV * otaCostRate;
    const baseOtaCost = baseOtaGBV * 0.18;
    const deltaOta = newOtaCost - baseOtaCost;

    const newDirectCost = newDirectGBV * directCostRate;
    const baseDirectCost = baseDirectGBV * directCostRate;
    const deltaDirect = newDirectCost - baseDirectCost;

    const baseGdsCost = 4.8;
    const deltaGds = newGdsTotalCost - baseGdsCost;

    const totalDeltaFriction = deltaOta + deltaDirect + deltaGds;
    const newTotalFriction = baseFriction + totalDeltaFriction;
    const newNetRevenue = baseGBV - newTotalFriction;
    const netSavings = 512.3 - newNetRevenue; // positive means savings

    document.getElementById('sim-result-savings').textContent = `${-netSavings >= 0 ? '+$' : '-$'}${Math.abs(netSavings).toFixed(2)}B`;
    document.getElementById('sim-result-net').textContent = `$${newNetRevenue.toFixed(1)}B`;
    document.getElementById('sim-result-friction').textContent = `$${newTotalFriction.toFixed(1)}B (${((newTotalFriction / baseGBV) * 100).toFixed(1)}%)`;

    // Net RevPAR Impact (assuming 4,250M room nights)
    const deltaPerRoomNight = (-netSavings * 1000.0) / 4250.0;
    document.getElementById('sim-result-revpar').textContent = `${deltaPerRoomNight >= 0 ? '+$' : '-$'}${Math.abs(deltaPerRoomNight).toFixed(2)}`;
  }

  directShiftSlider.addEventListener('input', calculateSimulation);
  otaCommSlider.addEventListener('input', calculateSimulation);
  gdsFeeSlider.addEventListener('input', calculateSimulation);

  calculateSimulation();
}
