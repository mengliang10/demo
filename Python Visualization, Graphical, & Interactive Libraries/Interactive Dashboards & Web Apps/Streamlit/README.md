# Streamlit
**Category:** [Interactive Dashboards & Web Apps](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Turn Python data scripts into shareable, reactive web applications in minutes with zero frontend code.

## Official Resources
- **Website / Documentation:** [https://streamlit.io](https://streamlit.io)

## Installation & Setup
```bash
pip install streamlit
```

## Starter / Hello World Example
```python
import streamlit as st
import numpy as np

st.title("Streamlit Dashboard")
x = st.slider("Select value", 0, 100, 25)
st.write(f"The square of {x} is {x**2}")
st.line_chart(np.random.randn(20, 3))
```
