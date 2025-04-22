

# INTERNAL TEST ONLY - will be ready soon 


# Modelica MCP Server

A Model Context Protocol server that provides modelica model simulation capabilities. This server enables LLMs to retrieve and process modelica related tasks.

What is MCP, refer to https://modelcontextprotocol.io/


### Available Tools

- `modelica_simulate` - run modelica model simulation by source code.
    - `modelica_code` (string, required): the source code of modelica model
    - `stop_time` (float, optional, default=1.0): stop time of simulation


### Prompts - not supported yet

- **Simulation Prompt**
  - Simulation result
  - Arguments:
    - `modelica code` (string, required): ...

## Installation

### Pre-requests
- python installed
- wget tool installed (or you can download installation script manully )


### Step 1:   Get  ```"ORTHOGONAL_TOKEN"```
- **You need to register in paas.orthogonal.cc**
1. Logging to orthogonal:  open browser, log into https://paas.orthogonal.cc
2. Retrieve token:  after sucessful login, type F12 enter into dev mode, then click 'Network', finally type F5 to refresh, the network communications will be shown here, find 'status/' record and show its headers, the token is something like ```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1OTA4NTk0LCJpYXQiOjE3NDUzMDM3OTQsImp0aSI6IjAxOWI3YWIxODg0YjRiZDE4MzE4ZmI4ZjVlNTI1OTI1IiwidXNlcl9pZCI6OH0.JwN3wjohjMUJZhWVB0rsePujn85Hq0ltg0d4HuXkc2Y```      (Without starting 'Bearer ' ) 
3. Record this token, it will be used to fill in mcp configuration
<center><img src="temp_auth_token.png" width="50%" height="50%" ></center>
4. (Optional for cursor config) Enter into your cursor project root folder ( will automatically create mcp.json) <br>

### Step 2:  run installation script
replace below "ORTHOGONAL_TOKEN" with your token
<p><b>
wget http://paas.orthogonal.cc/mydownload/install_orthogonal_mcp_server.py -O install_orthogonal_mcp_server.py ; python install_orthogonal_mcp_server.py  ORTHOGONAL_TOKEN
</b>
<p>
example:<br>
wget http://paas.orthogonal.cc/mydownload/install_orthogonal_mcp_server.py -O install_orthogonal_mcp_server.py ; python install_orthogonal_mcp_server.py   "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1OTA4NTk0LCJpYXQiOjE3NDUzMDM3OTQsImp0aSI6IjAxOWI3YWIxODg0YjRiZDE4MzE4ZmI4ZjVlNTI1OTI1IiwidXNlcl9pZCI6OH0.JwN3wjohjMUJZhWVB0rsePujn85Hq0ltg0d4HuXkc2Y"<br>

<br>
if the message "=== INSTALLATION SUCCESS ===" is printed, then you are all set

<p>

<!-- 
### FOR reference ONLY：   Cursor Installation:  using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *modelica_simulate*.

uv installation <br>
```curl -LsSf https://astral.sh/uv/install.sh | sh```

1. clone mcp server<br>
```git clone https://github.com/Orthogonalpub/modelica_simulation_mcp_server ```

2. enter into the directory<br>
```cd modelica_simulation_mcp_server```

3. create virtual env<br>
```uv venv```

4. activate virtual env<br>

<p><b>Windows:</b> <br>
```.venv\Scripts\activate```<br>

<p><b>Mac / Linux:</b> <br>
```source .venv/bin/activate```<br>

5. add dependencies<br>
```uv add "mcp[cli]" httpx websocket-client pandas pydantic  --active```

-->

## MCP client configuration example:

### Configure for cursor/Claude.app   ( installation will config automatically for cursor )

Add to your cursor/Claude settings:  mcp.json ( located in your user home directly or .cursor/ directory )
in cursor you can open this file by clicking "Settings" -> "MCP" -> "Add new global MCP server"

<details>
<summary>Using uvx</summary>

Example:  
1. set "ORTHOGONAL_TOKEN" correctly
2. set path of "args" and "command" correctly by your local installation

<p><b>Windows</b>
<br> mcp.json example <br>

Make sure to change below settings according to your installation: 
``` /opt/homebrew/bin/uv ```
``` /Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/ ```
``` /Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/main.py ```

```json
{
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
}
```


<p><b>Mac / Linux</b>
<br> mcp.json example <br>

Make sure to change below settings according to your installation: 
``` command:  /opt/homebrew/bin/uv ```
``` args:     /Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/ ```
``` args:     /Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/main.py ```

```json
{
        "mcpServers": {
                "modelica-mcp-server": {
                        "connectionType": "stdio",
                        "command": "/opt/homebrew/bin/uv",
                        "args": [
            			    "--directory",
           			     "/Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/",
           			     "run",
                                     "/Users/rainnie/Downloads/halo/modelica_simulation_mcp_server/main.py"
                        ],
                        "env": {
                                "ORTHOGONAL_TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0OTY2OTQxLCJpYXQiOjE3NDQzNjIxNDEsImp0aSI6ImE5M2RlNDUyMGU1ZDQ3M2RiZjVjOTFhMDgxZDEyYThjIiwidXNlcl9pZCI6NDR9.k0RM8as9PtFX1cvCowOQeZraDPM-Qks4dl9uFauHUH8",
                                "DEBUG": "true",
                                "LOG_LEVEL": "verbose",
                                "PORT": "9223"
                        },
                        "disabled": false,
                        "autoApprove": []
                }
        }
}

```


</details>

after successful installation, the mcp server will be shown and the status icon is GREEN
<center><img src="./mcp_server_running.png" width="50%" height="50%" ></center>


### Debug 

using mcp inspector
```mcp dev main.py```
it needs to add environment variable in mcp inspector window

## License

modelica-simulation is licensed under the GPL License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
