/**
 * Cruise Industry Distribution & Revenue Split Dashboard
 * Main Application Logic & Visualizations
 */

let globalData = null;
let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const res = await fetch('data/cruise_distribution_data.json');
    globalData = await res.json();
    
    initTabs();
    // Support direct linking to tabs via URL hash
    if (window.location.hash) {
      const tabId = window.location.hash.substring(1);
      const targetBtn = document.querySelector(".tab-btn[data-tab="" + tabId + ""]");
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
    console.error('Error loading cruise distribution data:', err);
  }
});

// Tab Switching
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

// Render Top KPI Metrics
function renderKPIs() {
  const m = globalData.cruise_metrics;
  document.getElementById('kpi-gbv').textContent = `$${m.global_gbv_billions.toFixed(1)}B`;
  document.getElementById('kpi-ticket-onboard').textContent = `$${m.ticket_revenue_billions.toFixed(1)}B / $${m.onboard_revenue_billions.toFixed(1)}B`;
  document.getElementById('kpi-friction').textContent = `$${m.total_distribution_cost_billions.toFixed(2)}B`;
  document.getElementById('kpi-net').textContent = `$${m.net_cruise_revenue_billions.toFixed(2)}B`;
  document.getElementById('kpi-agent-share').textContent = `${m.agent_intermediated_share_pct.toFixed(1)}%`;
}

