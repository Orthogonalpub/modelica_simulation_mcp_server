

# INTERNAL TEST ONLY - will be ready soon 


# Modelica MCP Server

A Model Context Protocol server that provides modelica model simulation capabilities. This server enables LLMs to retrieve and process modelica related tasks.


### Available Tools

- `modelica_simulate` - run modelica model simulation by source code.
    - `modelica_code` (string, required): the source code of modelica model


### Prompts

- **Simulation Prompt**
  - Simulation result
  - Arguments:
    - `modelica code` (string, required): ...

## Installation

### Get Orthogonal Server token
- **You need to register in paas.orthogonal.cc**
- **1, open browser, log into https://paas.orthogonal.cc**
- **2, type F12 enter into dev mode, then click 'Network', finally type F5 to refresh, the network communications will be shown here, find 'status/' record and show its headers, the token is something like ```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MjI3NjAzLCJpYXQiOjE3NDQ2MjI4MDMsImp0aSI6IjY4MmFmOTA0MjA5ZDRmYWZiNTI1MmIyYTg1MjMxZDQ3IiwidXNlcl9pZCI6OH0.NKbo6NNtSzyzNebXSlmbRLYkf_5ffdWALT7OxXDr6b8```  **     (Without starting 'Bearer ' ) 
- **3, record this token, it will be used to fill in mcp configuration**


### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *modelica_simulate*.

1. clone mcp server
```git clone https://github.com/Orthogonalpub/modelica_simulation_mcp_server ```

2. enter into the directory
```cd modelica_simulation_mcp_server```

3. create virtual env
```uv venv```

4. activate virtual env
```.venv\Scripts\activate```

5. add dependencies
```uv add mcp[cli] httpx websocket-client pandas --active```





## Configuration

### Configure for cursor/Claude.app

Add to your cursor/Claude settings:

<details>
<summary>Using uvx</summary>

Example:  
set  "command/args/ORTHOGONAL_TOKEN" correctly by your local installation
```json
  "mcpServers": {
      "modelica-mcp-server": {
          "connectionType": "stdio", 
          "command": "C:\\arbeit\\99.fmi\\modelica_simulation_mcp_server\\.venv\\Scripts\\python.exe",
          "args": [
              "C:\\arbeit\\99.fmi\\modelica_simulation_mcp_server\\main.py"
            ],
            "env": {
              "ORTHOGONAL_TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0NzE3MDk1LCJpYXQiOjE3NDQxMTIyOTUsImp0aSI6IjMyYTczOTljMDJjZDQxZDBiNWYwNzVmZDBiNjk3YmI4IiwidXNlcl9pZCI6OH0.49PfrGwxpP0yehrb6_bd0TZh4v_uo2pj5jvy10xH18U",
              "DEBUG": "true",
              "LOG_LEVEL": "verbose",
              "PORT": "9223"
              },
            "disabled": false,
            "autoApprove": []
      }
  }
```
</details>


### Customization - simulation parameters

The server can be configured to use different simulation parameters `--start-time`, to be added



## License

modelica-simulation is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
