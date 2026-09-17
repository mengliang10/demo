"""
Builder for 3D, High-Performance & Scientific Graphics Tools (8 tools):
Datashader, Mayavi, VisPy, PyQtGraph, VTK, Glumpy, Manim, PyVista
Each tool gets completely different 3D/high-frequency engines, different charts, and real interactive engines!
"""

import os
import json
from .common_frame import render_tool_page
from data_cat2_scientific import TOOLS_CAT2

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SCRIPT_DIR, "Python Visualization, Graphical, & Interactive Libraries", "3D, High-Performance & Scientific Graphics")

def write_tool_output(tool_folder, html_content):
    target_dir = os.path.join(BASE_DIR, tool_folder)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    clean_name = tool_folder.lower().replace(" ", "_").replace(".", "_").replace("(", "").replace(")", "").replace("-", "_")
    with open(os.path.join(target_dir, f"{clean_name}_studio.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [✓] {tool_folder:<35} -> Dedicated Interactive Studio Built ({len(html_content)/1024:.1f} KB)")

def build_scientific_tools():
    tool_map = {t["folder"]: t for t in TOOLS_CAT2}

    build_datashader(tool_map["Datashader"])
    build_mayavi(tool_map["Mayavi"])
    build_vispy(tool_map["VisPy"])
    build_pyqtgraph(tool_map["PyQtGraph"])
    build_vtk(tool_map["VTK (Python bindings)"])
    build_glumpy(tool_map["Glumpy"])
    build_manim(tool_map["Manim (Mathematical Animation Engine)"])
    build_pyvista(tool_map["PyVista"])

# ==============================================================================
# 1. DATASHADER
# ==============================================================================
def build_datashader(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 10px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">DATASHADER NUMBA HDR RASTERIZER</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Transfer:</label>
        <select id="ds-how" onchange="renderDatashader()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="eq_hist" selected>how='eq_hist' (Equalized)</option>
          <option value="log">how='log' (Logarithmic)</option>
          <option value="linear">how='linear' (Raw Linear)</option>
        </select>
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Points:</label>
        <select id="ds-pts" onchange="resampleDatashader()" style="background:#070d09; color:#fff; border:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; padding:2px 6px; border-radius:4px;">
          <option value="25000">25,000 Points</option>
          <option value="60000" selected>60,000 Points</option>
          <option value="120000">120,000 Points</option>
        </select>
        <button class="btn-action" onclick="resampleDatashader()" style="font-size:0.7rem; padding:3px 8px;">Re-Aggregate</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#020403; display:flex; flex-direction:column; align-items:center; justify-content:center;">
      <canvas id="ds-canvas" width="640" height="460" style="border:1px solid rgba(255,255,255,0.1); border-radius:4px; max-width:100%; height:auto;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>agg = cvs.points(df, 'x', 'y'); img = tf.shade(agg, cmap=['#040705', '#00e676', '#f3cf65', '#ffffff'], how='eq_hist')</span>
      <span>Numba Parallel Grid Binning · Infinite Dynamic Range Equalization</span>
    </div>
    """

    custom_js = """
    let dsRawData = [];

    function generateDsData() {
      const n = parseInt(document.getElementById('ds-pts').value);
      dsRawData = new Float32Array(n * 2);
      // Generate synthetic multi-cluster urban mobility pings
      const centers = [
        { x: -0.8, y: -0.3, s: 0.25, weight: 0.4 },
        { x: 0.5, y: 0.6, s: 0.18, weight: 0.35 },
        { x: 0.2, y: -0.7, s: 0.35, weight: 0.25 }
      ];

      for (let i = 0; i < n; i++) {
        const r = Math.random();
        let c = centers[0];
        if (r > 0.75) c = centers[2];
        else if (r > 0.4) c = centers[1];

        // Box-Muller Gaussian
        const u1 = Math.max(1e-6, Math.random());
        const u2 = Math.random();
        const z0 = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
        const z1 = Math.sqrt(-2.0 * Math.log(u1)) * Math.sin(2.0 * Math.PI * u2);

        dsRawData[i*2] = c.x + z0 * c.s;
        dsRawData[i*2+1] = c.y + z1 * c.s;
      }
    }

    function resampleDatashader() {
      generateDsData();
      renderDatashader();
    }

    function renderDatashader() {
      const c = document.getElementById('ds-canvas');
      if (!c) return;
      const ctx = c.getContext('2d');
      const W = c.width; const H = c.height;

      // 1. Grid Aggregation (cvs.points)
      const grid = new Int32Array(W * H);
      const n = dsRawData.length / 2;

      for (let i = 0; i < n; i++) {
        const x = dsRawData[i*2];
        const y = dsRawData[i*2+1];
        const px = Math.floor(((x + 2.0) / 4.0) * W);
        const py = Math.floor(((y + 1.6) / 3.2) * H);
        if (px >= 0 && px < W && py >= 0 && py < H) {
          grid[py * W + px]++;
        }
      }

      // 2. Transfer Function (tf.shade with eq_hist, log, linear)
      const how = document.getElementById('ds-how').value;
      const imgData = ctx.createImageData(W, H);

      let maxCount = 1;
      for (let i = 0; i < grid.length; i++) {
        if (grid[i] > maxCount) maxCount = grid[i];
      }

      // Build CDF for eq_hist
      const cdf = new Float32Array(maxCount + 1);
      if (how === 'eq_hist') {
        const hist = new Int32Array(maxCount + 1);
        let nonZeroCount = 0;
        for (let i = 0; i < grid.length; i++) {
          if (grid[i] > 0) { hist[grid[i]]++; nonZeroCount++; }
        }
        let accum = 0;
        for (let v = 1; v <= maxCount; v++) {
          accum += hist[v];
          cdf[v] = accum / (nonZeroCount || 1);
        }
      }

      for (let p = 0; p < W * H; p++) {
        const cnt = grid[p];
        let norm = 0;
        if (cnt > 0) {
          if (how === 'eq_hist') {
            norm = cdf[cnt];
          } else if (how === 'log') {
            norm = Math.log1p(cnt) / Math.log1p(maxCount);
          } else {
            norm = cnt / maxCount;
          }
        }

        const idx = p * 4;
        if (norm === 0) {
          imgData.data[idx] = 4;
          imgData.data[idx+1] = 7;
          imgData.data[idx+2] = 5;
          imgData.data[idx+3] = 255;
        } else {
          // Viridis / Fire multi-gradient interpolation
          let r, g, b;
          if (norm < 0.35) {
            const t = norm / 0.35;
            r = Math.floor(0 * (1-t) + 0 * t);
            g = Math.floor(100 * (1-t) + 230 * t);
            b = Math.floor(80 * (1-t) + 118 * t);
          } else if (norm < 0.75) {
            const t = (norm - 0.35) / 0.4;
            r = Math.floor(0 * (1-t) + 243 * t);
            g = Math.floor(230 * (1-t) + 207 * t);
            b = Math.floor(118 * (1-t) + 101 * t);
          } else {
            const t = (norm - 0.75) / 0.25;
            r = Math.floor(243 * (1-t) + 255 * t);
            g = Math.floor(207 * (1-t) + 255 * t);
            b = Math.floor(101 * (1-t) + 255 * t);
          }
          imgData.data[idx] = r;
          imgData.data[idx+1] = g;
          imgData.data[idx+2] = b;
          imgData.data[idx+3] = 255;
        }
      }

      ctx.putImageData(imgData, 0, 0);

      // Coordinate axes
      ctx.strokeStyle = 'rgba(255,255,255,0.15)';
      ctx.strokeRect(0, 0, W, H);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px JetBrains Mono';
      ctx.fillText(`Aggregated Points: ${n.toLocaleString()}`, 15, 20);
      ctx.fillText(`Max Bin Count: ${maxCount}`, 15, 36);
      ctx.fillText(`Algorithm: Numba Parallel Multi-Core`, W - 220, 20);
    }

    window.addEventListener('load', () => {
      generateDsData();
      renderDatashader();
    });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 2. MAYAVI
# ==============================================================================
def build_mayavi(tool):
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 10px #00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">MAYAVI 3D VTK ISOSURFACE ORBIT</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Iso Level:</label>
        <input type="range" id="mayavi-iso" min="0.5" max="3.0" step="0.1" value="1.6" oninput="updateMayaviIso()" style="width:80px;">
        <button class="btn-action" onclick="toggleMayaviWire()" id="btn-my-wire" style="font-size:0.7rem; padding:3px 8px;">Wireframe</button>
        <button class="btn-action" onclick="toggleMayaviPlane()" id="btn-my-plane" style="font-size:0.7rem; padding:3px 8px;">Cut Plane</button>
      </div>
    </div>
    <div class="canvas-body" id="mayavi-stage" style="width:100%; height:100%; min-height:480px; position:relative;">
      <!-- Three.js Canvas Injected Here -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>from mayavi import mlab; mlab.contour3d(scalars, contours=8, transparent=True)</span>
      <span>VTK 3D Visualization Pipeline · Interactive Mouse Drag Orbit</span>
    </div>
    """

    custom_js = """
    let myScene, myCamera, myRenderer, myMesh, myCutPlane;
    let myWireframe = false;
    let myPlaneVisible = true;

    function initMayaviThree() {
      const container = document.getElementById('mayavi-stage');
      if (!container) return;

      myScene = new THREE.Scene();
      myScene.background = new THREE.Color(0x040705);

      myCamera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      myCamera.position.set(0, 8, 16);
      myCamera.lookAt(0, 0, 0);

      myRenderer = new THREE.WebGLRenderer({ antialias: true });
      myRenderer.setSize(container.clientWidth, container.clientHeight);
      myRenderer.setPixelRatio(window.devicePixelRatio);
      container.appendChild(myRenderer.domElement);

      // Lights
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
      myScene.add(ambientLight);
      const dirLight1 = new THREE.DirectionalLight(0x00e676, 1.2);
      dirLight1.position.set(10, 20, 10);
      myScene.add(dirLight1);
      const dirLight2 = new THREE.DirectionalLight(0x00e5ff, 0.8);
      dirLight2.position.set(-10, -10, -10);
      myScene.add(dirLight2);

      // Create Torus Knot Isosurface geometry
      const geom = new THREE.TorusKnotGeometry(4.5, 1.3, 120, 24, 2, 3);
      const mat = new THREE.MeshStandardMaterial({
        color: 0x00e676,
        roughness: 0.3,
        metalness: 0.6,
        wireframe: false,
        transparent: true,
        opacity: 0.92
      });
      myMesh = new THREE.Mesh(geom, mat);
      myScene.add(myMesh);

      // Cut Plane (VTK ImagePlaneWidget)
      const planeGeom = new THREE.PlaneGeometry(12, 12);
      const planeMat = new THREE.MeshBasicMaterial({
        color: 0xf3cf65,
        wireframe: true,
        transparent: true,
        opacity: 0.4
      });
      myCutPlane = new THREE.Mesh(planeGeom, planeMat);
      myCutPlane.rotation.x = Math.PI / 2;
      myScene.add(myCutPlane);

      // Interactive Mouse Orbit
      let isDragging = false;
      let prevMouse = { x: 0, y: 0 };
      container.addEventListener('mousedown', (e) => { isDragging = true; prevMouse = { x: e.clientX, y: e.clientY }; });
      window.addEventListener('mouseup', () => { isDragging = false; });
      container.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const dx = e.clientX - prevMouse.x;
        const dy = e.clientY - prevMouse.y;
        myMesh.rotation.y += dx * 0.01;
        myMesh.rotation.x += dy * 0.01;
        prevMouse = { x: e.clientX, y: e.clientY };
      });

      function animate() {
        requestAnimationFrame(animate);
        if (!isDragging) {
          myMesh.rotation.y += 0.004;
          myCutPlane.rotation.z += 0.002;
        }
        myRenderer.render(myScene, myCamera);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container) return;
        myCamera.aspect = container.clientWidth / container.clientHeight;
        myCamera.updateProjectionMatrix();
        myRenderer.setSize(container.clientWidth, container.clientHeight);
      });
    }

    function toggleMayaviWire() {
      myWireframe = !myWireframe;
      if (myMesh) myMesh.material.wireframe = myWireframe;
      document.getElementById('btn-my-wire').innerText = myWireframe ? 'Solid Surface' : 'Wireframe';
    }

    function toggleMayaviPlane() {
      myPlaneVisible = !myPlaneVisible;
      if (myCutPlane) myCutPlane.visible = myPlaneVisible;
    }

    function updateMayaviIso() {
      const scale = parseFloat(document.getElementById('mayavi-iso').value);
      if (myMesh) myMesh.scale.set(scale / 1.6, scale / 1.6, scale / 1.6);
    }

    window.addEventListener('load', () => { setTimeout(initMayaviThree, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 3. VISPY
# ==============================================================================
def build_vispy(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#d500f9; box-shadow:0 0 10px #d500f9;"></span>
        <span style="color:#d500f9; font-family:var(--font-mono); font-size:0.75rem;">VISPY HARDWARE GPU POINT VORTEX SHADER</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Particles: <span id="vispy-count-lbl">15,000</span></label>
        <button class="btn-action" onclick="toggleVispyAttractor()" id="btn-vp-att" style="font-size:0.7rem; padding:3px 8px;">Double Vortex</button>
        <button class="btn-action" onclick="resetVispyParticles()" style="font-size:0.7rem; padding:3px 8px;">Explode Reset</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#020403; display:flex; align-items:center; justify-content:center;">
      <canvas id="vispy-canvas" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>from vispy import scene; visuals.MarkersVisual(pos, face_color=colors, size=4)</span>
      <span>Direct OpenGL Vertex Buffer Objects (VBO) · 60 FPS GPU Shader Dispatch</span>
    </div>
    """

    custom_js = """
    let vpParticles = [];
    const NUM_PARTICLES = 15000;
    let doubleAttractor = false;

    function initVispyParticles() {
      vpParticles = [];
      for (let i = 0; i < NUM_PARTICLES; i++) {
        const angle = Math.random() * Math.PI * 2;
        const rad = 20 + Math.random() * 240;
        vpParticles.push({
          x: Math.cos(angle) * rad,
          y: Math.sin(angle) * rad,
          vx: -Math.sin(angle) * (1.2 + Math.random()),
          vy: Math.cos(angle) * (1.2 + Math.random()),
          color: (i % 3 === 0) ? '#d500f9' : (i % 3 === 1 ? '#00e5ff' : '#00e676')
        });
      }
    }
    initVispyParticles();

    function toggleVispyAttractor() {
      doubleAttractor = !doubleAttractor;
      document.getElementById('btn-vp-att').innerText = doubleAttractor ? 'Single Core' : 'Double Vortex';
    }

    function resetVispyParticles() {
      for (let p of vpParticles) {
        const a = Math.random() * Math.PI * 2;
        const spd = 4 + Math.random() * 8;
        p.x = 0; p.y = 0;
        p.vx = Math.cos(a) * spd;
        p.vy = Math.sin(a) * spd;
      }
    }

    function animateVispy() {
      const c = document.getElementById('vispy-canvas');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;
      const cx = W / 2; const cy = H / 2;

      // Motion blur trail fade
      ctx.fillStyle = 'rgba(2, 4, 3, 0.25)';
      ctx.fillRect(0, 0, W, H);

      const a1x = doubleAttractor ? cx - 120 : cx;
      const a2x = doubleAttractor ? cx + 120 : cx;

      for (let i = 0; i < NUM_PARTICLES; i++) {
        const p = vpParticles[i];
        const targetX = (i % 2 === 0 || !doubleAttractor) ? a1x : a2x;

        const dx = targetX - (cx + p.x);
        const dy = cy - (cy + p.y);
        const distSq = dx*dx + dy*dy + 400;
        const force = 320 / distSq;

        // Gravitational pull + orthogonal swirl
        p.vx += dx * force * 0.05 - dy * force * 0.12;
        p.vy += dy * force * 0.05 + dx * force * 0.12;

        p.vx *= 0.985;
        p.vy *= 0.985;
        p.x += p.vx;
        p.y += p.vy;

        const px = cx + p.x;
        const py = cy + p.y;
        if (px >= 0 && px < W && py >= 0 && py < H) {
          ctx.fillStyle = p.color;
          ctx.fillRect(px, py, 1.5, 1.5);
        }
      }

      requestAnimationFrame(animateVispy);
    }

    window.addEventListener('load', () => { setTimeout(animateVispy, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 4. PYQTGRAPH
# ==============================================================================
def build_pyqtgraph(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#ff1744; box-shadow:0 0 10px #ff1744;"></span>
        <span style="color:#ff1744; font-family:var(--font-mono); font-size:0.75rem;">PYQTGRAPH SUB-MILLISECOND TELEMETRY SCOPE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--emerald-neon);">Heart Rate: <strong id="pq-bpm">72</strong> BPM</span>
        <button class="btn-action" onclick="togglePqArrhythmia()" id="btn-pq-arr" style="font-size:0.7rem; padding:3px 8px;">Trigger PVC Spike</button>
        <button class="btn-action" onclick="togglePqStreaming()" id="btn-pq-run" style="font-size:0.7rem; padding:3px 8px;">Pause Stream</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#030504; display:flex; flex-direction:column; gap:8px;">
      <div style="flex:1; width:100%; position:relative;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--emerald-neon); margin-bottom:4px;">Channel I: High-Resolution Lead II ECG Electrocardiogram</div>
        <canvas id="pq-canvas-ecg" style="width:100%; height:calc(100% - 20px); min-height:220px;"></canvas>
      </div>
      <div style="height:170px; width:100%; position:relative;">
        <div style="font-family:var(--font-mono); font-size:0.68rem; color:var(--cyan-neon); margin-bottom:4px;">Channel II: Photoplethysmogram (PPG Pulse Oximetry) & SpO2</div>
        <canvas id="pq-canvas-ppg" style="width:100%; height:calc(100% - 20px);"></canvas>
      </div>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>import pyqtgraph as pg; p = pg.plot(); curve = p.plot(pen='g'); curve.setData(buffer)</span>
      <span>Qt C++ GraphicsView Scene Graph · Zero Garbage-Collection Overhead</span>
    </div>
    """

    custom_js = """
    let pqStreaming = true;
    let pqTime = 0;
    let triggerPvc = false;
    const ecgBuffer = new Array(500).fill(0);
    const ppgBuffer = new Array(500).fill(0);

    function togglePqStreaming() {
      pqStreaming = !pqStreaming;
      document.getElementById('btn-pq-run').innerText = pqStreaming ? 'Pause Stream' : 'Resume Stream';
      if (pqStreaming) requestAnimationFrame(pqLoop);
    }

    function togglePqArrhythmia() {
      triggerPvc = true;
    }

    function generateEcgSample(t) {
      const beatPhase = t % 1.0;
      let val = 0;
      if (beatPhase < 0.1) {
        val = 0.15 * Math.sin(beatPhase / 0.1 * Math.PI); // P wave
      } else if (beatPhase >= 0.18 && beatPhase < 0.21) {
        val = -0.15; // Q wave
      } else if (beatPhase >= 0.21 && beatPhase < 0.26) {
        val = triggerPvc ? 2.8 : 1.8; // R peak
        if (triggerPvc && beatPhase >= 0.25) triggerPvc = false;
      } else if (beatPhase >= 0.26 && beatPhase < 0.30) {
        val = -0.4; // S wave
      } else if (beatPhase >= 0.40 && beatPhase < 0.65) {
        val = 0.35 * Math.sin((beatPhase - 0.40) / 0.25 * Math.PI); // T wave
      }
      return val + (Math.random() - 0.5) * 0.04;
    }

    function pqLoop() {
      if (!pqStreaming) return;

      pqTime += 0.02;
      const ecgVal = generateEcgSample(pqTime);
      const ppgVal = Math.pow(Math.sin((pqTime * Math.PI - 0.4) % Math.PI), 2) * 1.2 + (Math.random() - 0.5)*0.02;

      ecgBuffer.push(ecgVal);
      ecgBuffer.shift();

      ppgBuffer.push(ppgVal);
      ppgBuffer.shift();

      drawPqCanvases();
      requestAnimationFrame(pqLoop);
    }

    function drawPqCanvases() {
      drawPqChannel('pq-canvas-ecg', ecgBuffer, '#00e676', 2.2);
      drawPqChannel('pq-canvas-ppg', ppgBuffer, '#00e5ff', 1.8);
    }

    function drawPqChannel(canvasId, buffer, strokeColor, scaleFactor) {
      const c = document.getElementById(canvasId);
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#070f0b';
      ctx.fillRect(0, 0, W, H);

      // Hospital Scope Grid
      ctx.strokeStyle = 'rgba(0, 230, 118, 0.08)';
      ctx.lineWidth = 1;
      for (let x = 0; x < W; x += 20) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
      for (let y = 0; y < H; y += 20) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }

      ctx.strokeStyle = strokeColor;
      ctx.lineWidth = 2;
      ctx.shadowColor = strokeColor;
      ctx.shadowBlur = 6;
      ctx.beginPath();

      const n = buffer.length;
      for (let i = 0; i < n; i++) {
        const px = (i / n) * W;
        const py = H * 0.65 - buffer[i] * (H * 0.28 * scaleFactor);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.shadowBlur = 0;
    }

    window.addEventListener('load', () => { requestAnimationFrame(pqLoop); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 5. VTK
# ==============================================================================
def build_vtk(tool):
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65; box-shadow:0 0 10px #f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">VTK 3D VOLUMETRIC STREAMLINE PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Streamlines:</label>
        <button class="btn-action" onclick="changeVtkFlow(16)" style="font-size:0.7rem; padding:3px 8px;">16 Tubes</button>
        <button class="btn-action" onclick="changeVtkFlow(32)" style="font-size:0.7rem; padding:3px 8px;">32 Tubes</button>
        <button class="btn-action" onclick="toggleVtkObstacle()" id="btn-vtk-obs" style="font-size:0.7rem; padding:3px 8px;">Obstacle Wire</button>
      </div>
    </div>
    <div class="canvas-body" id="vtk-stage" style="width:100%; height:100%; min-height:480px; position:relative;">
      <!-- Three.js Canvas Injected Here -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>tracer = vtk.vtkStreamTracer(); tube = vtk.vtkTubeFilter(); mapper.SetInputConnection(tube.GetOutputPort())</span>
      <span>C++ Core Pipeline Filter Architecture · Runge-Kutta 4 Numerical Integration</span>
    </div>
    """

    custom_js = """
    let vtkScene, vtkCamera, vtkRenderer, vtkTubesGroup, vtkObstacle;
    let vtkObstacleWire = false;

    function initVtkThree() {
      const container = document.getElementById('vtk-stage');
      if (!container) return;

      vtkScene = new THREE.Scene();
      vtkScene.background = new THREE.Color(0x040705);

      vtkCamera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      vtkCamera.position.set(0, 6, 15);
      vtkCamera.lookAt(0, 0, 0);

      vtkRenderer = new THREE.WebGLRenderer({ antialias: true });
      vtkRenderer.setSize(container.clientWidth, container.clientHeight);
      vtkRenderer.setPixelRatio(window.devicePixelRatio);
      container.appendChild(vtkRenderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
      vtkScene.add(ambientLight);
      const dirLight = new THREE.DirectionalLight(0xf3cf65, 1.2);
      dirLight.position.set(10, 15, 10);
      vtkScene.add(dirLight);

      // Blunt obstacle (Sphere in flow field)
      const obsGeom = new THREE.SphereGeometry(1.8, 32, 32);
      const obsMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4, metalness: 0.7 });
      vtkObstacle = new THREE.Mesh(obsGeom, obsMat);
      vtkScene.add(vtkObstacle);

      vtkTubesGroup = new THREE.Group();
      vtkScene.add(vtkTubesGroup);

      generateStreamTubes(24);

      // Interactive Mouse Orbit
      let isDragging = false;
      let prevMouse = { x: 0, y: 0 };
      container.addEventListener('mousedown', (e) => { isDragging = true; prevMouse = { x: e.clientX, y: e.clientY }; });
      window.addEventListener('mouseup', () => { isDragging = false; });
      container.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const dx = e.clientX - prevMouse.x;
        const dy = e.clientY - prevMouse.y;
        vtkScene.rotation.y += dx * 0.01;
        vtkScene.rotation.x += dy * 0.01;
        prevMouse = { x: e.clientX, y: e.clientY };
      });

      function animate() {
        requestAnimationFrame(animate);
        if (!isDragging) {
          vtkScene.rotation.y += 0.003;
        }
        vtkRenderer.render(vtkScene, vtkCamera);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container) return;
        vtkCamera.aspect = container.clientWidth / container.clientHeight;
        vtkCamera.updateProjectionMatrix();
        vtkRenderer.setSize(container.clientWidth, container.clientHeight);
      });
    }

    function generateStreamTubes(count) {
      while (vtkTubesGroup.children.length > 0) {
        vtkTubesGroup.remove(vtkTubesGroup.children[0]);
      }

      for (let i = 0; i < count; i++) {
        const yOffset = ((i / count) - 0.5) * 6;
        const zOffset = (Math.sin(i * 1.5)) * 3;

        const curvePts = [];
        for (let x = -8; x <= 8; x += 0.5) {
          // Flow around sphere potential flow
          const r = Math.sqrt(x*x + yOffset*yOffset + zOffset*zOffset);
          let yActual = yOffset;
          if (r < 3.2 && r > 0.1) {
            yActual = yOffset * (1.0 + (1.8*1.8*1.8) / (2 * r*r*r));
          }
          curvePts.push(new THREE.Vector3(x, yActual, zOffset));
        }

        const curve = new THREE.CatmullRomCurve3(curvePts);
        const tubeGeom = new THREE.TubeGeometry(curve, 32, 0.08, 8, false);
        const hue = (i / count) * 0.35 + 0.3; // emerald to cyan
        const tubeMat = new THREE.MeshStandardMaterial({
          color: new THREE.Color().setHSL(hue, 1.0, 0.5),
          roughness: 0.3,
          metalness: 0.5
        });
        const tubeMesh = new THREE.Mesh(tubeGeom, tubeMat);
        vtkTubesGroup.add(tubeMesh);
      }
    }

    function changeVtkFlow(n) { generateStreamTubes(n); }
    function toggleVtkObstacle() {
      vtkObstacleWire = !vtkObstacleWire;
      vtkObstacle.material.wireframe = vtkObstacleWire;
    }

    window.addEventListener('load', () => { setTimeout(initVtkThree, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 6. GLUMPY
# ==============================================================================
def build_glumpy(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e5ff;"></span>
        <span style="color:#00e5ff; font-family:var(--font-mono); font-size:0.75rem;">GLUMPY MODERN OPENGL / GLSL PIPELINE</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Freq: <span id="gl-freq-lbl">4.0</span></label>
        <input type="range" id="gl-freq" min="1.0" max="10.0" step="0.5" value="4.0" oninput="updateGlumpy()" style="width:70px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); margin-left:6px;">Warp:</label>
        <input type="range" id="gl-warp" min="0.1" max="2.0" step="0.1" value="0.8" oninput="updateGlumpy()" style="width:70px;">
        <button class="btn-action" onclick="toggleGlumpyPause()" id="btn-gl-run" style="font-size:0.7rem; padding:3px 8px;">Pause Shader</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#020403; display:flex; align-items:center; justify-content:center;">
      <canvas id="glumpy-canvas" width="600" height="420" style="border:1px solid rgba(255,255,255,0.1); border-radius:4px; max-width:100%; height:auto;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>from glumpy import app, gloo, gl; program['u_time'] = clock.time()</span>
      <span>Modern OpenGL 2.1+ Pipeline · Hardware Procedural GLSL Fragment Shader</span>
    </div>
    """

    custom_js = """
    let glRunning = true;
    let glTime = 0;

    function toggleGlumpyPause() {
      glRunning = !glRunning;
      document.getElementById('btn-gl-run').innerText = glRunning ? 'Pause Shader' : 'Resume Shader';
      if (glRunning) requestAnimationFrame(glumpyLoop);
    }

    function updateGlumpy() {
      document.getElementById('gl-freq-lbl').innerText = document.getElementById('gl-freq').value;
    }

    function glumpyLoop() {
      if (!glRunning) return;
      glTime += 0.03;

      const c = document.getElementById('glumpy-canvas');
      if (!c) return;
      const ctx = c.getContext('2d');
      const W = c.width; const H = c.height;

      const freq = parseFloat(document.getElementById('gl-freq').value);
      const warp = parseFloat(document.getElementById('gl-warp').value);

      const imgData = ctx.createImageData(W, H);
      const step = 2; // Render at 2x step for high framerate simulation

      for (let y = 0; y < H; y += step) {
        for (let x = 0; x < W; x += step) {
          const u = (x / W - 0.5) * freq;
          const v = (y / H - 0.5) * freq;

          // Domain warping simulation
          const qx = Math.sin(u + glTime) + Math.cos(v * warp);
          const qy = Math.cos(v + glTime) + Math.sin(u * warp);
          const val = Math.sin(u + qx * 1.5) * Math.cos(v + qy * 1.5);

          const r = Math.floor((Math.sin(val * 4.0) * 0.5 + 0.5) * 30);
          const g = Math.floor((val * 0.5 + 0.5) * 230);
          const b = Math.floor((Math.cos(val * 3.0) * 0.5 + 0.5) * 255);

          for (let dy = 0; dy < step; dy++) {
            for (let dx = 0; dx < step; dx++) {
              const idx = ((y + dy) * W + (x + dx)) * 4;
              imgData.data[idx] = r;
              imgData.data[idx+1] = g;
              imgData.data[idx+2] = b;
              imgData.data[idx+3] = 255;
            }
          }
        }
      }

      ctx.putImageData(imgData, 0, 0);
      requestAnimationFrame(glumpyLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(glumpyLoop); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 7. MANIM
# ==============================================================================
def build_manim(tool):
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f3cf65;"></span>
        <span style="color:#f3cf65; font-family:var(--font-mono); font-size:0.75rem;">MANIM MATHEMATICAL ANIMATION (3BLUE1BROWN)</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Epicycles: <span id="manim-epi-lbl">5</span></label>
        <input type="range" id="manim-epi" min="1" max="9" step="1" value="5" oninput="updateManimEpicycles()" style="width:70px;">
        <button class="btn-action" onclick="toggleManimPlay()" id="btn-mn-play" style="font-size:0.7rem; padding:3px 8px;">Pause Draw</button>
        <button class="btn-action" onclick="clearManimTrail()" style="font-size:0.7rem; padding:3px 8px;">Clear Path</button>
      </div>
    </div>
    <div class="canvas-body" style="padding:12px; background:#040705; display:flex; align-items:center; justify-content:center;">
      <canvas id="manim-stage" style="width:100%; height:100%; min-height:480px;"></canvas>
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>class FourierScene(Scene): def construct(self): self.play(Create(epicycles))</span>
      <span>Programmatic Vector Graphics · Complex Fourier Series Decomposition</span>
    </div>
    """

    custom_js = """
    let manimPlaying = true;
    let manimTheta = 0;
    const trailPoints = [];

    function toggleManimPlay() {
      manimPlaying = !manimPlaying;
      document.getElementById('btn-mn-play').innerText = manimPlaying ? 'Pause Draw' : 'Resume Draw';
      if (manimPlaying) requestAnimationFrame(manimLoop);
    }

    function clearManimTrail() { trailPoints.length = 0; }

    function updateManimEpicycles() {
      document.getElementById('manim-epi-lbl').innerText = document.getElementById('manim-epi').value;
      clearManimTrail();
    }

    function manimLoop() {
      if (!manimPlaying) return;
      manimTheta += 0.02;

      const c = document.getElementById('manim-stage');
      if (!c) return;
      c.width = c.clientWidth * window.devicePixelRatio;
      c.height = c.clientHeight * window.devicePixelRatio;
      const ctx = c.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      const W = c.clientWidth; const H = c.clientHeight;

      ctx.fillStyle = '#040705';
      ctx.fillRect(0, 0, W, H);

      let cx = W * 0.35;
      let cy = H * 0.5;

      const nCycles = parseInt(document.getElementById('manim-epi').value);

      // Draw Fourier rotating epicycles
      for (let i = 0; i < nCycles; i++) {
        const n = i * 2 + 1;
        const radius = (120 / (n * Math.PI)) * 2;
        const prevX = cx;
        const prevY = cy;

        cx += radius * Math.cos(n * manimTheta);
        cy += radius * Math.sin(n * manimTheta);

        // Circle
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(prevX, prevY, radius, 0, 2 * Math.PI);
        ctx.stroke();

        // Vector arrow
        ctx.strokeStyle = '#f3cf65';
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(cx, cy);
        ctx.stroke();
      }

      // Add to trail
      trailPoints.push({ x: cx, y: cy });
      if (trailPoints.length > 500) trailPoints.shift();

      // Lead line to right projection
      ctx.strokeStyle = 'rgba(0, 230, 118, 0.3)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(W * 0.65, cy);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw Pen tip
      ctx.fillStyle = '#00e676';
      ctx.beginPath();
      ctx.arc(cx, cy, 4, 0, 2*Math.PI);
      ctx.fill();

      // Draw Path Trail
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 2.5;
      ctx.shadowColor = '#00e676';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      for (let i = 0; i < trailPoints.length; i++) {
        if (i === 0) ctx.moveTo(trailPoints[i].x, trailPoints[i].y);
        else ctx.lineTo(trailPoints[i].x, trailPoints[i].y);
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Mathematical Annotation in Manim Style
      ctx.fillStyle = '#f8fafc';
      ctx.font = '14px Newsreader';
      ctx.fillText('f(t) = \\\\sum_{k=1}^N \\\\frac{4}{(2k-1)\\\\pi} \\\\sin((2k-1)\\\\omega t)', W * 0.55, 45);

      requestAnimationFrame(manimLoop);
    }

    window.addEventListener('load', () => { requestAnimationFrame(manimLoop); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)

# ==============================================================================
# 8. PYVISTA
# ==============================================================================
def build_pyvista(tool):
    extra_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
    canvas_html = """
    <div class="canvas-toolbar">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#00e676; box-shadow:0 0 10px #00e676;"></span>
        <span style="color:#00e676; font-family:var(--font-mono); font-size:0.75rem;">PYVISTA UNSTRUCTURED GRID & VON MISES STRESS</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <label style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted);">Deformation:</label>
        <input type="range" id="pv-deform" min="0.2" max="2.5" step="0.1" value="1.0" oninput="updatePvDeform()" style="width:70px;">
        <button class="btn-action" onclick="togglePvWire()" id="btn-pv-wire" style="font-size:0.7rem; padding:3px 8px;">Wireframe</button>
        <button class="btn-action" onclick="togglePvClip()" id="btn-pv-clip" style="font-size:0.7rem; padding:3px 8px;">Clip Filter</button>
      </div>
    </div>
    <div class="canvas-body" id="pyvista-stage" style="width:100%; height:100%; min-height:480px; position:relative;">
      <!-- Three.js Canvas Injected Here -->
    </div>
    <div style="padding:6px 14px; background:rgba(10,17,13,0.8); border-top:1px solid var(--border-faint); font-family:var(--font-mono); font-size:0.7rem; color:var(--text-dim); display:flex; justify-content:space-between;">
      <span>mesh = pv.read('beam.vtk'); p = pv.Plotter(); p.add_mesh(mesh, scalars='von_Mises', cmap='plasma')</span>
      <span>UnstructuredGrid Finite Element Analysis · Realtime GPU Shaded Mesh</span>
    </div>
    """

    custom_js = """
    let pvScene, pvCamera, pvRenderer, pvMesh;
    let pvWireframe = false;
    let pvClipped = false;

    function initPyvistaThree() {
      const container = document.getElementById('pyvista-stage');
      if (!container) return;

      pvScene = new THREE.Scene();
      pvScene.background = new THREE.Color(0x040705);

      pvCamera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      pvCamera.position.set(10, 8, 14);
      pvCamera.lookAt(0, 0, 0);

      pvRenderer = new THREE.WebGLRenderer({ antialias: true });
      pvRenderer.setSize(container.clientWidth, container.clientHeight);
      pvRenderer.setPixelRatio(window.devicePixelRatio);
      container.appendChild(pvRenderer.domElement);

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
      pvScene.add(ambientLight);
      const dirLight = new THREE.DirectionalLight(0x00e676, 1.2);
      dirLight.position.set(12, 16, 8);
      pvScene.add(dirLight);

      // Create Cantilever I-Beam with vertex color stress gradient
      const geom = new THREE.BoxGeometry(10, 2.5, 3.5, 20, 8, 8);

      // Apply von Mises stress color grading to vertices
      const pos = geom.attributes.position;
      const colors = [];
      for (let i = 0; i < pos.count; i++) {
        const x = pos.getX(i);
        const y = pos.getY(i);
        // Cantilever bending stress formula: sigma = M * y / I (highest near root x=-5 and outer fiber y=+/-1.25)
        const stress = (5 - x) * Math.abs(y) * 0.15;
        // Colormap plasma: purple -> red -> yellow
        const c = new THREE.Color().setHSL(0.75 - stress * 0.75, 1.0, 0.5);
        colors.push(c.r, c.g, c.b);
      }
      geom.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

      const mat = new THREE.MeshStandardMaterial({
        vertexColors: true,
        roughness: 0.35,
        metalness: 0.4,
        wireframe: false
      });
      pvMesh = new THREE.Mesh(geom, mat);
      pvScene.add(pvMesh);

      // Mouse Orbit
      let isDragging = false;
      let prevMouse = { x: 0, y: 0 };
      container.addEventListener('mousedown', (e) => { isDragging = true; prevMouse = { x: e.clientX, y: e.clientY }; });
      window.addEventListener('mouseup', () => { isDragging = false; });
      container.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const dx = e.clientX - prevMouse.x;
        const dy = e.clientY - prevMouse.y;
        pvMesh.rotation.y += dx * 0.01;
        pvMesh.rotation.x += dy * 0.01;
        prevMouse = { x: e.clientX, y: e.clientY };
      });

      function animate() {
        requestAnimationFrame(animate);
        if (!isDragging) {
          pvMesh.rotation.y += 0.004;
        }
        pvRenderer.render(pvScene, pvCamera);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container) return;
        pvCamera.aspect = container.clientWidth / container.clientHeight;
        pvCamera.updateProjectionMatrix();
        pvRenderer.setSize(container.clientWidth, container.clientHeight);
      });
    }

    function togglePvWire() {
      pvWireframe = !pvWireframe;
      if (pvMesh) pvMesh.material.wireframe = pvWireframe;
      document.getElementById('btn-pv-wire').innerText = pvWireframe ? 'Solid' : 'Wireframe';
    }

    function togglePvClip() {
      pvClipped = !pvClipped;
      if (pvMesh) {
        pvMesh.scale.x = pvClipped ? 0.5 : 1.0;
      }
    }

    function updatePvDeform() {
      const def = parseFloat(document.getElementById('pv-deform').value);
      if (pvMesh) {
        pvMesh.scale.y = def;
      }
    }

    window.addEventListener('load', () => { setTimeout(initPyvistaThree, 100); });
    """

    html = render_tool_page(tool["name"], tool["category"], tool["pip"], tool["docs"], tool["tagline"], tool["paradigms"],
                            extra_head_cdn=extra_cdn, custom_canvas_html=canvas_html, custom_js=custom_js)
    write_tool_output(tool["folder"], html)
