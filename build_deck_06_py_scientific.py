"""
Builder for Deck 06: Python Scientific, 3D & High-Performance Visualization
Generates 06-python-scientific-3d.html (20 distinct visual paradigms)
"""
import os
from template_engine import generate_deck_html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def build_deck():
    deck_meta = {
        'id': 'deck-06',
        'series_num': '06',
        'title': 'Python Scientific, 3D & High-Performance Visualization',
        'category': 'Scientific, 3D & WebGL',
        'subtitle': '20 High-Performance Scientific Paradigms across Datashader, Mayavi, VisPy, PyQtGraph, VTK, and Glumpy'
    }

    slides = [
        # 1. Datashader 10-Million Point HDR Cloud
        {
            'slide_id': 'slide-01-datashader-hdr',
            'tag': '01 / Out-of-Core Aggregation',
            'headline': 'Billion-Scale Point Rendering:',
            'headline_span': 'Datashader Perceptual HDR Cloud',
            'subtitle': 'Rasterizing tens of millions of raw coordinates into dynamic perceptual dynamic-range pixels with zero overplotting.',
            'library_badge': 'Datashader (Bokeh/Numba)',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; position:relative;">
                <svg viewBox="0 0 450 300" style="width:100%; max-height:340px; background:#040705; border-radius:8px; border:1px solid #00e676;">
                  <defs>
                    <radialGradient id="denseCore" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stop-color="#fffefa" stop-opacity="1"/>
                      <stop offset="15%" stop-color="#00e676" stop-opacity="0.9"/>
                      <stop offset="45%" stop-color="#0d5c36" stop-opacity="0.6"/>
                      <stop offset="85%" stop-color="#07180e" stop-opacity="0.2"/>
                      <stop offset="100%" stop-color="#040705" stop-opacity="0"/>
                    </radialGradient>
                  </defs>
                  <!-- HDR Density Core -->
                  <circle cx="225" cy="150" r="140" fill="url(#denseCore)"/>
                  <circle cx="225" cy="150" r="30" fill="#fff" opacity="0.8"/>
                  <text x="225" y="154" text-anchor="middle" fill="#040705" font-family="JetBrains Mono" font-size="10" font-weight="bold">10M Points</text>
                  <text x="20" y="30" fill="#00e676" font-family="JetBrains Mono" font-size="11">Logarithmic Equalized Transfer Function</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Raster-pixel histogram aggregation with histogram equalization (eq_hist): $I(x,y) = \\text{CDF}(C(x,y))$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Nationwide cell phone GPS pings, high-frequency limit order book depths, astrophysics N-body galactic simulations.'},
                {'title': 'Technical Strengths', 'desc': 'Renders 100,000,000 points without memory explosion or visual overplotting saturation.'}
            ],
            'metrics': [
                {'label': 'Capacity', 'val': '10M - 1B Points', 'sub': 'Out-of-Core'},
                {'label': 'Aggregation', 'val': 'Numba Parallel', 'sub': 'Multi-Core CPU/GPU'},
                {'label': 'Overplotting', 'val': 'Mathematically Zero', 'sub': 'Perceptual HDR'},
                {'label': 'Output', 'val': '2D Image Buffer', 'sub': 'RGB Raster'}
            ],
            'code_snippet': """import datashader as ds, datashader.transfer_functions as tf
cvs = ds.Canvas(plot_width=800, plot_height=600)
agg = cvs.points(df, 'lon', 'lat')
img = tf.shade(agg, cmap=color_key, how='eq_hist')"""
        },

        # 2. VisPy Real-Time 60-FPS Multi-Channel Oscilloscope Waterfall
        {
            'slide_id': 'slide-02-vispy-oscilloscope',
            'tag': '02 / OpenGL Shaders',
            'headline': '60-FPS Real-Time Telemetry:',
            'headline_span': 'VisPy GPU Multi-Channel Waterfall',
            'subtitle': 'Hardware-accelerated OpenGL shader pipeline rendering continuous multi-channel signal waterfalls.',
            'library_badge': 'VisPy OpenGL',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <svg viewBox="0 0 450 250" style="width:100%; max-height:280px; background:#050a07; border-radius:8px; border:1px solid #d4af37;">
                  <!-- 4 Channel Oscilloscope Traces -->
                  <g fill="none" stroke-width="2">
                    <path d="M 20 50 Q 80 20, 140 50 T 260 50 T 380 50 T 430 50" stroke="#00e676"/>
                    <path d="M 20 100 Q 70 80, 120 100 T 220 100 T 320 100 T 430 100" stroke="#f3cf65"/>
                    <path d="M 20 150 Q 90 120, 160 150 T 300 150 T 430 150" stroke="#00e5ff"/>
                    <path d="M 20 200 Q 60 180, 100 200 T 200 200 T 300 200 T 430 200" stroke="#ff1744"/>
                  </g>
                  <text x="30" y="45" fill="#00e676" font-family="JetBrains Mono" font-size="9">CH1: Sensor Alpha (60 FPS)</text>
                  <text x="30" y="95" fill="#f3cf65" font-family="JetBrains Mono" font-size="9">CH2: Sensor Beta</text>
                  <text x="30" y="145" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">CH3: Sensor Gamma</text>
                  <text x="30" y="195" fill="#ff1744" font-family="JetBrains Mono" font-size="9">CH4: Parity Alarms</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Direct OpenGL GLSL vertex shader attribute buffers streaming continuous floating-point audio/seismic arrays.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Neuroscience multi-electrode EEG arrays, real-time audio FFT telemetry, seismic fault monitoring.'},
                {'title': 'Technical Strengths', 'desc': 'Consumes near-zero CPU; graphics card handles all interpolation and line antialiasing.'}
            ],
            'metrics': [
                {'label': 'Engine', 'val': 'OpenGL ES 2.0', 'sub': 'Raw Shaders'},
                {'label': 'Refresh', 'val': '60.0 FPS Sync', 'sub': 'V-Sync Locked'},
                {'label': 'Channels', 'val': '128+ Streams', 'sub': 'Simultaneous'},
                {'label': 'CPU Overhead', 'val': '< 2% CPU', 'sub': 'GPU Offload'}
            ],
            'code_snippet': """from vispy import app, scene
canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
lines = scene.Line(pos=signal_data, color='#00e676', parent=view.scene)"""
        },

        # 3. Mayavi 3D Isosurface Extraction
        {
            'slide_id': 'slide-03-mayavi-isosurface',
            'tag': '03 / Volumetric Scalar Fields',
            'headline': 'Volumetric Scalar Fields:',
            'headline_span': 'Mayavi 3D Isosurface Extraction',
            'subtitle': 'Marching cubes algorithm extracting continuous equisurface boundaries from 3D scalar density tensors.',
            'library_badge': 'Mayavi (VTK-Python)',
            'chart_html': """
              <div id="mayavi-iso-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('mayavi-iso-stage');
                  if (!el || !window.Plotly) return;
                  const x = [], y = [], z = [], val = [];
                  for(let i=0; i<10; i++) {
                    for(let j=0; j<10; j++) {
                      for(let k=0; k<10; k++) {
                        const r = Math.sqrt((i-5)**2 + (j-5)**2 + (k-5)**2);
                        if (Math.abs(r - 3.5) < 0.8) {
                          x.push(i); y.push(j); z.push(k);
                          val.push(r);
                        }
                      }
                    }
                  }
                  Plotly.newPlot('mayavi-iso-stage', [{
                    type: 'scatter3d', mode: 'markers',
                    x: x, y: y, z: z,
                    marker: { size: 5, color: val, colorscale: 'Viridis' }
                  }], {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { color: '#9ba9a1' }, yaxis: { color: '#9ba9a1' }, zaxis: { color: '#f3cf65' },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.2 } }
                    }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Lorensen & Cline Marching Cubes algorithm: polygonizing implicit surface $F(x,y,z) = c$ in volumetric voxels.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Medical MRI brain segmentation, subterranean oil reservoir modeling, aerodynamic vortex cores.'},
                {'title': 'Technical Strengths', 'desc': 'Seamless Pythonic wrapper over Kitware VTK; instant rendering of complex topological shapes.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'Marching Cubes', 'sub': 'Isosurface'},
                {'label': 'Data Struct', 'val': '3D Scalar Grid', 'sub': 'Voxels (x,y,z)'},
                {'label': 'Framework', 'val': 'Mayavi + VTK', 'sub': 'Scientific C++'},
                {'label': 'Shading', 'val': 'Specular Phong', 'sub': 'Light Normals'}
            ],
            'code_snippet': """from mayavi import mlab
src = mlab.pipeline.scalar_field(scalar_tensor)
mlab.pipeline.iso_surface(src, contours=[0.2, 0.6], colormap='YlGn')
mlab.show()"""
        },

        # 4. VTK Volumetric Orthogonal Slicing of Medical Scans
        {
            'slide_id': 'slide-04-vtk-slicing',
            'tag': '04 / Orthogonal Planes',
            'headline': 'Multi-Planar Reconstruction:',
            'headline_span': 'VTK Orthogonal Slice Planes',
            'subtitle': 'Axial, sagittal, and coronal slice planes intersecting 3D clinical medical DICOM volumes.',
            'library_badge': 'Kitware VTK C++/Python',
            'chart_html': """
              <div style="width:100%; height:100%; display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; padding:15px; box-sizing:border-box;">
                <!-- Axial View -->
                <div style="background:#070d09; border:1px solid #00e676; border-radius:6px; padding:8px; display:flex; flex-direction:column; align-items:center;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#00e676;">Axial Plane (Z)</span>
                  <svg viewBox="0 0 100 100" style="width:80px; height:80px; margin-top:10px;">
                    <ellipse cx="50" cy="50" rx="35" ry="40" fill="#1b2822" stroke="#00e676"/>
                    <circle cx="50" cy="50" r="14" fill="#00e676" opacity="0.4"/>
                  </svg>
                </div>
                <!-- Sagittal View -->
                <div style="background:#070d09; border:1px solid #d4af37; border-radius:6px; padding:8px; display:flex; flex-direction:column; align-items:center;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65;">Sagittal Plane (X)</span>
                  <svg viewBox="0 0 100 100" style="width:80px; height:80px; margin-top:10px;">
                    <ellipse cx="50" cy="50" rx="30" ry="42" fill="#1b2822" stroke="#d4af37"/>
                    <rect x="40" y="35" width="20" height="30" fill="#d4af37" opacity="0.4"/>
                  </svg>
                </div>
                <!-- Coronal View -->
                <div style="background:#070d09; border:1px solid #00e5ff; border-radius:6px; padding:8px; display:flex; flex-direction:column; align-items:center;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#00e5ff;">Coronal Plane (Y)</span>
                  <svg viewBox="0 0 100 100" style="width:80px; height:80px; margin-top:10px;">
                    <ellipse cx="50" cy="50" rx="38" ry="32" fill="#1b2822" stroke="#00e5ff"/>
                    <ellipse cx="50" cy="50" rx="16" ry="12" fill="#00e5ff" opacity="0.4"/>
                  </svg>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Trilinear voxel interpolation $f(x,y,z)$ evaluated along arbitrary 3D cross-section cutting planes.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Radiology PACS software, surgical navigation digital twins, industrial CT materials defect scans.'},
                {'title': 'Technical Strengths', 'desc': 'Global gold standard for scientific visualization (used by ParaView, 3D Slicer, and ANSYS).'}
            ],
            'metrics': [
                {'label': 'Standard', 'val': 'DICOM / NIfTI', 'sub': 'Medical Gold Std'},
                {'label': 'Slicing', 'val': 'MPR Orthogonal', 'sub': 'Axial/Sag/Cor'},
                {'label': 'Interpolation', 'val': 'Trilinear Voxel', 'sub': 'Hardware Texture'},
                {'label': 'Core C++', 'val': 'VTK Pipeline', 'sub': 'Ultra Fast'}
            ],
            'code_snippet': """import vtk
reslice = vtk.vtkImageReslice()
reslice.SetInputData(reader.GetOutput())
reslice.SetResliceAxesDirectionCosines(1,0,0, 0,1,0, 0,0,1)"""
        },

        # 5. PyQtGraph High-Speed Telemetry Multi-Plot Real-Time Strip Chart
        {
            'slide_id': 'slide-05-pyqtgraph-telemetry',
            'tag': '05 / Embedded High-Speed UI',
            'headline': 'Sub-Millisecond GUI Plotting:',
            'headline_span': 'PyQtGraph Real-Time Multi-Plot',
            'subtitle': 'Qt/QGraphicsView C++ accelerated visualization updating charts at 120 FPS for live laboratory instrumentation.',
            'library_badge': 'PyQtGraph / Qt6',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; gap:8px; padding:15px; box-sizing:border-box;">
                <div style="background:#09100c; border:1px solid #00e676; border-radius:4px; height:65px; display:flex; align-items:center; padding:0 10px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#00e676; width:90px;">ADC Ch 01:</span>
                  <svg viewBox="0 0 300 40" style="flex:1; height:35px;">
                    <path d="M 0 20 L 50 5 L 80 35 L 140 10 L 220 30 L 300 15" fill="none" stroke="#00e676" stroke-width="2"/>
                  </svg>
                </div>
                <div style="background:#09100c; border:1px solid #d4af37; border-radius:4px; height:65px; display:flex; align-items:center; padding:0 10px;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65; width:90px;">ADC Ch 02:</span>
                  <svg viewBox="0 0 300 40" style="flex:1; height:35px;">
                    <path d="M 0 25 L 60 10 L 120 30 L 180 5 L 250 25 L 300 20" fill="none" stroke="#f3cf65" stroke-width="2"/>
                  </svg>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'PyQt QGraphicsScene scene-graph caching combined with NumPy memory-view slicing.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Semiconductor wafer testing equipment, rocket launch ground control consoles, EEG medical monitors.'},
                {'title': 'Technical Strengths', 'desc': 'Can plot live incoming data at over 100 FPS where Matplotlib would freeze the entire GUI.'}
            ],
            'metrics': [
                {'label': 'GUI Binding', 'val': 'PyQt6 / PySide6', 'sub': 'Native Desktop'},
                {'label': 'Frame Cadence', 'val': '120 FPS Burst', 'sub': 'Zero Lag'},
                {'label': 'NumPy Link', 'val': 'Zero-Copy Buffer', 'sub': 'Shared RAM'},
                {'label': 'Use Case', 'val': 'Lab Instruments', 'sub': 'Real-Time'}
            ],
            'code_snippet': """import pyqtgraph as pg
win = pg.GraphicsLayoutWidget(show=True)
p1 = win.addPlot(title="High-Speed ADC")
curve = p1.plot(pen='#00e676')
def update(): curve.setData(data_stream)"""
        },

        # 6. Glumpy GPU Shader-Based N-Body Galaxy
        {
            'slide_id': 'slide-06-glumpy-nbody',
            'tag': '06 / OpenGL Hardware Compute',
            'headline': 'Hardware Shader Compute:',
            'headline_span': 'Glumpy N-Body Particle Gravitation',
            'subtitle': 'Modern OpenGL (GLSL 4.0) pipeline simulating gravitational kinematics of 100,000 star particles directly on the GPU.',
            'library_badge': 'Glumpy OpenGL',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; position:relative;">
                <canvas id="nbody-canvas" width="450" height="300" style="background:#030604; border-radius:8px; border:1px solid #d4af37;"></canvas>
                <div style="position:absolute; bottom:14px; right:16px; background:rgba(7,12,9,0.85); padding:4px 10px; border-radius:4px; font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65;">
                  GLSL Spiral Galaxy &bull; 100k Stars
                </div>
              </div>
              <script>
              (function(){
                const canvas = document.getElementById('nbody-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                const stars = Array.from({length: 450}, () => {
                  const arm = Math.floor(Math.random() * 2);
                  const dist = Math.random() * 120 + 10;
                  const angle = dist / 25 + arm * Math.PI + (Math.random() - 0.5) * 0.4;
                  return { dist, angle, speed: 0.015 / Math.sqrt(dist/20) };
                });
                function animate() {
                  ctx.fillStyle = 'rgba(3, 6, 4, 0.18)';
                  ctx.fillRect(0, 0, canvas.width, canvas.height);
                  ctx.fillStyle = '#fffefa';
                  stars.forEach(s => {
                    s.angle += s.speed;
                    const x = canvas.width / 2 + Math.cos(s.angle) * s.dist;
                    const y = canvas.height / 2 + Math.sin(s.angle) * (s.dist * 0.6);
                    ctx.fillStyle = s.dist < 40 ? '#f3cf65' : (s.dist < 80 ? '#00e676' : '#00e5ff');
                    ctx.fillRect(x, y, 1.5, 1.5);
                  });
                  requestAnimationFrame(animate);
                }
                animate();
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Newtonian $N$-body gravitational kinematics evaluated via OpenGL compute / transform feedback shaders.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Astrophysics research, computational fluid dynamics (CFD), quantum molecular modeling.'},
                {'title': 'Technical Strengths', 'desc': 'Bridges NumPy arrays directly to GPU vertex attributes with zero serialization latency.'}
            ],
            'metrics': [
                {'label': 'Shader Level', 'val': 'Modern GLSL 4.0', 'sub': 'Compute Core'},
                {'label': 'Particle Max', 'val': '1,000,000 Pts', 'sub': 'Full Simulation'},
                {'label': 'Data Bridge', 'val': 'NumPy to VBO', 'sub': 'Zero Copy'},
                {'label': 'FPS', 'val': '60 FPS Ultra', 'sub': 'Hardware Sync'}
            ],
            'code_snippet': """from glumpy import app, gloo, gl
program = gloo.Program(vertex_shader, fragment_shader, count=100000)
program['position'] = numpy_coords
@window.event
def on_draw(dt): program.draw(gl.GL_POINTS)"""
        },

        # 7. Datashader Force-Directed Edge Bundling on 500k Nodes
        {
            'slide_id': 'slide-07-datashader-bundling',
            'tag': '07 / Big Graph Edge Bundling',
            'headline': 'Massive Graph Densities:',
            'headline_span': 'Datashader Edge Bundling',
            'subtitle': 'Fast force-directed edge bundling condensing half a million graph interconnections into clean structural arteries.',
            'library_badge': 'Datashader Bundling',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 380 260" style="width:100%; max-height:280px;">
                  <!-- Bundled Trunk Ribbons -->
                  <path d="M 60 130 C 140 90, 200 90, 320 60" fill="none" stroke="#00e676" stroke-width="4" opacity="0.8"/>
                  <path d="M 60 130 C 140 170, 200 170, 320 200" fill="none" stroke="#00e676" stroke-width="4" opacity="0.8"/>
                  <!-- Secondary sub-bundles -->
                  <path d="M 60 130 C 120 120, 180 120, 260 130" fill="none" stroke="#d4af37" stroke-width="2.5" opacity="0.6"/>
                  <!-- Core Cluster Points -->
                  <circle cx="60" cy="130" r="14" fill="#00e676"/>
                  <circle cx="320" cy="60" r="10" fill="#f3cf65"/>
                  <circle cx="320" cy="200" r="10" fill="#f3cf65"/>
                  <circle cx="260" cy="130" r="8" fill="#00e5ff"/>
                  <text x="60" y="165" text-anchor="middle" fill="#00e676" font-family="DM Sans" font-size="10" font-weight="bold">Core Hub (50k)</text>
                  <text x="320" y="45" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Branch A</text>
                  <text x="320" y="225" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Branch B</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Force-directed edge bundling (FDEB) treating edges as flexible springs attracting parallel trajectories.'},
                {'title': 'Enterprise Use Cases', 'desc': 'National airline flight corridor optimization, internet router backbone topology, banking wire transfers.'},
                {'title': 'Technical Strengths', 'desc': 'Datashader’s Numba compilation computes edge bundling across 500,000 edges in seconds instead of hours.'}
            ],
            'metrics': [
                {'label': 'Algorithm', 'val': 'FDEB Fast Numba', 'sub': 'Parallel Kernels'},
                {'label': 'Edge Capacity', 'val': '500,000 Edges', 'sub': 'Seconds Compute'},
                {'label': 'Hairball Drop', 'val': '-92% Visual Noise', 'sub': 'Artery Routing'},
                {'label': 'Integration', 'val': 'NetworkX + DShader', 'sub': 'PyData Suite'}
            ],
            'code_snippet': """from datashader.bundling import hammer_bundle
bundled_lines = hammer_bundle(nodes, edges, initial_bandwidth=0.05)
cvs.line(bundled_lines, 'x', 'y')"""
        },

        # 8. Mayavi 3D Vector Quivers in Aerodynamics
        {
            'slide_id': 'slide-08-mayavi-quiver',
            'tag': '08 / Aerodynamic Vortices',
            'headline': 'Turbulent Fluid Dynamics:',
            'headline_span': 'Mayavi 3D Quiver Vortices',
            'subtitle': '3D volumetric vector cones and streamtubes tracking velocity curl $(\\nabla \\times \\mathbf{v})$ in wake turbulence.',
            'library_badge': 'Mayavi mlab.quiver3d',
            'chart_html': """
              <div id="mayavi-quiver-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('mayavi-quiver-stage');
                  if (!el || !window.Plotly) return;
                  const x = [], y = [], z = [], u = [], v = [], w = [];
                  for(let i=0; i<6; i++) {
                    for(let j=0; j<6; j++) {
                      for(let k=0; k<6; k++) {
                        x.push(i); y.push(j); z.push(k);
                        u.push(-j + 2.5); v.push(i - 2.5); w.push(0.5);
                      }
                    }
                  }
                  Plotly.newPlot('mayavi-quiver-stage', [{
                    type: 'cone', x: x, y: y, z: z, u: u, v: v, w: w,
                    colorscale: 'Viridis', sizemode: 'scaled', sizeref: 0.8
                  }], {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { color: '#9ba9a1' }, yaxis: { color: '#9ba9a1' }, zaxis: { color: '#f3cf65' },
                      camera: { eye: { x: 1.4, y: 1.4, z: 1.2 } }
                    }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Vector vorticity calculation: $\\vec{\\omega} = \\nabla \\times \\vec{v}$ rendered as 3D oriented arrow/cone glyphs.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Aircraft wingtip vortex dissipation, wind turbine wake interactions, HVAC duct airflow.'},
                {'title': 'Technical Strengths', 'desc': 'Glyph scaling proportional to local velocity vector magnitude; customizable directional cones.'}
            ],
            'metrics': [
                {'label': 'Glyph Type', 'val': 'Oriented 3D Cones', 'sub': 'Direction + Mag'},
                {'label': 'Vorticity', 'val': 'Curl Operator', 'sub': 'Vortex Cores'},
                {'label': 'Engine', 'val': 'VTK Glyph3D', 'sub': 'C++ Acceleration'},
                {'label': 'Interactivity', 'val': 'Full 3D Orbit', 'sub': 'Quaternion'}
            ],
            'code_snippet': """from mayavi import mlab
mlab.quiver3d(x, y, z, u, v, w, colormap='hot', scale_factor=0.5)
mlab.show()"""
        },

        # 9. VTK Finite Element Analysis (FEA) Stress Map
        {
            'slide_id': 'slide-09-vtk-fea',
            'tag': '09 / Structural Mechanics',
            'headline': 'Continuum Solid Mechanics:',
            'headline_span': 'VTK Finite Element Stress Tensor',
            'subtitle': 'Von Mises yield stress tensor mapped across unstructured tetrahedral solid meshes under mechanical load.',
            'library_badge': 'Kitware VTK UnstructuredGrid',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Structural I-Beam under load -->
                  <!-- Top Flange -->
                  <rect x="50" y="40" width="250" height="24" fill="#00e676" stroke="#fff" stroke-width="1"/>
                  <!-- Web with Stress Concentration -->
                  <rect x="150" y="64" width="50" height="110" fill="url(#feaGrad)" stroke="#fff" stroke-width="1"/>
                  <!-- Bottom Flange -->
                  <rect x="50" y="174" width="250" height="24" fill="#00e676" stroke="#fff" stroke-width="1"/>
                  <!-- Stress Hotspot (Red Core) -->
                  <circle cx="175" cy="119" r="16" fill="#ff1744" opacity="0.9" filter="drop-shadow(0 0 8px #ff1744)"/>
                  <text x="175" y="123" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9" font-weight="bold">380 MPa</text>
                  <!-- Gradient definition -->
                  <defs>
                    <linearGradient id="feaGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#00e676"/>
                      <stop offset="50%" stop-color="#ffab00"/>
                      <stop offset="100%" stop-color="#00e676"/>
                    </linearGradient>
                  </defs>
                  <text x="175" y="225" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Von Mises Critical Shear Zone</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Von Mises equivalent stress calculation from Cauchy stress tensor: $\\sigma_v = \\sqrt{\\frac{1}{2}[(\\sigma_{11}-\\sigma_{22})^2 + \\dots + 6\\sigma_{12}^2]}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Civil structural building foundation integrity, aerospace fuselage pressure tests, bridge engineering.'},
                {'title': 'Technical Strengths', 'desc': 'Unstructured grid data model supports arbitrary tetrahedral, hexahedral, and pyramid finite elements.'}
            ],
            'metrics': [
                {'label': 'Stress Metric', 'val': 'Von Mises (MPa)', 'sub': 'Equivalent Shear'},
                {'label': 'Element Type', 'val': 'Tetrahedral / Hex', 'sub': 'UnstructuredGrid'},
                {'label': 'Standard', 'val': 'ANSYS / Nastran', 'sub': 'CAE Benchmark'},
                {'label': 'Solver Bridge', 'val': 'VTK Python C++', 'sub': 'Hardware Shaded'}
            ],
            'code_snippet': """grid = vtk.vtkUnstructuredGrid()
grid.GetPointData().SetScalars(vonMisesStressArray)
mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(grid)"""
        },

        # 10. VisPy 3D LiDAR Terrain Point Cloud
        {
            'slide_id': 'slide-10-vispy-lidar',
            'tag': '10 / GPU Point Cloud Canvas',
            'headline': 'High-Density Terrain Scans:',
            'headline_span': 'VisPy 3D LiDAR Shader Mesh',
            'subtitle': 'Streaming raw airborne LiDAR point clouds at native 60 FPS with distance-to-canopy color shaders.',
            'library_badge': 'VisPy SceneGraph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Slanted Point Cloud Plane -->
                  <g fill="#00e676" opacity="0.8">
                    <circle cx="80" cy="180" r="2.5"/> <circle cx="110" cy="170" r="2.5"/> <circle cx="140" cy="165" r="2.5"/>
                    <circle cx="90" cy="150" r="2.5"/> <circle cx="130" cy="140" r="2.5"/> <circle cx="170" cy="130" r="2.5"/>
                    <circle cx="120" cy="120" r="2.5"/> <circle cx="160" cy="100" r="2.5"/> <circle cx="200" cy="95" r="2.5"/>
                  </g>
                  <g fill="#d4af37" opacity="0.9">
                    <!-- Tree canopy elevated points -->
                    <circle cx="150" cy="80" r="3.5"/> <circle cx="160" cy="65" r="4"/> <circle cx="175" cy="70" r="4.5"/>
                    <circle cx="165" cy="85" r="3.5"/> <circle cx="155" cy="95" r="3"/>
                  </g>
                  <g fill="#00e5ff" opacity="0.9">
                    <!-- High mountain ridge -->
                    <circle cx="240" cy="50" r="3"/> <circle cx="270" cy="40" r="3.5"/> <circle cx="300" cy="35" r="4"/>
                  </g>
                  <text x="175" y="225" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="10">2.5M Pulses &bull; Native 60 FPS VisPy Scene</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'OpenGL Instanced vertex rendering using VisPy SceneGraph Visuals pipeline with custom GLSL depth shaders.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Autonomous vehicle driving point-clouds (Velodyne / Luminar), forestry canopy density audits.'},
                {'title': 'Technical Strengths', 'desc': 'Seamless mouse rotation, panning, and fly-through navigation directly inside a lightweight Python GUI.'}
            ],
            'metrics': [
                {'label': 'Throughput', 'val': '5M+ Points / sec', 'sub': 'GPU Pipeline'},
                {'label': 'Shader', 'val': 'Custom GLSL', 'sub': 'Elevation Depth'},
                {'label': 'Camera', 'val': 'Turntable / Arcball', 'sub': 'Intuitive Orbit'},
                {'label': 'Language', 'val': 'Python + Modern GL', 'sub': 'VisPy'}
            ],
            'code_snippet': """from vispy.scene import visuals
scatter = visuals.Markers()
scatter.set_data(lidar_xyz, edge_color=None, face_color=colors, size=2)
view.add(scatter)"""
        },

        # 11. Datashader Geospatial OpenStreetMap GPS Trace Density Aggregation
        {
            'slide_id': 'slide-11-datashader-gps',
            'tag': '11 / Continental Telemetry',
            'headline': 'Continental Trace Density:',
            'headline_span': 'Datashader OpenStreetMap Aggregates',
            'subtitle': 'Millions of vehicular GPS coordinates rasterized across national road networks with zero downsampling loss.',
            'library_badge': 'Datashader Geo',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px; background:#070d09; border-radius:6px;">
                  <!-- Road Network Lines radiating -->
                  <g stroke="#00e676" stroke-width="1.5" opacity="0.6">
                    <line x1="175" y1="120" x2="60" y2="40"/>
                    <line x1="175" y1="120" x2="290" y2="50"/>
                    <line x1="175" y1="120" x2="80" y2="200"/>
                    <line x1="175" y1="120" x2="270" y2="210"/>
                  </g>
                  <!-- Central Urban Highway Hub (Bright White-Gold Core) -->
                  <circle cx="175" cy="120" r="18" fill="#fffefa" opacity="0.95" filter="drop-shadow(0 0 10px #f3cf65)"/>
                  <text x="175" y="124" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">Metro Hub</text>
                  <text x="175" y="230" text-anchor="middle" fill="#d4af37" font-family="JetBrains Mono" font-size="10">8.4 Million GPS Traces Aggregated</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Coordinate projection into Web Mercator pixels followed by 2D binning aggregation into NumPy float arrays.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Nationwide fleet movement density, cell tower roaming paths, consumer mobility catchment tracking.'},
                {'title': 'Technical Strengths', 'desc': 'Generates high-resolution tile servers directly from raw multi-gigabyte Parquet datasets.'}
            ],
            'metrics': [
                {'label': 'Data Format', 'val': 'Apache Parquet', 'sub': 'Fast Columnar'},
                {'label': 'Resolution', 'val': 'Sub-Meter Grid', 'sub': 'No Pixel Blur'},
                {'label': 'Tile Engine', 'val': 'Dynamic Slippy', 'sub': 'XYZ Web Map'},
                {'label': 'Speed', 'val': '< 800 ms Render', 'sub': 'Numba JIT'}
            ],
            'code_snippet': """cvs = ds.Canvas(plot_width=1000, plot_height=800, x_range=x_range, y_range=y_range)
agg = cvs.line(df, 'x', 'y', agg=ds.count())
img = tf.shade(agg, cmap=fire)"""
        },

        # 12. PyQtGraph Real-Time 2D FFT Spectrogram
        {
            'slide_id': 'slide-12-pyqtgraph-spectrogram',
            'tag': '12 / Time-Frequency Analysis',
            'headline': 'Spectral Analysis:',
            'headline_span': 'PyQtGraph Real-Time FFT Spectrogram',
            'subtitle': 'Sliding Short-Time Fourier Transform (STFT) displaying acoustic frequency spectrum cascades live at 60 FPS.',
            'library_badge': 'PyQtGraph ImageItem',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:15px; box-sizing:border-box;">
                <div style="background:#070d09; border:1px solid #d4af37; border-radius:6px; height:180px; display:flex; flex-direction:column; justify-content:space-around; padding:10px;">
                  <div style="display:flex; justify-content:space-between; font-family:JetBrains Mono; font-size:0.75rem; color:#f3cf65;">
                    <span>20 kHz</span>
                    <span>10 kHz</span>
                    <span>1 kHz</span>
                    <span>0 Hz</span>
                  </div>
                  <!-- Spectrogram Frequency Wave Heatmap Bands -->
                  <div style="height:25px; background:linear-gradient(90deg, #070d09, #00e676, #00e676, #070d09, #ff1744, #ffab00);"></div>
                  <div style="height:25px; background:linear-gradient(90deg, #070d09, #070d09, #d4af37, #00e676, #070d09, #d4af37);"></div>
                  <div style="height:25px; background:linear-gradient(90deg, #00e676, #070d09, #070d09, #00e676, #00e676, #070d09);"></div>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Short-Time Fourier Transform: $\\text{STFT}\\{x(t)\\}(\\tau, \\omega) = \\int_{-\\infty}^\\infty x(t) w(t - \\tau) e^{-i\\omega t} dt$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Rotating machinery bearing failure acoustic detection, speech recognition AI frontends, radio RF monitoring.'},
                {'title': 'Technical Strengths', 'desc': 'ImageItem OpenGL hardware texture streaming with custom color lookup tables (LUT).'}
            ],
            'metrics': [
                {'label': 'Transform', 'val': 'Fast Fourier (FFT)', 'sub': 'Short-Time STFT'},
                {'label': 'Windowing', 'val': 'Hanning Window', 'sub': 'Zero Leakage'},
                {'label': 'Latency', 'val': '< 8 ms Real-Time', 'sub': 'Audio Live'},
                {'label': 'Display', 'val': 'QImage Texture', 'sub': 'Hardware LUT'}
            ],
            'code_snippet': """img = pg.ImageItem()
plot.addItem(img)
lut = pg.colormap.get('plasma').getLookupTable()
img.setLookupTable(lut)"""
        },

        # 13. Glumpy Ray-Marched 3D Quaternion Julia Fractal
        {
            'slide_id': 'slide-13-glumpy-fractal',
            'tag': '13 / Ray-Marching Shaders',
            'headline': '4D Quaternion Geometry:',
            'headline_span': 'Glumpy Ray-Marched Julia Fractal',
            'subtitle': 'Signed distance function (SDF) sphere-tracing rendering hypercomplex 4D quaternion fractals.',
            'library_badge': 'Glumpy Raymarcher',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 240" style="width:100%; max-height:260px;">
                  <!-- Fractal Organic Bulbs -->
                  <g fill="#d4af37" stroke="#fffefa" stroke-width="0.8">
                    <circle cx="160" cy="120" r="45" fill="rgba(212,175,55,0.7)"/>
                    <circle cx="115" cy="100" r="24" fill="rgba(0,230,118,0.7)"/>
                    <circle cx="205" cy="100" r="24" fill="rgba(0,230,118,0.7)"/>
                    <circle cx="160" cy="170" r="22" fill="rgba(0,229,255,0.7)"/>
                    <!-- Tertiary micro buds -->
                    <circle cx="95" cy="85" r="12" fill="#f3cf65"/>
                    <circle cx="225" cy="85" r="12" fill="#f3cf65"/>
                    <circle cx="138" cy="190" r="10" fill="#00e676"/>
                    <circle cx="182" cy="190" r="10" fill="#00e676"/>
                  </g>
                  <text x="160" y="230" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="10">Quaternion Iteration: Z = Z² + C</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Sphere-tracing raymarching of 4D quaternion polynomial iterative mapping: $q_{n+1} = q_n^2 + c$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Procedural asset generation, mathematical physics visualization, volumetric lighting shaders.'},
                {'title': 'Technical Strengths', 'desc': 'Renders mathematically infinite geometric detail using only a single quad and GLSL fragment shader.'}
            ],
            'metrics': [
                {'label': 'Algebra', 'val': '4D Quaternions', 'sub': 'Hypercomplex'},
                {'label': 'Rendering', 'val': 'Sphere Tracing', 'sub': 'Raymarch SDF'},
                {'label': 'Complexity', 'val': 'Infinite Detail', 'sub': 'Zero Polygons'},
                {'label': 'Hardware', 'val': 'Fragment Shader', 'sub': 'Single Quad'}
            ],
            'code_snippet': """float map(vec3 p) {
  vec4 z = vec4(p, 0.0);
  for (int i=0; i<10; i++) { z = quatSq(z) + c; }
  return 0.5 * log(r) * r / dr;
}"""
        },

        # 14. Mayavi Parametric Klein Bottle & Mobius Strip
        {
            'slide_id': 'slide-14-mayavi-klein',
            'tag': '14 / Differential Topology',
            'headline': 'Non-Orientable Manifolds:',
            'headline_span': 'Mayavi Parametric Klein Bottle',
            'subtitle': 'Immersion of non-orientable 4D topological surfaces in 3D Euclidean space with self-intersection tubes.',
            'library_badge': 'Mayavi Differential Geometry',
            'chart_html': """
              <div id="mayavi-klein-stage" class="plotly-graph" style="width:100%; height:100%;"></div>
              <script>
              (function(){
                window.addEventListener('load', function() {
                  const el = document.getElementById('mayavi-klein-stage');
                  if (!el || !window.Plotly) return;
                  const u = [], v = [], x = [], y = [], z = [];
                  const n = 24;
                  for(let i=0; i<n; i++) {
                    const ui = (i / n) * Math.PI;
                    for(let j=0; j<n; j++) {
                      const vi = (j / n) * 2 * Math.PI;
                      const r = 4 * (1 - Math.cos(ui) / 2);
                      let px, py, pz;
                      if (ui < Math.PI) {
                        px = 6 * Math.cos(ui) * (1 + Math.sin(ui)) + r * Math.cos(ui) * Math.cos(vi);
                        py = 16 * Math.sin(ui) + r * Math.sin(ui) * Math.cos(vi);
                      } else {
                        px = 6 * Math.cos(ui) * (1 + Math.sin(ui)) + r * Math.cos(vi + Math.PI);
                        py = 16 * Math.sin(ui);
                      }
                      pz = r * Math.sin(vi);
                      x.push(px); y.push(py); z.push(pz);
                    }
                  }
                  Plotly.newPlot('mayavi-klein-stage', [{
                    type: 'mesh3d', x: x, y: y, z: z,
                    color: '#d4af37', opacity: 0.75
                  }], {
                    paper_bgcolor: 'transparent',
                    margin: { l: 0, r: 0, b: 0, t: 0 },
                    scene: {
                      xaxis: { showgrid: false }, yaxis: { showgrid: false }, zaxis: { showgrid: false },
                      camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
                    }
                  }, { responsive: true, displayModeBar: false });
                });
              })();
              </script>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Parametric surface immersion equations $(x(u,v), y(u,v), z(u,v))$ for closed non-orientable surface with Euler characteristic $\\chi = 0$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Mathematical education, string theory compactification models, advanced industrial CAD geometry.'},
                {'title': 'Technical Strengths', 'desc': 'Computes exact surface normal vectors for smooth specular highlights across self-intersecting manifolds.'}
            ],
            'metrics': [
                {'label': 'Manifold', 'val': 'Non-Orientable', 'sub': 'One-Sided'},
                {'label': 'Euler Char', 'val': 'χ = 0', 'sub': 'Zero Genus'},
                {'label': 'Immersion', 'val': '4D to 3D Space', 'sub': 'Self-Crossing'},
                {'label': 'Mesh Engine', 'val': 'Mayavi / VTK', 'sub': 'C++ Precision'}
            ],
            'code_snippet': """u, v = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]
x = 6 * np.cos(u) * (1 + np.sin(u)) + r * np.cos(u) * np.cos(v)
mlab.mesh(x, y, z, colormap='Spectral')"""
        },

        # 15. VisPy Interactive Volumetric Maximum Intensity Projection (MIP)
        {
            'slide_id': 'slide-15-vispy-mip',
            'tag': '15 / Direct Volume Rendering',
            'headline': 'Direct Volume Ray-Casting:',
            'headline_span': 'VisPy Maximum Intensity Projection (MIP)',
            'subtitle': 'Evaluates maximum scalar value along viewing rays through 3D CT/MRI volumetric voxel grids.',
            'library_badge': 'VisPy VolumeVisual',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- MIP Ray Projections -->
                  <g stroke="rgba(255,255,255,0.15)" stroke-width="1" stroke-dasharray="3">
                    <line x1="40" y1="60" x2="310" y2="60"/>
                    <line x1="40" y1="120" x2="310" y2="120"/>
                    <line x1="40" y1="180" x2="310" y2="180"/>
                  </g>
                  <!-- High Intensity Skeleton Core -->
                  <rect x="140" y="80" width="70" height="80" fill="#fffefa" opacity="0.9" rx="8" filter="drop-shadow(0 0 10px #00e676)"/>
                  <text x="175" y="125" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="11" font-weight="bold">Bone Peak</text>
                  <!-- Ray Hit Label -->
                  <circle cx="310" cy="120" r="5" fill="#00e676"/>
                  <text x="310" y="140" text-anchor="middle" fill="#00e676" font-family="JetBrains Mono" font-size="9">MIP Hit: Max(I)</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Volume raycasting evaluating maximum intensity along ray path: $I_{\\text{MIP}}(u, v) = \\max_{t} \\{ f(\\mathbf{r}_0 + t\\mathbf{d}) \\}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Angiography blood vessel visualization, industrial non-destructive casting defect inspection.'},
                {'title': 'Technical Strengths', 'desc': 'Requires no complex transfer function opacity tuning; automatically highlights highest-density structures.'}
            ],
            'metrics': [
                {'label': 'Ray Operator', 'val': 'Max(I) Projection', 'sub': 'MIP Raycast'},
                {'label': 'Opacity Tuning', 'val': 'Zero Config', 'sub': 'Density Peak'},
                {'label': 'Hardware', 'val': '3D Texture Shaders', 'sub': 'Texture3D'},
                {'label': 'Use Case', 'val': 'Angiography CT', 'sub': 'Vessel Trees'}
            ],
            'code_snippet': """volume = scene.visuals.Volume(data, clim=(0, 255),
                             method='mip', parent=view.scene)"""
        },

        # 16. VTK Streamtube Flow Field around Aircraft Foil
        {
            'slide_id': 'slide-16-vtk-streamtube',
            'tag': '16 / CFD Streamtubes',
            'headline': 'Aerodynamic Streamtubes:',
            'headline_span': 'VTK Computational Aerodynamics',
            'subtitle': 'Constant-flux streamtubes expanding and contracting based on air pressure around supersonic wings.',
            'library_badge': 'VTK StreamTracer',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 380 240" style="width:100%; max-height:260px;">
                  <!-- Airfoil Shape (Black/Gold) -->
                  <path d="M 60 120 C 120 70, 220 90, 320 120 C 220 130, 120 140, 60 120 Z" fill="#13221b" stroke="#d4af37" stroke-width="2"/>
                  <!-- Streamtubes (Upper Accelerated - Cyan/Green) -->
                  <path d="M 40 80 C 100 50, 200 60, 340 100" fill="none" stroke="#00e5ff" stroke-width="4" opacity="0.85"/>
                  <path d="M 40 60 C 100 30, 200 40, 340 80" fill="none" stroke="#00e676" stroke-width="3" opacity="0.8"/>
                  <!-- Lower Streamtubes -->
                  <path d="M 40 160 C 120 150, 220 145, 340 140" fill="none" stroke="#f3cf65" stroke-width="3" opacity="0.8"/>
                  <text x="180" y="115" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Supersonic Foil</text>
                  <text x="180" y="45" text-anchor="middle" fill="#00e5ff" font-family="JetBrains Mono" font-size="9">Low Pressure / High V</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Bernoulli streamtube mass conservation: $\\rho_1 A_1 v_1 = \\rho_2 A_2 v_2$ with tube radius inversely proportional to velocity.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Formula 1 aerodynamic rear-wing downforce modeling, high-speed rail nose cone streamlining.'},
                {'title': 'Technical Strengths', 'desc': 'Conveys volumetric airflow tube cross-sections rather than thin 1D vector line approximations.'}
            ],
            'metrics': [
                {'label': 'Conservation', 'val': 'Mass Flux A1*V1', 'sub': 'Continuity'},
                {'label': 'Tube Radius', 'val': 'r ~ 1/v', 'sub': 'Dynamic Radius'},
                {'label': 'Integration', 'val': 'Runge-Kutta 4/5', 'sub': 'Adaptive Step'},
                {'label': 'Engine', 'val': 'VTK TubeFilter', 'sub': '3D Polygonal'}
            ],
            'code_snippet': """tracer = vtk.vtkStreamTracer()
tube = vtk.vtkTubeFilter()
tube.SetInputConnection(tracer.GetOutputPort())
tube.SetRadius(0.05)"""
        },

        # 17. Datashader Hexagonal 2D Binning with Logarithmic Scaling
        {
            'slide_id': 'slide-17-datashader-hexbin',
            'tag': '17 / High-Density Hexagons',
            'headline': 'Logarithmic Tessellation:',
            'headline_span': 'Datashader Hexbin Aggregation',
            'subtitle': 'Sub-pixel hexagonal quantization with gamma log scaling preventing bright-core washout.',
            'library_badge': 'Datashader Hexbin',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 320 240" style="width:100%; max-height:260px;">
                  <!-- Hexagonal Array -->
                  <g fill="#00e676" stroke="#070c09" stroke-width="1">
                    <polygon points="160,80 180,90 180,110 160,120 140,110 140,90" fill="#fffefa"/>
                    <polygon points="180,110 200,120 200,140 180,150 160,140 160,120" fill="#00e676"/>
                    <polygon points="140,110 160,120 160,140 140,150 120,140 120,120" fill="#00e676"/>
                    <polygon points="160,50 180,60 180,80 160,90 140,80 140,60" fill="#d4af37"/>
                    <polygon points="200,80 220,90 220,110 200,120 180,110 180,90" fill="#1b2822"/>
                    <polygon points="120,80 140,90 140,110 120,120 100,110 100,90" fill="#1b2822"/>
                  </g>
                  <text x="160" y="105" text-anchor="middle" fill="#070c09" font-family="JetBrains Mono" font-size="9" font-weight="bold">100k</text>
                  <text x="160" y="210" text-anchor="middle" fill="#f3cf65" font-family="DM Sans" font-size="10">Logarithmic Gamma Equalized Counts</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Hexagonal spatial binning with non-linear power transform: $C\' = C^\\gamma$ where $\\gamma \\in (0, 1]$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Millions of customer loyalty transactions, retail foot traffic density, credit card swipe matrices.'},
                {'title': 'Technical Strengths', 'desc': 'Hexagons possess 6 equidistant neighbors, eliminating rectangular diagonal orientation bias.'}
            ],
            'metrics': [
                {'label': 'Geometry', 'val': 'Regular Hexagon', 'sub': '6 Equidistant'},
                {'label': 'Gamma Scale', 'val': 'γ = 0.4', 'sub': 'Reveals Shadows'},
                {'label': 'Bias Free', 'val': 'Zero Diagonal Bias', 'sub': 'Optimal Shape'},
                {'label': 'Throughput', 'val': '10M Points', 'sub': 'Numba Fast'}
            ],
            'code_snippet': """agg = cvs.points(df, 'x', 'y', agg=ds.count())
img = tf.shade(agg, cmap=greens, how='log')"""
        },

        # 18. PyQtGraph Multi-ROI Real-Time Image Histogram
        {
            'slide_id': 'slide-18-pyqtgraph-roi',
            'tag': '18 / Interactive Machine Vision',
            'headline': 'Real-Time ROI Analysis:',
            'headline_span': 'PyQtGraph Region-of-Interest Slicing',
            'subtitle': 'Interactive draggable bounding box calculating sub-region pixel intensity histograms at 60 FPS.',
            'library_badge': 'PyQtGraph ROI',
            'chart_html': """
              <div style="width:100%; height:100%; display:grid; grid-template-columns:1.2fr 1fr; gap:12px; padding:15px; box-sizing:border-box;">
                <!-- Main Image with ROI -->
                <div style="background:#070d09; border:1px solid rgba(255,255,255,0.15); border-radius:6px; position:relative; overflow:hidden;">
                  <div style="position:absolute; left:30px; top:40px; width:90px; height:70px; border:2px solid #00e676; background:rgba(0,230,118,0.15);">
                    <span style="font-family:JetBrains Mono; font-size:0.75rem; color:#00e676; padding:2px;">ROI #1</span>
                  </div>
                </div>
                <!-- Live Histogram of ROI -->
                <div style="background:#070d09; border:1px solid #d4af37; border-radius:6px; padding:10px; display:flex; flex-direction:column; justify-content:space-between;">
                  <span style="font-family:JetBrains Mono; font-size:0.8rem; color:#f3cf65;">Live ROI Pixel Histogram</span>
                  <svg viewBox="0 0 160 80" style="width:100%; height:70px;">
                    <path d="M 10 70 Q 40 20, 80 50 T 150 70 Z" fill="#00e676" opacity="0.6"/>
                  </svg>
                  <span style="font-size:0.75rem; color:#9ba9a1;">Mean: 142.4 &bull; Std: 18.2</span>
                </div>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'NumPy sub-array memory slicing: $\\text{Hist}(I[y_1:y_2, x_1:x_2])$ executed upon Qt mouse-drag events.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Automated optical inspection (AOI) chip fabrication defects, live fluorescence microscopy.'},
                {'title': 'Technical Strengths', 'desc': 'Direct C++ NumPy buffer binding recalculates histograms without perceptible mouse drag latency.'}
            ],
            'metrics': [
                {'label': 'Interaction', 'val': 'Draggable Box', 'sub': 'Live Resizing'},
                {'label': 'Calculation', 'val': 'Instant NumPy', 'sub': 'Sub-Millisecond'},
                {'label': 'GUI Framework', 'val': 'Qt6 / C++', 'sub': 'Native Speed'},
                {'label': 'Histogram', 'val': '256 Bins', 'sub': 'Dynamic Range'}
            ],
            'code_snippet': """roi = pg.RectROI([20, 20], [80, 60], pen='#00e676')
win.addItem(roi)
def update(): hist.plot(roi.getArrayRegion(img, imgItem))
roi.sigRegionChanged.connect(update)"""
        },

        # 19. VisPy Real-Time Seismic Wave Propagation Mesh
        {
            'slide_id': 'slide-19-vispy-seismic',
            'tag': '19 / Wave Propagation',
            'headline': 'Dynamic Mesh Deformation:',
            'headline_span': 'VisPy 3D Seismic Wave Propagation',
            'subtitle': 'Finite difference time domain (FDTD) acoustic wave equations animating real-time crustal displacement.',
            'library_badge': 'VisPy Mesh Deform',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Deformed wireframe grid -->
                  <path d="M 40 160 Q 140 60, 180 150 T 320 160" fill="none" stroke="#00e676" stroke-width="2.5"/>
                  <path d="M 40 180 Q 140 80, 180 170 T 320 180" fill="none" stroke="#d4af37" stroke-width="2"/>
                  <!-- Epicenter Marker -->
                  <circle cx="140" cy="90" r="8" fill="#ff1744" filter="drop-shadow(0 0 8px #ff1744)"/>
                  <text x="140" y="75" text-anchor="middle" fill="#ff1744" font-family="JetBrains Mono" font-size="10" font-weight="bold">Epicenter</text>
                  <text x="175" y="220" text-anchor="middle" fill="#fffefa" font-family="DM Sans" font-size="10">2D Acoustic Wave Equation: ∂²u/∂t² = c² ∇²u</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': '2D acoustic wave equation FDTD integration: $u_{i,j}^{n+1} = 2u_{i,j}^n - u_{i,j}^{n-1} + \\left(\\frac{c\\Delta t}{\\Delta x}\\right)^2 \\nabla^2 u$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Earthquake hazard mitigation modeling, ultrasonic non-destructive weld testing, architectural acoustics.'},
                {'title': 'Technical Strengths', 'desc': 'Direct GLSL vertex displacement avoids mutating CPU RAM arrays on every frame.'}
            ],
            'metrics': [
                {'label': 'Physics PDE', 'val': 'Wave Equation', 'sub': 'Acoustic FDTD'},
                {'label': 'Deformation', 'val': 'Vertex Shader', 'sub': 'GPU Displace'},
                {'label': 'Courant Cond.', 'val': 'CFL Stable', 'sub': 'c*Δt/Δx < 1/√2'},
                {'label': 'Frame Rate', 'val': '60 FPS Continuous', 'sub': 'VisPy Canvas'}
            ],
            'code_snippet': """# Vertex shader updates Z coordinate directly
gl_Position = u_model * vec4(position.xy, wave_height, 1.0);"""
        },

        # 20. VTK Tensor Ellipsoids (Diffusion Tensor Imaging)
        {
            'slide_id': 'slide-20-vtk-tensor',
            'tag': '20 / Tensor Fields',
            'headline': 'Anisotropic Tensor Fields:',
            'headline_span': 'VTK Diffusion Tensor Ellipsoids',
            'subtitle': '3D oriented ellipsoids parameterized by eigenvalue decomposition of symmetric second-order stress/diffusion tensors.',
            'library_badge': 'VTK TensorGlyph',
            'chart_html': """
              <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                <svg viewBox="0 0 350 240" style="width:100%; max-height:260px;">
                  <!-- Array of oriented ellipsoids -->
                  <g transform="translate(60, 60)">
                    <ellipse cx="0" cy="0" rx="28" ry="12" fill="#00e676" opacity="0.8" transform="rotate(25)"/>
                  </g>
                  <g transform="translate(140, 60)">
                    <ellipse cx="0" cy="0" rx="32" ry="10" fill="#00e676" opacity="0.85" transform="rotate(35)"/>
                  </g>
                  <g transform="translate(220, 60)">
                    <ellipse cx="0" cy="0" rx="36" ry="8" fill="#d4af37" opacity="0.85" transform="rotate(45)"/>
                  </g>
                  <g transform="translate(100, 140)">
                    <ellipse cx="0" cy="0" rx="20" ry="18" fill="#00e5ff" opacity="0.75" transform="rotate(0)"/>
                  </g>
                  <g transform="translate(180, 140)">
                    <ellipse cx="0" cy="0" rx="34" ry="9" fill="#d4af37" opacity="0.85" transform="rotate(55)"/>
                  </g>
                  <g transform="translate(260, 140)">
                    <ellipse cx="0" cy="0" rx="38" ry="7" fill="#ff1744" opacity="0.9" transform="rotate(65)"/>
                  </g>
                  <text x="175" y="225" text-anchor="middle" fill="#fffefa" font-family="JetBrains Mono" font-size="10">Eigenvalues λ₁ ≥ λ₂ ≥ λ₃ &bull; Anisotropic Alignment</text>
                </svg>
              </div>
            """,
            'specs': [
                {'title': 'Mathematical Engine', 'desc': 'Eigenvalue decomposition of symmetric $3\\times 3$ tensor: $\\mathbf{D} = \\mathbf{V} \\mathbf{\\Lambda} \\mathbf{V}^T$, where radii $r_i = \\sqrt{\\lambda_i}$.'},
                {'title': 'Enterprise Use Cases', 'desc': 'Brain white-matter tractography (DTI), crystal anisotropy stress, geological tectonic stress fields.'},
                {'title': 'Technical Strengths', 'desc': 'VTK TensorGlyph automatically computes principal eigenvector axes and scales ellipsoid radii in C++.'}
            ],
            'metrics': [
                {'label': 'Tensor Order', 'val': '2nd Order 3x3', 'sub': 'Symmetric DTI'},
                {'label': 'Eigendecomp', 'val': 'λ1, λ2, λ3', 'sub': 'Principal Axes'},
                {'label': 'Anisotropy', 'val': 'Fractional (FA)', 'sub': 'Water Diffusion'},
                {'label': 'Framework', 'val': 'Kitware VTK', 'sub': 'TensorGlyph'}
            ],
            'code_snippet': """tensorGlyphs = vtk.vtkTensorGlyph()
tensorGlyphs.SetInputData(tensorVolume)
tensorGlyphs.SetSourceConnection(sphere.GetOutputPort())
tensorGlyphs.ColorGlyphsWithFractionalAnisotropy()"""
        }
    ]

    html = generate_deck_html(deck_meta, slides)
    out_path = os.path.join(SCRIPT_DIR, "06-python-scientific-3d.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Built {out_path} (20 slides, {len(html)} bytes)")

if __name__ == "__main__":
    build_deck()
