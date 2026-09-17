# Anvil
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Full-stack web applications with nothing but Python, drag-and-drop designer, and client-server RPC.

## Official Resources
- **Website / Documentation:** [https://anvil.works](https://anvil.works)

## Installation & Setup
```bash
pip install anvil-uplink
```

## Starter / Hello World Example
```python
import anvil.server
anvil.server.connect("YOUR_UPLINK_KEY")
@anvil.server.callable
def process_data(value):
    return f"Computed: {value * 2}"
anvil.server.wait_forever()
```
