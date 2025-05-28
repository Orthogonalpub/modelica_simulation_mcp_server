
# Modelica MCP Server

**A lightweight Model Context Protocol server for simulating Modelica models**  
_Enabling LLMs to process Modelica-related tasks seamlessly_

![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-6366f1?style=for-the-badge) ![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge) ![Active Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)

---

## What is this?

![Overview](2.png)

The Modelica MCP server transforms **ODE—a new Modelica IDE** into an engineering **AI agent**, seamlessly bridging Large Language Models with advanced simulation capabilities. It enables AI to autonomously generate, visualize, and simulate complex engineering models through natural language interactions.

**Key Capabilities:**

- **🤖 AI-Driven Model Generation**: Automatically create complete Modelica models from natural language descriptions
- **🎨 Intelligent Diagram Creation**: Generate interactive visual diagrams with proper component placement and connections in Modelica IDE
- **🔄 Autonomous Simulation**: End-to-end simulation workflow from concept to results
  


## Key Features

| Feature                        | Description                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **🤖 AI Model Generation**     | **Automatically create** complete Modelica models from natural language descriptions                                                 |
| **🎨 Intelligent Diagramming** | **Generate visual diagrams** with smart component placement, automatic routing, and professional annotations through ODE integration |
| **🏗️ Full IDE Access**        | **Complete Modelica development environment** via ODE with syntax highlighting, error checking, and debugging                        |
| **📊 Advanced Visualization**  | **Real-time plotting**, 3D visualization, interactive charts, and customizable result analysis dashboards                            |
| **⚡ Seamless Integration**     | **One-click setup** with popular AI clients like Cursor, and custom LLM applications                                                 |
| **🛡️ Enterprise Security**    | **Token-based authentication** with secure cloud execution and data protection                                                       |
| **🔄 Autonomous Workflows**    | **End-to-end automation** from natural language input to simulation results and engineering insights                                 |

---

## Available Tools

###### `modelica_simulate()`

**Purpose**: Execute complete Modelica simulation workflows with AI  
**Features**:
- Automatic model validation and error correction
- Multi-scenario simulation batching
- Real-time progress monitoring 
###### `modelica_get_diagram_url()`

**Purpose**: Generate interactive model diagrams through ODE integration  
**Features**:
- AI-optimized component placement and layout
- Automatic connection routing and labeling
- Professional engineering diagram standards

---

## Installation Guide by example using Cursor

1. **Create User Account** → Visit [www.orthogonal.dev](https://www.orthogonal.dev/)
2. **Login** to your account
3. **Get token**
4. **MCP Client Configuration**

![Installation Screenshot](1.png)

---
## Show case

This demonstration showcases creating a bouncing ball model with realistic physics including gravitational acceleration, ground collision detection, and coefficient of restitution using just a text prompt in Cursor. The Modelica MCP Server automatically generates the differential equations, runs the simulation, and extracts position and velocity data over time. The simulation results are then fed into a custom Three.js visualization that renders an animated 3D scene with the bouncing ball, ground plane, and real-time trajectory tracking.



[![Watch the Demo](https://img.youtube.com/vi/j9FHccdkPPU/maxresdefault.jpg)](https://youtu.be/j9FHccdkPPU)

**🎥 [Watch Full Demo on YouTube](https://youtu.be/j9FHccdkPPU)**

---
## Resources & Links

|Resource|Description|
|---|---|
|**[Model Context Protocol](https://modelcontextprotocol.io/)**|Official MCP documentation and specifications|
|**[Orthogonal Platform](https://www.orthogonal.dev/)**|Advanced Modelica simulation platform|
|**[Modelica Language](https://modelica.org/)**|Official Modelica language resources|

---
## Author Information

**orthogonal supersystems GmbH**  
[www.orthogonal.dev](https://www.orthogonal.dev/)
