# -*- coding: utf-8 -*-

import os
import sys
import platform
import subprocess

g_os_name = "None"
g_root_folder = ""

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

    if sys.version_info < (3, 10):
        print("Exit -1, python Version must >= 3.10") 
        exit( -1 )

    # STEP 1:  ensure orthogonal token is given ########################################################
    if len(sys.argv) != 2:
        print("Exit -1, ORTHOGONAL TOKEN must be set") 
        print(f"Example: {sys.argv[0]}  orthogonal_token ") 
        exit( -1 ) 

    g_os_name = platform.system()

    g_root_folder = os.path.dirname(os.path.abspath(__file__))

    # data_file = os.path.join(script_dir, "data", "my_data.txt")  # 使用 os.path.join


    # step 2:  check orthogonal token ########################################################
    if g_os_name == "Windows":
        command = ["cmd", "/c", "dir /b"]  # Execute 'dir /b' using cmd.exe
    elif g_os_name == "Darwin":
        command = ["ls", "-l"]
    elif g_os_name == "Linux":
        command = ["ls", "-l"]
    else:
        print("Not supported os system", g_os_name )
        sys.exit(1)

    result_data, result_err_msg = run_command( command )

    print ("=============================================")
    print (result_data, result_err_msg ) 


if __name__ == "__main__":
    main()
