# -*- coding: utf-8 -*-

import os
import sys
import platform
import subprocess
import shutil
import json

g_os_name = "None"
g_root_folder = ""
g_uv_path = ""
g_target_git_url = "https://github.com/Orthogonalpub/modelica_simulation_mcp_server"

g_mcp_server_unique_name = "modelica-mcp-server"

g_default_mcp_json_string_windows ='''
{
  "mcpServers": {
          "modelica-mcp-server": {
              "connectionType": "stdio", 
              "command": "__PLACEHOLDER_PYTHON_CMD__",
              "args": [
                  "__PLACEHOLDER_PYTHON_MAIN__"
                ],
                "env": {
                  "ORTHOGONAL_TOKEN": "__PLACEHOLDER_ORTHOGONAL_TOKEN__",
                  "DEBUG": "true",
                  "LOG_LEVEL": "verbose",
                  "PORT": "9223"
                  },
                "disabled": false,
                "autoApprove": []
          }
  }
}
'''

g_default_mcp_json_string_mac_linux ='''
{
        "mcpServers": {
                "modelica-mcp-server": {
                        "connectionType": "stdio",
                        "command": "__PLACEHOLDER_UV_PATH__",
                        "args": [
            			    "--directory",
           			     "__PLACEHOLDER_RUNNING_FOLDER__",
           			     "run",
                                     "__PLACEHOLDER_PYTHON_MAIN__"
                        ],
                        "env": {
                                "ORTHOGONAL_TOKEN": "__PLACEHOLDER_ORTHOGONAL_TOKEN__",
                                "DEBUG": "true",
                                "LOG_LEVEL": "verbose",
                                "PORT": "9223"
                        },
                        "disabled": false,
                        "autoApprove": []
                }
        }
}
'''





def run_command(command: list) -> str:
    global g_os_name

    if g_os_name == "Windows":
        # command = ["cmd", "/c", "dir /b"]  # Execute 'dir /b' using cmd.exe
        pass
    elif g_os_name == "Darwin":
        # command = ["ls", "-l"]
        pass
    elif g_os_name == "Linux":
        # command = ["ls", "-l"]
        pass
    else:
        print("Not supported os system", g_os_name )
        sys.exit(1)

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # print("output command:")
        # print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

    return result.stdout, result.stderr


