/**
 * Tours, Activities & Experiences Distribution Dashboard
 * Main Application Logic & Visualizations
 */

let globalData = null;
let currentFilter = 'all';

async function init() {
  try {
    globalData = window.TOURS_DATA;
    if (!globalData) {
      const res = await fetch('data/tours_distribution_data.json');
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
    console.error('Error loading tours distribution data:', err);
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
  const m = globalData.tours_metrics;
  document.getElementById('kpi-gbv').textContent = `$${m.global_gbv_billions.toFixed(1)}B`;
  document.getElementById('kpi-direct-ota').textContent = `${m.direct_share_pct.toFixed(1)}% / ${m.ota_trade_share_pct.toFixed(1)}%`;
  document.getElementById('kpi-friction').textContent = `$${m.total_distribution_cost_billions.toFixed(1)}B`;
  document.getElementById('kpi-net').textContent = `$${m.net_operator_revenue_billions.toFixed(1)}B`;
  document.getElementById('kpi-take-rate').textContent = `${m.blended_distribution_take_rate_pct.toFixed(1)}%`;
}

function renderMasterSankey(filterMode) {
  const nodes = globalData.nodes;
  let links = globalData.links;

  if (filterMode === 'direct') {
    links = links.filter(l => l.source_id.includes('direct') || l.target_id.includes('direct'));
  } else if (filterMode === 'ota') {
    links = links.filter(l => l.source_id.includes('ota') || l.target_id.includes('ota'));
  } else if (filterMode === 'shorex') {
    links = links.filter(l => l.source_id.includes('shorex') || l.target_id.includes('shorex'));
  } else if (filterMode === 'dmc') {
    links = links.filter(l => l.source_id.includes('dmc') || l.target_id.includes('dmc'));
  } else if (filterMode === 'concierge') {
    links = links.filter(l => l.source_id.includes('concierge') || l.target_id.includes('concierge'));
  }

  const nodeLabels = nodes.map(n => `<b>${n.name}</b><br>$${n.value.toFixed(1)}B (${((n.value / 160.0) * 100).toFixed(1)}%)`);
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
      hovertemplate: '<b>%{label}</b><br>Experiences Throughput: $%{value}B<extra></extra>'
    },
    link: {
      source: links.map(l => l.source),
      target: links.map(l => l.target),
      value: links.map(l => l.value),
      color: linkColors,
      customdata: links.map(l => l.label),
      hovertemplate: '<b>%{source.label}</b> ➔ <b>%{target.label}</b><br>Flow: <b>$%{value}B USD</b><br>Channel: %{customdata}<extra></extra>'
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
    "Gross Experience Bookings (GBV)",
    "Experience OTA Commissions",
    "Cruise Shorex Markups",
    "ResTech Platform SaaS/Fees",
    "Payment Processing",
    "DMC Wholesale Markups",
    "Hotel Concierge Commissions",
    "Net Operator Revenue",
    "Tour Guides, Drivers & Staff",
    "Vehicles, Boats & Fuel",
    "National Park Entry & Permits",
    "Commercial Liability Insurance",
    "Basecamps, Docks & Rent",
    "Marketing & Corporate G&A",
    "Operator Operating Profit"
  ];

  const y = [
    160.0,
    -9.88,
    -5.40,
    -4.20,
    -4.56,
    -2.16,
    -1.20,
    0, // Net Revenue
    -38.5,
    -23.9,
    -15.9,
    -9.3,
    -7.9,
    -8.7,
    0  // EBITDA Total
  ];

  const measure = [
    "absolute", "relative", "relative", "relative", "relative", "relative", "relative",
    "total",
    "relative", "relative", "relative", "relative", "relative", "relative",
    "total"
  ];

  const text = y.map((val, idx) => {
    if (idx === 0) return "$160.0B";
    if (idx === 7) return "$132.6B";
    if (idx === 14) return "$28.4B";
    return `-$${Math.abs(val).toFixed(2)}B`;
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
      text: "Global Tours & Activities Revenue to EBITDA Waterfall ($ Billions)",
      font: { color: "#f9fafb", size: 16 }
    },
    paper_bgcolor: "transparent",
    plot_bgcolor: "transparent",
    font: {
      family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      color: "#9ca3af",
      size: 11
    },
    yaxis: { title: "Billions USD ($B)", gridcolor: "rgba(75, 85, 99, 0.25)" },
    xaxis: { tickangle: -30 },
    margin: { l: 60, r: 40, t: 60, b: 120 }
  };

  Plotly.react('revenue-waterfall-chart', [trace], layout, { responsive: true });
}

function renderCostSankey() {
  const nodes = [
    { name: "Gross Booking Value ($160.0B)", color: "#3b82f6" },       // 0
    { name: "Intermediary Friction ($27.4B)", color: "#ef4444" },      // 1
    { name: "Net Operator Revenue ($132.6B)", color: "#10b981" },      // 2
    { name: "OTA Commissions ($9.88B)", color: "#f97316" },           // 3
    { name: "Cruise Shorex Margin ($5.40B)", color: "#ec4899" },       // 4
    { name: "ResTech & Cards ($8.76B)", color: "#f59e0b" },            // 5
    { name: "DMC & Concierge ($3.36B)", color: "#a855f7" },            // 6
    { name: "Guides & Drivers ($38.5B)", color: "#64748b" },           // 7
    { name: "Vehicles, Boats & Fuel ($23.9B)", color: "#475569" },     // 8
    { name: "Parks & Permits ($15.9B)", color: "#334155" },            // 9
    { name: "Liability Insurance ($9.3B)", color: "#1e293b" },         // 10
    { name: "Docks & Rent ($7.9B)", color: "#0f172a" },                // 11
    { name: "Marketing & G&A ($8.7B)", color: "#1e1e24" },             // 12
    { name: "Operator Operating Profit ($28.4B)", color: "#22c55e" }   // 13
  ];

  const links = [
    { source: 0, target: 1, value: 27.4 },
    { source: 0, target: 2, value: 132.6 },

    // Friction split
    { source: 1, target: 3, value: 9.88 },
    { source: 1, target: 4, value: 5.40 },
    { source: 1, target: 5, value: 8.76 },
    { source: 1, target: 6, value: 3.36 },

    // Net split
    { source: 2, target: 7, value: 38.5 },
    { source: 2, target: 8, value: 23.9 },
    { source: 2, target: 9, value: 15.9 },
    { source: 2, target: 10, value: 9.3 },
    { source: 2, target: 11, value: 7.9 },
    { source: 2, target: 12, value: 8.7 },
    { source: 2, target: 13, value: 28.4 }
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

  renderTourBreakdownChart(item);
}

function renderTourBreakdownChart(item) {
  const summary = item.financial_summary;
  const guestPaid = summary.ticket_price || summary.total_guest_paid || summary.guest_paid_to_cruise || summary.trip_price || summary.contract_value || summary.imputed_retail_value;
  const operatorNet = summary.operator_net_received;
  const friction = guestPaid - operatorNet;

  const data = [
    {
      x: ['Operator Net Retained', 'Intermediary Friction'],
      y: [operatorNet, friction],
      type: 'bar',
      marker: { color: ['#10b981', '#ef4444'] },
      text: [`$${operatorNet.toFixed(2)} (${summary.net_yield_pct}%)`, `$${friction.toFixed(2)} (${summary.distribution_friction_pct}%)`],
      textposition: 'auto'
    }
  ];

  const layout = {
    title: {
      text: `Tour Operator Revenue Retention ($${guestPaid.toLocaleString()} Booking Price)`,
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
  const directShiftSlider = document.getElementById('sim-direct-shift');
  const otaCommSlider = document.getElementById('sim-ota-comm');
  const shorexMarkupSlider = document.getElementById('sim-shorex-markup');

  function calculateSimulation() {
    const directShift = parseFloat(directShiftSlider.value); // -10% to +20%
    const otaComm = parseFloat(otaCommSlider.value);         // 20% to 32%
    const shorexMarkup = parseFloat(shorexMarkupSlider.value); // 30% to 60%

    document.getElementById('val-direct-shift').textContent = `${directShift > 0 ? '+' : ''}${directShift}%`;
    document.getElementById('val-ota-comm').textContent = `${otaComm}%`;
    document.getElementById('val-shorex-markup').textContent = `${shorexMarkup}%`;

    const baseGBV = 160.0;
    const baseOtaVolume = 38.0;
    const baseDirectVolume = 90.0; // 50B offline + 40B online

    const shiftedVolume = baseGBV * (directShift / 100.0);
    const newDirectVolume = Math.max(0, baseDirectVolume + shiftedVolume);
    const newOtaVolume = Math.max(0, baseOtaVolume - shiftedVolume);

    const oldOtaCost = baseOtaVolume * 0.26; // 26% blended
    const newOtaCost = newOtaVolume * (otaComm / 100.0);
    const otaDelta = newOtaCost - oldOtaCost;

    const oldShorexCost = 5.40;
    const newShorexCost = 12.0 * (shorexMarkup / 100.0);
    const shorexDelta = newShorexCost - oldShorexCost;

    const baseFriction = 27.4;
    const newFriction = baseFriction + otaDelta + shorexDelta;
    const newNetRevenue = baseGBV - newFriction;
    const netSavings = newNetRevenue - 132.6;

    document.getElementById('sim-result-savings').textContent = `${netSavings >= 0 ? '+$' : '-$'}${Math.abs(netSavings).toFixed(2)}B`;
    document.getElementById('sim-result-net').textContent = `$${newNetRevenue.toFixed(1)}B`;
    document.getElementById('sim-result-friction').textContent = `$${newFriction.toFixed(1)}B (${((newFriction / baseGBV) * 100).toFixed(1)}%)`;

    // Per booking impact (1.4B bookings)
    const perBookingDelta = (netSavings * 1000.0) / 1400.0;
    document.getElementById('sim-result-booking').textContent = `${perBookingDelta >= 0 ? '+$' : '-$'}${Math.abs(perBookingDelta).toFixed(2)}`;
  }

  directShiftSlider.addEventListener('input', calculateSimulation);
  otaCommSlider.addEventListener('input', calculateSimulation);
  shorexMarkupSlider.addEventListener('input', calculateSimulation);

  calculateSimulation();
}
