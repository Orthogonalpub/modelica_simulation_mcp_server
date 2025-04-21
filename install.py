# -*- coding: utf-8 -*-

import os
import sys
import platform
import subprocess
import shutil

g_os_name = "None"
g_root_folder = ""
g_uv_path = ""
g_target_git_url = "https://github.com/Orthogonalpub/modelica_simulation_mcp_server"

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




    if os.path.isdir( local_path):
         shutil.rmtree(local_path)




    if os.path.exists( local_path ):
        print(f"Exit -1, target path exists [{local_path}], please remove it" )
        sys.exit(1) 
    _, _ = run_command( ["git", "clone", g_target_git_url] )
    try:
      os.chdir( local_path ) 
    except Exception as e:
        print ( f"Failed enter into {local_path}, exit -1")
        sys.exit(-1)



    print("######## STEP 4:  create virtual venv and activate:  22222222222222222222222222222222 333333333333333333333333333333333" + os.getcwd() )
    _, _ = run_command( ["uv", "venv" ] )
    if g_os_name == "Windows":
        t_file = ".venv\\Scripts\\activate"
        if os.path.isfile(t_file):
            print ("11111111111111111111111111111111111111111111111", t_file, os.getcwd() )
            os.system( t_file + " ;  uv add \"mcp[cli]\" httpx websocket-client pandas pydantic  --active" )
            print ("2222222222222222222222222222222222222222")
            os.system("uv pip list")
        else:
            print (f"Invalid virtual env [{local_path}], exit -1") 
            sys.exit(1)
    else:
        t_file = ".venv/bin/activate"
        if os.path.isfile(t_file):
            result_data, result_err_msg = run_command( ["source", t_file] )
            print (f"{result_data} {result_err_msg}")
        else:
            print (f"Invalid virtual env [{local_path}], exit -1") 
            sys.exit(1)




    print ("================================= INSTALLATION SUCCESS =============================================")



if __name__ == "__main__":
    main()
