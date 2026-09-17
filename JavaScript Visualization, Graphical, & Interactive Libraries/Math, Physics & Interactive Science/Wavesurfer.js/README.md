# Wavesurfer.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Interactive audio waveform visualizer built on the Web Audio API and HTML5 Canvas.

## Official Resources
- **Website / Documentation:** [https://wavesurfer.xyz](https://wavesurfer.xyz)

## Installation & Setup
```bash
npm install wavesurfer.js
```

### CDN Embed:
```html
<script src="https://unpkg.com/wavesurfer.js@7"></script>
```

## Starter / Hello World Example
```javascript
import WaveSurfer from 'wavesurfer.js';
const wavesurfer = WaveSurfer.create({
  container: '#waveform',
  waveColor: '#4F4A85',
  progressColor: '#383351',
  url: '/audio/track.mp3'
});
```
