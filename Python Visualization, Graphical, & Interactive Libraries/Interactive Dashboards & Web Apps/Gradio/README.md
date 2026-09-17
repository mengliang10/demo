# Gradio
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Build and share machine learning demos, LLM user interfaces, and interactive web tools effortlessly.

## Official Resources
- **Website / Documentation:** [https://www.gradio.app](https://www.gradio.app)

## Installation & Setup
```bash
pip install gradio
```

## Starter / Hello World Example
```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo.launch()
```
