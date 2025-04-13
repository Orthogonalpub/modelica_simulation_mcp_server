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

Example
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



### Customization - robots.txt

By default, the server will obey a websites robots.txt file if the request came from the model (via a tool), but not if
the request was user initiated (via a prompt). This can be disabled by adding the argument `--ignore-robots-txt` to the
`args` list in the configuration.


### Customization - simulation parameters

The server can be configured to use different simulation parameters `--start-time`.


## License

modelica-simulation is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
