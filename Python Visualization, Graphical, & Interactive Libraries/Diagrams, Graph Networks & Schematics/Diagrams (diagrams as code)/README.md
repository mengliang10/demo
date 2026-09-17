# Diagrams (diagrams as code)
**Category:** [Diagrams, Graph Networks & Schematics](../)
**Ecosystem:** [Python Visualization, Graphical, & Interactive Libraries](../../)

## Overview
Diagram as Code: prototype and document cloud system architectures in pure Python scripts.

## Official Resources
- **Website / Documentation:** [https://diagrams.mingrammer.com](https://diagrams.mingrammer.com)

## Installation & Setup
```bash
pip install diagrams
```

## Starter / Hello World Example
```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service Architecture", show=False, filename="aws_arch"):
    ELB("lb") >> EC2("web") >> RDS("userdb")
```