// 1. Master Cruise 5-Tier Journey Sankey
function renderMasterSankey(filterMode) {
  const nodes = globalData.nodes;
  let links = globalData.links;

  if (filterMode === 'agents') {
    links = links.filter(l => l.source_id.includes('agent') || l.target_id.includes('agent') || l.source_id.includes('host') || l.target_id.includes('host'));
  } else if (filterMode === 'direct') {
    links = links.filter(l => l.source_id.includes('direct') || l.target_id.includes('direct') || l.source_id.includes('onboard') || l.target_id.includes('onboard'));
  } else if (filterMode === 'luxury') {
    links = links.filter(l => l.source_id.includes('lux') || l.target_id.includes('lux') || l.source_id.includes('consortia') || l.target_id.includes('consortia'));
  } else if (filterMode === 'ota') {
    links = links.filter(l => l.source_id.includes('ota') || l.target_id.includes('ota') || l.source_id.includes('big_box') || l.target_id.includes('big_box'));
  }

  const nodeLabels = nodes.map(n => `<b>${n.name}</b><br>$${n.value.toFixed(1)}B (${((n.value / 38.0) * 100).toFixed(1)}%)`);
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
      hovertemplate: '<b>%{label}</b><br>Cruise Throughput: $%{value}B<extra></extra>'
    },
    link: {
      source: links.map(l => l.source),
      target: links.map(l => l.target),
      value: links.map(l => l.value),
      color: linkColors,
      customdata: links.map(l => l.label),
      hovertemplate: '<b>%{source.label}</b> ➔ <b>%{target.label}</b><br>Volume: <b>$%{value}B USD</b><br>Path: %{customdata}<extra></extra>'
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

// 2. Financial Revenue & Cost Split (Cruise Waterfall)
function renderRevenueWaterfall() {
  const x = [
    "Gross Passenger Value (GBV)",
    "Travel Agency Commissions",
    "Cruise OTA Margins",
    "Consortia Overrides",
    "Big Box Cash-Cards/Rebates",
    "GDS & Tech Switch Fees",
    "Payment Processing",
    "Net Cruise Line Revenue",
    "Ship Crew Payroll & Manning",
    "Marine Fuel (HFO/MGO/LNG)",
    "Food & Beverage Hotel Supplies",
    "Port Taxes, Dues & Pilotage",
    "Ship Drydock & Maintenance",
    "Entertainment & Shows",
    "Marketing & Corporate G&A",
    "Cruise EBITDA (GOP)"
  ];

  const y = [
    38.0,
    -2.65,
    -0.85,
    -0.35,
    -0.25,
    -0.20,
    -0.45,
    0, // Net Revenue
    -4.80,
    -4.20,
    -3.10,
    -3.40,
    -3.80,
    -1.50,
    -2.30,
    0  // EBITDA Total
  ];

  const measure = [
    "absolute", "relative", "relative", "relative", "relative", "relative", "relative",
    "total",
    "relative", "relative", "relative", "relative", "relative", "relative", "relative",
    "total"
  ];

  const text = y.map((val, idx) => {
    if (idx === 0) return "$38.0B";
    if (idx === 7) return "$33.25B";
    if (idx === 15) return "$10.15B";
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
      text: "Global Cruise Industry Revenue to EBITDA Waterfall ($ Billions)",
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
    { name: "Gross Passenger Value ($38.0B)", color: "#3b82f6" },     // 0
    { name: "Ticket Fare ($25.0B)", color: "#06b6d4" },               // 1
    { name: "Onboard Spend ($13.0B)", color: "#8b5cf6" },             // 2
    { name: "Distribution Friction ($4.75B)", color: "#ef4444" },     // 3
    { name: "Net Cruise Revenue ($33.25B)", color: "#10b981" },       // 4
    { name: "Travel Agent Comm ($2.65B)", color: "#a855f7" },         // 5
    { name: "OTA & Big Box ($1.10B)", color: "#f97316" },             // 6
    { name: "Consortia & Tech ($1.00B)", color: "#ec4899" },          // 7
    { name: "Ship Crew Manning ($4.80B)", color: "#64748b" },         // 8
    { name: "Marine Fuel ($4.20B)", color: "#475569" },               // 9
    { name: "Port Dues & Taxes ($3.40B)", color: "#334155" },         // 10
    { name: "Food, F&B & Hotel ($3.10B)", color: "#1e293b" },         // 11
    { name: "Drydock & Maintenance ($3.80B)", color: "#0f172a" },     // 12
    { name: "Marketing & G&A ($3.80B)", color: "#1e1e24" },           // 13
    { name: "Cruise EBITDA ($10.15B)", color: "#22c55e" }             // 14
  ];

  const links = [
    { source: 0, target: 1, value: 25.0 },
    { source: 0, target: 2, value: 13.0 },
    
    { source: 1, target: 3, value: 4.75 },
    { source: 1, target: 4, value: 20.25 },
    { source: 2, target: 4, value: 13.0 }, // 0% commission on onboard spend!

    // Friction split
    { source: 3, target: 5, value: 2.65 },
    { source: 3, target: 6, value: 1.10 },
    { source: 3, target: 7, value: 1.00 },

    // Net split
    { source: 4, target: 8, value: 4.80 },
    { source: 4, target: 9, value: 4.20 },
    { source: 4, target: 10, value: 3.40 },
    { source: 4, target: 11, value: 3.10 },
    { source: 4, target: 12, value: 3.80 },
    { source: 4, target: 13, value: 3.80 },
    { source: 4, target: 14, value: 10.15 }
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

// 3. Cruise Archetypes Explorer
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

  renderCruiseBreakdownChart(item);
}

function renderCruiseBreakdownChart(item) {
  const summary = item.financial_summary;
  const guestPaid = summary.total_guest_spend || summary.total_contract_value;
  const cruiseNet = summary.cruise_net_received;
  const friction = guestPaid - cruiseNet;

  const data = [
    {
      x: ['Cruise Line Net Retained', 'Intermediary Friction'],
      y: [cruiseNet, friction],
      type: 'bar',
      marker: { color: ['#10b981', '#ef4444'] },
      text: [`$${cruiseNet.toFixed(2)} (${summary.net_yield_pct}%)`, `$${friction.toFixed(2)} (${summary.distribution_friction_pct}%)`],
      textposition: 'auto'
    }
  ];

  const layout = {
    title: {
      text: `Cruise Revenue Retention ($${guestPaid.toLocaleString()} Total Spend)`,
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

// 4. Benchmark Table
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

// 5. Cruise What-If Simulator
function initSimulator() {
  const directShiftSlider = document.getElementById('sim-direct-shift');
  const agentCommSlider = document.getElementById('sim-agent-comm');
  const nccfDeductionSlider = document.getElementById('sim-nccf-deduction');

  function calculateSimulation() {
    const directShift = parseFloat(directShiftSlider.value); // -10% to +15%
    const agentComm = parseFloat(agentCommSlider.value);     // 10% to 18%
    const nccfPct = parseFloat(nccfDeductionSlider.value);   // 10% to 30% of fare

    document.getElementById('val-direct-shift').textContent = `${directShift > 0 ? '+' : ''}${directShift}%`;
    document.getElementById('val-agent-comm').textContent = `${agentComm}%`;
    document.getElementById('val-nccf').textContent = `${nccfPct}% of fare`;

    const baseGBV = 38.0;
    const baseTicket = 25.0;
    const baseOnboard = 13.0;

    // Shift ticket revenue between Agency and Direct
    const baseAgentTicket = 19.0;
    const baseDirectTicket = 6.0;

    const shiftedTicket = (baseTicket * (directShift / 100.0));
    const newAgentTicket = Math.max(0, baseAgentTicket - shiftedTicket);
    const newDirectTicket = Math.max(0, baseDirectTicket + shiftedTicket);

    // Commission is paid on commissionable fare (Ticket minus NCCF)
    const commissionableFare = newAgentTicket * (1 - (nccfPct / 100.0));
    const newAgencyCommission = commissionableFare * (agentComm / 100.0);

    const directCost = newDirectTicket * 0.025; // 2.5% tech + card cost
    const otherFriction = 2.10; // OTAs, GDS, Consortia, Payment processing

    const newTotalFriction = newAgencyCommission + directCost + otherFriction;
    const newNetRevenue = baseGBV - newTotalFriction;
    const netSavings = 33.25 - newNetRevenue;

    document.getElementById('sim-result-savings').textContent = `${-netSavings >= 0 ? '+$' : '-$'}${Math.abs(netSavings).toFixed(2)}B`;
    document.getElementById('sim-result-net').textContent = `$${newNetRevenue.toFixed(2)}B`;
    document.getElementById('sim-result-friction').textContent = `$${newTotalFriction.toFixed(2)}B (${((newTotalFriction / baseGBV) * 100).toFixed(1)}%)`;

    // Per passenger swing (33.5M passengers)
    const perPaxDelta = (-netSavings * 1000.0) / 33.5;
    document.getElementById('sim-result-revpax').textContent = `${perPaxDelta >= 0 ? '+$' : '-$'}${Math.abs(perPaxDelta).toFixed(2)}`;
  }

  directShiftSlider.addEventListener('input', calculateSimulation);
  agentCommSlider.addEventListener('input', calculateSimulation);
  nccfDeductionSlider.addEventListener('input', calculateSimulation);

  calculateSimulation();
}
