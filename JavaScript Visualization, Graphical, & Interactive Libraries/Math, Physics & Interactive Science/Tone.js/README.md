# Tone.js
**Category:** [Math, Physics & Interactive Science](../)
**Ecosystem:** [JavaScript Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Web Audio framework for creating interactive music, synthesizers, and audio DSP in the browser.

## Official Resources
- **Website / Documentation:** [https://tonejs.github.io](https://tonejs.github.io)

## Installation & Setup
```bash
npm install tone
```

### CDN Embed:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

## Starter / Hello World Example
```javascript
const synth = new Tone.Synth().toDestination();
document.getElementById('play-btn').addEventListener('click', () => {
  Tone.start();
  synth.triggerAttackRelease("C4", "8n");
});
```