def main():
    """Main func"""

    global g_os_name
    global g_root_folder
    global g_uv_path
    global g_target_git_url
    global g_default_mcp_json_string_windows
    global g_default_mcp_json_string_mac_linux

    failed_flag_file = "failed.txt"
    if os.path.isfile( failed_flag_file ):
        os.remove(failed_flag_file)

    if sys.version_info < (3, 10):
        print("Exit -1, python Version must >= 3.10") 
        exit( -1 )

    print("######## STEP 1:  ensure orthogonal token is given ... " )
    if len(sys.argv) != 2:
        print("Exit -1, ORTHOGONAL TOKEN must be set") 
        print(f"Example: {sys.argv[0]}  orthogonal_token ") 
        exit( -1 ) 

    g_os_name = platform.system()
    g_root_folder = os.path.dirname(os.path.abspath(__file__))

    print("######## STEP 2:  check and install uv ... " )
    g_uv_path = shutil.which("uv")
    if g_uv_path:
        pass
    else:  
        if g_os_name == "Windows":
            command = ["pip", "install", "uv"] 
        elif g_os_name == "Darwin":
            command = ["pip", "install", "uv"] 
        elif g_os_name == "Linux":
            command = ["pip", "install", "uv"] 
        else:
            print("Not supported os system", g_os_name )
            sys.exit(1)

        result_data, result_err_msg = run_command( command )

        g_uv_path = shutil.which("uv")
        if g_uv_path:
            pass
        else:            
            print("Failed to install uv")
            sys.exit(1)


    print("######## STEP 3:  download from github ... " )
    local_path = g_target_git_url[g_target_git_url.rfind("/")+1:]
    if os.path.exists( local_path ):
        print(f"Exit -1, target path exists [{local_path}], please remove it" )
        sys.exit(1) 
    _, _ = run_command( ["git", "clone", g_target_git_url] )
    # try:
    #   os.chdir( local_path ) 
    # except Exception as e:
    #     print ( f"Failed enter into {local_path}, exit -1")
    #     sys.exit(-1)
    

    print("######## STEP 4:  create virtual venv and activate: " + os.getcwd() )
    _, _ = run_command( ["uv", "venv" ] )
    if g_os_name == "Windows":
        t_file = ".venv\\Scripts\\activate"
    else:
        t_file = ".venv/bin/activate"

    if os.path.isfile(t_file):
        if g_os_name == "Windows":
            command = t_file + " &&  uv add \"mcp[cli]\" httpx websocket-client pandas pydantic  --active " 
        else:
            # command = "source " + t_file + " && pip install uv  &&  uv add \"mcp[cli]\" httpx websocket-client pandas pydantic  --active   "  
            command = "source " + t_file + " && pip install uv  -i https://pypi.tuna.tsinghua.edu.cn/simple  &&  uv pip install \"mcp[cli]\" httpx websocket-client pandas pydantic -i https://pypi.tuna.tsinghua.edu.cn/simple  "  

        print (f"Now to run command [{command}]")
        os.system( command )
    else:
        print (f"Invalid virtual env [{local_path}], exit -1") 
        sys.exit(1)

    if os.path.isfile( failed_flag_file ):
        print (f"Invalid venv install [{local_path}], exit -1") 
        sys.exit(1)



    print("######## STEP 5:  create cursor configuration mcp.json ... " )
    os.chdir( g_root_folder ) 
    if os.path.isfile( ".cursor" ):
        print("Exit -1, .cursor exists in current folder and it should not be a file") 
        exit( -1 ) 

    if g_os_name == "Windows":
        mcp_string = g_default_mcp_json_string_windows.replace("__PLACEHOLDER_PYTHON_CMD__", os.path.join(g_root_folder, ".venv", "Scripts", "python.exe").replace("\\", "\\\\") ).replace("__PLACEHOLDER_PYTHON_MAIN__", os.path.join(g_root_folder, local_path, "main.py").replace("\\","\\\\")).replace("__PLACEHOLDER_ORTHOGONAL_TOKEN__", sys.argv[1] ) 
    else:
        mcp_string = g_default_mcp_json_string_mac_linux.replace("__PLACEHOLDER_UV_PATH__", g_uv_path ).replace("__PLACEHOLDER_RUNNING_FOLDER__", os.path.join(g_root_folder,local_path)).replace("__PLACEHOLDER_PYTHON_MAIN__", os.path.join(g_root_folder, local_path, "main.py")).replace("__PLACEHOLDER_ORTHOGONAL_TOKEN__",sys.argv[1]) 
    try:
        new_mcp_json_dict = json.loads(mcp_string)
    except Exception as e:
        print(f"JSON load error ：{e}")            
        sys.exit( -1 )        


    os.makedirs(".cursor", exist_ok=True)    
    mcp_config_path = os.path.join ( ".cursor", "mcp.json")
    if os.path.isfile( mcp_config_path ):
        try:
            with open(mcp_config_path, 'r', encoding='utf-8') as f:  # 推荐使用 UTF-8 编码
                mcp_json_dict = json.load(f)
        except FileNotFoundError:
            print(f"Error file not found'{mcp_config_path}'")
            sys.exit( -1 )
        except json.JSONDecodeError:
            print(f"Json file format error: '{mcp_config_path}'")
            sys.exit( -1 )
        except Exception as e:
            print(f"Unknown error: {e}")
            sys.exit( -1 )
        
        if mcp_json_dict.get("mcpServers"):
            mcp_json_dict["mcpServers"][g_mcp_server_unique_name] = new_mcp_json_dict["mcpServers"][g_mcp_server_unique_name]
        else:
            mcp_json_dict["mcpServers"] = new_mcp_json_dict["mcpServers"]

    else:
        mcp_json_dict = new_mcp_json_dict



    with open(mcp_config_path, 'w', encoding='utf-8') as f: 
        json.dump(mcp_json_dict, f, indent=4, ensure_ascii=False)  




    print ("================================= INSTALLATION SUCCESS =============================================")



if __name__ == "__main__":
    main()
