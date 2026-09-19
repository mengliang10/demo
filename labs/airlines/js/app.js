/**
 * Commercial Airline Distribution & Economics Dashboard
 * Main Application Logic & Visualizations
 */

let globalData = null;
let currentFilter = 'all';

async function init() {
  try {
    globalData = window.AIRLINE_DATA;
    if (!globalData) {
      const res = await fetch('data/airline_distribution_data.json');
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
    console.error('Error loading airline distribution data:', err);
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

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
      window.dispatchEvent(new Event('resize'));
    });
  });

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

function renderKPIs() {
  const m = globalData.airline_metrics;
  document.getElementById('kpi-gbv').textContent = `$${m.global_gbv_billions.toFixed(1)}B`;
  document.getElementById('kpi-fare-ancillary').textContent = `$${m.base_fare_revenue_billions.toFixed(1)}B / $${m.ancillary_revenue_billions.toFixed(1)}B`;
  document.getElementById('kpi-friction').textContent = `$${m.total_distribution_cost_billions.toFixed(1)}B`;
  document.getElementById('kpi-net').textContent = `$${m.net_airline_revenue_billions.toFixed(1)}B`;
  document.getElementById('kpi-direct').textContent = `${m.direct_share_pct.toFixed(1)}%`;
}

function renderMasterSankey(filterMode) {
  const nodes = globalData.nodes;
  let links = globalData.links;

  if (filterMode === 'direct') {
    links = links.filter(l => l.source_id.includes('direct') || l.target_id.includes('direct'));
  } else if (filterMode === 'gds') {
    links = links.filter(l => l.source_id.includes('gds') || l.target_id.includes('gds'));
  } else if (filterMode === 'ndc') {
    links = links.filter(l => l.source_id.includes('ndc') || l.target_id.includes('ndc'));
  } else if (filterMode === 'corporate') {
    links = links.filter(l => l.source_id.includes('corp') || l.target_id.includes('corp') || l.source_id.includes('tmc') || l.target_id.includes('tmc'));
  } else if (filterMode === 'ota') {
    links = links.filter(l => l.source_id.includes('ota') || l.target_id.includes('ota'));
  }

  const nodeLabels = nodes.map(n => `<b>${n.name}</b><br>$${n.value.toFixed(1)}B (${((n.value / 800.0) * 100).toFixed(1)}%)`);
  const nodeColors = nodes.map(n => n.color);

  const linkColors = links.map(l => {
    const srcNode = nodes[l.source];
    let c = srcNode.color.replace('#', '');
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
      hovertemplate: '<b>%{source.label}</b> ➔ <b>%{target.label}</b><br>Volume: <b>$%{value}B USD</b><br>Route: %{customdata}<extra></extra>'
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

  Plotly.react('master-sankey-chart', [trace], layout, { responsive: true });
}

function renderRevenueWaterfall() {
  const x = [
    "Gross Passenger Booking Value",
    "Credit Card Interchange",
    "GDS Segment & Booking Fees",
    "TMC Overrides & Incentives",
    "OTA Commissions / Margins",
    "Metasearch Referrals (CPC)",
    "PSS & NDC Platform SaaS",
    "Net Airline Passenger Revenue",
    "Aviation Jet Fuel (A1/SAF)",
    "Flight & Maintenance Labor",
    "Aircraft Ownership & Leases",
    "Airport Landing & ATC Fees",
    "Maintenance, Repair & Overhaul",
    "In-Flight Catering & Services",
    "Selling & Corporate G&A",
    "Operating Profit (EBIT)"
  ];

  const y = [
    800.0,
    -18.0,
    -7.2,
    -6.4,
    -5.8,
    -4.8,
    -4.2,
    0, // Net Revenue
    -224.0,
    -192.0,
    -96.0,
    -72.0,
    -64.0,
    -24.0,
    -26.0,
    0  // EBIT Total
  ];

  const measure = [
    "absolute", "relative", "relative", "relative", "relative", "relative", "relative",
    "total",
    "relative", "relative", "relative", "relative", "relative", "relative", "relative",
    "total"
  ];

  const text = y.map((val, idx) => {
    if (idx === 0) return "$800.0B";
    if (idx === 7) return "$753.6B";
    if (idx === 15) return "$55.6B";
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
      text: "Global Airline Industry Revenue to EBIT Waterfall ($ Billions)",
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
      gridcolor: "rgba(75, 85, 99, 0.25)"
    },
    xaxis: { tickangle: -30 },
    margin: { l: 60, r: 40, t: 60, b: 120 }
  };

  Plotly.react('revenue-waterfall-chart', [trace], layout, { responsive: true });
}

function renderCostSankey() {
  const nodes = [
    { name: "Gross Passenger Value ($800.0B)", color: "#3b82f6" },     // 0
    { name: "Base Airfare ($640.0B)", color: "#06b6d4" },              // 1
    { name: "Ancillary Revenue ($160.0B)", color: "#8b5cf6" },         // 2
    { name: "Distribution Friction ($46.4B)", color: "#ef4444" },      // 3
    { name: "Net Airline Revenue ($753.6B)", color: "#10b981" },       // 4
    { name: "Card Interchange ($18.0B)", color: "#f59e0b" },          // 5
    { name: "GDS & TMC Fees ($13.6B)", color: "#a855f7" },             // 6
    { name: "OTA & Meta Spend ($10.6B)", color: "#f97316" },           // 7
    { name: "PSS & Tech SaaS ($4.2B)", color: "#ec4899" },             // 8
    { name: "Jet Fuel ($224.0B)", color: "#64748b" },                  // 9
    { name: "Flight & Maint Crew ($192.0B)", color: "#475569" },       // 10
    { name: "Aircraft Ownership ($96.0B)", color: "#334155" },         // 11
    { name: "Airport & ATC Fees ($72.0B)", color: "#1e293b" },         // 12
    { name: "MRO Maintenance ($64.0B)", color: "#0f172a" },           // 13
    { name: "Catering & G&A ($50.0B)", color: "#1e1e24" },             // 14
    { name: "Operating Profit EBIT ($55.6B)", color: "#22c55e" }       // 15
  ];

  const links = [
    { source: 0, target: 1, value: 640.0 },
    { source: 0, target: 2, value: 160.0 },
    
    { source: 1, target: 3, value: 46.4 },
    { source: 1, target: 4, value: 593.6 },
    { source: 2, target: 4, value: 160.0 }, // Near 100% direct ancillary retention!

    // Friction split
    { source: 3, target: 5, value: 18.0 },
    { source: 3, target: 6, value: 13.6 },
    { source: 3, target: 7, value: 10.6 },
    { source: 3, target: 8, value: 4.2 },

    // Net split
    { source: 4, target: 9, value: 224.0 },
    { source: 4, target: 10, value: 192.0 },
    { source: 4, target: 11, value: 96.0 },
    { source: 4, target: 12, value: 72.0 },
    { source: 4, target: 13, value: 64.0 },
    { source: 4, target: 14, value: 50.0 },
    { source: 4, target: 15, value: 55.6 }
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

function renderArchetypeExplorer(index) {
  const archetypes = globalData.journey_archetypes;
  const item = archetypes[index];

  const selector = document.getElementById('pathway-buttons');
  selector.innerHTML = archetypes.map((a, i) => `
    <div class="pathway-btn ${i === index ? 'active' : ''}" onclick="renderArchetypeExplorer(${i})">
      <div class="pathway-btn-cat">${a.category}</div>
      <div class="pathway-btn-title">${a.title}</div>
      <div style="font-size: 0.72rem; color: #9ca3af;">${a.formula}</div>
    </div>
  `).join('');

  document.getElementById('arch-title').textContent = item.title;
  document.getElementById('arch-formula').textContent = item.formula;
  document.getElementById('arch-category').textContent = item.category;
  document.getElementById('arch-tech').textContent = item.tech_stack;
  document.getElementById('arch-char').textContent = item.key_characteristics;

  const stepsContainer = document.getElementById('arch-steps');
  stepsContainer.innerHTML = item.steps.map((step, idx) => `
    <div class="flow-step-box">
      <div style="font-size: 0.7rem; color: #9ca3af; text-transform: uppercase;">Step ${idx + 1}</div>
      <div style="font-weight: 700; color: #f9fafb; font-size: 0.95rem; margin-top: 0.2rem;">${step.node}</div>
      <div style="font-size: 0.8rem; color: #38bdf8; font-weight: 600;">${step.entity}</div>
      <div style="font-size: 0.75rem; color: #d1d5db; margin-top: 0.4rem;">${step.role}</div>
      ${step.cost > 0 ? `<div style="font-size: 0.75rem; color: #f87171; margin-top: 0.3rem;">Friction: -$${step.cost.toFixed(2)}</div>` : ''}
    </div>
    ${idx < item.steps.length - 1 ? '<div class="flow-step-arrow">➔</div>' : ''}
  `).join('');

  renderAirlineBreakdownChart(item);
}

function renderAirlineBreakdownChart(item) {
  const summary = item.financial_summary;
  const guestPaid = summary.total_spend || summary.total_contract_value || summary.imputed_ticket_value;
  const airlineNet = summary.airline_net_received;
  const friction = guestPaid - airlineNet;

  const data = [
    {
      x: ['Airline Net Retained', 'Intermediary Friction'],
      y: [airlineNet, friction],
      type: 'bar',
      marker: { color: ['#10b981', '#ef4444'] },
      text: [`$${airlineNet.toFixed(2)} (${summary.net_yield_pct}%)`, `$${friction.toFixed(2)} (${summary.distribution_friction_pct}%)`],
      textposition: 'auto'
    }
  ];

  const layout = {
    title: {
      text: `Airline Passenger Revenue Yield ($${guestPaid.toLocaleString()} Total Ticket + Ancillary)`,
      font: { color: "#f9fafb", size: 14 }
    },
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      color: "#9ca3af",
      size: 11
    },
    yaxis: { title: "USD ($)", gridcolor: "rgba(75, 85, 99, 0.25)" },
    margin: { l: 60, r: 20, t: 50, b: 40 }
  };

  Plotly.react('adr-breakdown-chart', data, layout, { responsive: true });
}

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

function initSimulator() {
  const ndcShiftSlider = document.getElementById('sim-ndc-shift');
  const gdsFeeSlider = document.getElementById('sim-gds-fee');
  const ancillaryGrowthSlider = document.getElementById('sim-ancillary-growth');

  function calculateSimulation() {
    const ndcShift = parseFloat(ndcShiftSlider.value); // Shift from EDIFACT to NDC %
    const gdsFee = parseFloat(gdsFeeSlider.value);     // GDS segment fee $3 to $12
    const ancGrowth = parseFloat(ancillaryGrowthSlider.value); // Ancillary growth %

    document.getElementById('val-ndc-shift').textContent = `${ndcShift > 0 ? '+' : ''}${ndcShift}%`;
    document.getElementById('val-gds-fee').textContent = `$${gdsFee.toFixed(2)}`;
    document.getElementById('val-ancillary').textContent = `${ancGrowth > 0 ? '+' : ''}${ancGrowth}%`;

    const baseGBV = 800.0;
    const baseGdsVolume = 180.0; // $180B via GDS EDIFACT
    
    // GDS segments (~1.2B flight segments via GDS)
    const gdsSegments = 1200.0; // Million segments
    const shiftedSegments = gdsSegments * (ndcShift / 100.0);
    const newGdsSegments = Math.max(0, gdsSegments - shiftedSegments);

    const oldGdsCost = (gdsSegments * 6.0) / 1000.0; // $7.2B
    const newGdsCost = (newGdsSegments * gdsFee) / 1000.0;
    const gdsDelta = newGdsCost - oldGdsCost;

    // Ancillary expansion (95% margin retention)
    const ancillaryDelta = 160.0 * (ancGrowth / 100.0);
    const newGBV = baseGBV + ancillaryDelta;

    const baseFriction = 46.4;
    const newFriction = baseFriction + gdsDelta;
    const newNetRevenue = newGBV - newFriction;
    const netSavings = newNetRevenue - 753.6;

    document.getElementById('sim-result-savings').textContent = `${netSavings >= 0 ? '+$' : '-$'}${Math.abs(netSavings).toFixed(2)}B`;
    document.getElementById('sim-result-net').textContent = `$${newNetRevenue.toFixed(1)}B`;
    document.getElementById('sim-result-friction').textContent = `$${newFriction.toFixed(1)}B (${((newFriction / newGBV) * 100).toFixed(1)}%)`;

    // Per passenger swing (4.6B passengers)
    const perPaxDelta = (netSavings * 1000.0) / 4600.0;
    document.getElementById('sim-result-pax').textContent = `${perPaxDelta >= 0 ? '+$' : '-$'}${Math.abs(perPaxDelta).toFixed(2)}`;
  }

  ndcShiftSlider.addEventListener('input', calculateSimulation);
  gdsFeeSlider.addEventListener('input', calculateSimulation);
  ancillaryGrowthSlider.addEventListener('input', calculateSimulation);

  calculateSimulation();
}
