# Reflex
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Open-source full-stack framework for building web applications in pure Python (formerly Pynecone).

## Official Resources
- **Website / Documentation:** [https://reflex.dev](https://reflex.dev)

## Installation & Setup
```bash
pip install reflex
```

## Starter / Hello World Example
```python
import reflex as rx

class State(rx.State):
    count: int = 0
    def increment(self):
        self.count += 1

def index():
    return rx.vstack(
        rx.heading(State.count),
        rx.button("Increment", on_click=State.increment)
    )

app = rx.App()
app.add_page(index)
```
