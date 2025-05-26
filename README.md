# Modelica MCP Server

> A lightweight Model Context Protocol (MCP) server for simulating Modelica models, enabling LLMs to process Modelica-related tasks seamlessly.

[![MCP](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://claude.ai/chat/d5fffc82-c149-404b-b337-43ee9187d4f2#) [![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://claude.ai/chat/d5fffc82-c149-404b-b337-43ee9187d4f2#)

## 🚀 What is this?

This MCP server bridges the gap between Large Language Models and Modelica simulation capabilities. It allows AI assistants to execute Modelica code, run simulations, and analyze results directly within conversations.

**Learn more about MCP**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)

## ✨ Features

- **🔧 Direct Modelica Simulation** - Execute Modelica models with customizable parameters
- **📊 Visual Diagrams** - Generate and retrieve model diagrams
- **⚡ Fast Integration** - Quick setup with popular AI clients
- **🛡️ Secure** - Token-based authentication

## 🛠️ Available Tools

### `modelica_simulate`

Executes Modelica model simulations with configurable parameters.

**Parameters:**

- `modelica_code` _(string, required)_ - Complete Modelica model source code
- `stop_time` _(float, optional)_ - Simulation duration (default: 1.0 seconds)

**Returns:** Simulation results including status, error messages, and data values

### `modelica_get_diagram_url`

Generates visual diagrams for Modelica models.

**Parameters:**

- `model_name` _(string, required)_ - Name of the Modelica model
- `diagram_type` _(string, optional)_ - Type of diagram to generate

**Returns:** URL to the generated diagram

## 📦 Installation

### Step 1: Get Your Authentication Token

1. **Register** at [paas.orthogonal.cc](https://paas.orthogonal.cc/)
    
2. **Login** to your account
    
3. **Extract token**:
    
    - Open browser developer tools (`F12`)
    - Navigate to **Network** tab

4. **Save** the token for configuration
    

### Step 2: Configure MCP Client

#### For Cursor/Claude Desktop

Add to your MCP settings:

```json
{
  "mcpServers": {
    "modelica": {
      "command": "npx",
      "args": ["modelica-mcp-server"],
      "env": {
        "ORTHOGONAL_TOKEN": "your_token_here"
      }
    }
  }
}
```

#### For Other Clients

Configuration varies by client. Check your client's MCP documentation for specific setup instructions.

## 📋 Quick Start

Once configured, you can interact with Modelica models through your AI assistant:

```
"Simulate this Modelica model and show me the results:

model SimpleCircuit
  // Your Modelica code here
end SimpleCircuit;"
```

## 🎥 Demo

> **Installation Video Tutorial**: [Watch the setup process](https://claude.ai/chat/link-to-demo-video)

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🔗 Links

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Orthogonal Platform](https://paas.orthogonal.cc/)
- [Documentation](https://claude.ai/chat/d5fffc82-c149-404b-b337-43ee9187d4f2#) | [Issues](https://claude.ai/chat/d5fffc82-c149-404b-b337-43ee9187d4f2#) | [Discussions](https://claude.ai/chat/d5fffc82-c149-404b-b337-43ee9187d4f2#)

---

<div align="center"> <sub>Built with ❤️ for the Modelica community</sub> </div>
