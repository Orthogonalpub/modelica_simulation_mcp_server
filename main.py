
from typing import Any
import sys
import os
import websocket
import json
import time
import ssl
import httpx
import logging
from logging.handlers import RotatingFileHandler
import datetime
import asyncio
import copy

from mcp.server.fastmcp import FastMCP
import matplotlib.pyplot as plt
from pydantic import Field


USER_ORTH_TOKEN=""

# ORTHOGONAL_HOST="192.168.116.130"
# ORTHOGONAL_WS_URL=f"ws://{ORTHOGONAL_HOST}/ws/commontask/0/" 
# ORTHOGONAL_HTTP_URL=f"http://{ORTHOGONAL_HOST}/api/v2/mcp/mcp_checker" 

ORTHOGONAL_HOST="paas.orthogonal.cc"
ORTHOGONAL_WS_URL=f"wss://{ORTHOGONAL_HOST}/ws/commontask/0/" 
ORTHOGONAL_HTTP_URL=f"https://{ORTHOGONAL_HOST}/api/v2/mcp/mcp_checker" 

USER_AGENT = "MCP server"

SIMULATION_CMD="o_mcp_simulate"

modelica_source_code=""
modelica_stop_time=1.0

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(
    'orth.log',
    maxBytes=1024*1024*20,
    backupCount=2,
    encoding='utf-8' 
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

mcp = FastMCP("orthogonal-modelica")

ws_response_obj={}

def convert_orth2mcp(orth_obj: dict) -> None:

    global ws_response_obj

    ws_response_obj = {
        "simulation_status": "FAILED",        
        "simulation_error_messsage": "invalid response from modelica backend service",
        "simulation_data_values": {}
    }

    if orth_obj.get('ws_ret_code') is None or orth_obj.get('ws_ret_msg') is None:
        return

    ws_response_obj['simulation_status'] = orth_obj.get('ws_ret_code')
    ws_response_obj['simulation_error_messsage'] = orth_obj.get('ws_ret_msg')
    ws_response_obj['simulation_data_values'] = copy.deepcopy(orth_obj.get('ws_ret_data'))

    logger.debug(f"#### simulation data values ======================: {ws_response_obj['simulation_data_values']}")


def plot_simulation_data(ws_response_obj: dict):

    if ws_response_obj.get("simulation_data_values") is None:
        return

    simulation_data_values = ws_response_obj.get("simulation_data_values")

    fig, ax = plt.subplots() 
    x_axis = simulation_data_values.get("time")
    for key, value in simulation_data_values.items():
        if key != "time":
            ax.plot(x_axis, value, label=key)
    ax.legend()
    plt.show()


def on_message(ws, message):

    global ws_response_obj

    ws_response_obj={}

    # logger.debug("###### WebSocket Received:" + str(message) )

    try:
        json_obj = json.loads( message )  
        if json_obj.get("ws_msg_type")=="response" and json_obj.get("ws_method_param") and json_obj["ws_method_param"].get("command")==SIMULATION_CMD:    
         
            logger.debug("####################  Orthogonal Simulation returns： " + str(json_obj) ) 

            if json_obj.get("ws_ret_code") == "SUCCESS" or json_obj.get("ws_ret_code") == "FAILED" or json_obj.get("ws_ret_code") == "STOPPED":
                convert_orth2mcp(json_obj)
                ws.close()

    except Exception as e:
        ws.close() 
        logger.error ("Error: "  +  str( json_obj ) )


def on_error(ws, error):
    print(f"Error occurred: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")

def on_open(ws):

    global modelica_source_code
    global modelica_stop_time

    data_dict = {
        "ws_msg_type": "request", 
        "ws_method_name":"wsfunc_mb_runcommand", 
        "ws_timeout":30, "ws_seq": "123456780xxx", 
        "ws_method_param":{ 
            "command": SIMULATION_CMD, 
            "command_param": {
                "mo_src_code":  modelica_source_code,
                "mo_stop_time":  modelica_stop_time
            }
        } 
    }

    logger.debug("### Connection established sent:### " + str(json.dumps(data_dict))  )
    ws.send(json.dumps(data_dict))


def orth_simulate(modelica_code: str, stop_time: float = 1.0):

    global modelica_source_code
    global modelica_stop_time
    global USER_ORTH_TOKEN

    modelica_source_code = modelica_code
    modelica_stop_time = stop_time

    USER_ORTH_TOKEN = os.environ.get("ORTHOGONAL_TOKEN")
    if USER_ORTH_TOKEN is None or len(USER_ORTH_TOKEN) == 0:
        return {
                    "simulation_status": "FAILED",        
                    "simulation_error_messsage": "Env variable ORTHOGONAL_TOKEN is invalid or missing",
                    "simulation_data_values": {}
                } 

    custom_headers = {
        "Authorization": f"Bearer {USER_ORTH_TOKEN}",
        "Sec-WebSocket-Protocol": USER_ORTH_TOKEN
    }

    ws = websocket.WebSocketApp(
        ORTHOGONAL_WS_URL,
        header=custom_headers,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever(
        sslopt={"cert_reqs": ssl.CERT_NONE},
        ping_interval=120,
        ping_timeout=90
    )


@mcp.tool()
async def modelica_service_available() -> bool:
    """Check whether backend modelica service is running 

    Args:
        None

    Returns:
        bool: if backend modelica service is running, then return true, otherwise return false
    """

    USER_ORTH_TOKEN = os.environ.get("ORTHOGONAL_TOKEN")
    if USER_ORTH_TOKEN is None or len(USER_ORTH_TOKEN) == 0:
        return {
                    "simulation_status": "FAILED",        
                    "simulation_error_messsage": "Env variable ORTHOGONAL_TOKEN is invalid or missing",
                    "simulation_data_values": {}
                } 

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
        # "Host": ORTHOGONAL_HOST,
        "Authorization": "Bearer "+ USER_ORTH_TOKEN,
        # "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(ORTHOGONAL_HTTP_URL, headers=headers, timeout=60.0)
            
            response.raise_for_status()
            return True
        except httpx.ConnectError as e:
            logger.error(f"Connection error: {e}")
            return False
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e}, status code: {e.response.status_code}, response text: {e.response.text}")
            return False
        except Exception as e:
            logger.exception(f"An unexpected error occurred: {e}") 
            return False


@mcp.tool()
async def modelica_simulate(modelica_code: str = Field(default="", description="Modelica source code, the type is string"), 
                            stop_time: float = Field(default=1.0, gt=0.0, le=30.0, description="Stop time of simulation in seconds, the type is float and default value is 1.0")
                            ) -> dict:

    """Run simulation with modelica code and return simulation result object of dict type

    Args:
        modelica_code (str): the input modelica code, which will be sent to modelica simulation mcp server to simuate. The input modelica source code must be valid, otherwise simulation will fail

        stop_time (float): the stop time of the simulation in seconds, default is 1.0 
        
    Returns:
        dict: the simulation result， it is an object containing below keys:                
        * `"simulation_status"` (str): "SUCCESS" or "FAILED", to indicate the simulation is success or failed.     
        * `"simulation_error_messsage"` (str): the detailed error message if simulation fails, which can be used to fix the problem, if success, it will be an empty string.
        * `"simulation_data_values"` (dict): an dict object for simulation data values, the keys are the names of simulation data, the values are value-list of the corresponding columns.
    """



    USER_ORTH_TOKEN = os.environ.get("ORTHOGONAL_TOKEN")
    if USER_ORTH_TOKEN is None or len(USER_ORTH_TOKEN) == 0:
        return {
                    "simulation_status": "FAILED",        
                    "simulation_error_messsage": "Env variable ORTHOGONAL_TOKEN is invalid or missing",
                    "simulation_data_values": {}
                } 

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Authorization": "Bearer "+ USER_ORTH_TOKEN,
        "Content-Type": "application/json",
    }

    # print ( headers )
    async with httpx.AsyncClient() as client:

        global ws_response_obj

        try:
            # response = await client.get(ORTHOGONAL_HTTP_URL, headers=headers, timeout=30.0)
            # response.raise_for_status()
            
            if len(modelica_code) <= 2:
                ws_response_obj = {
                    "simulation_status": "FAILED",        
                    "simulation_error_messsage": "invalid modelica source code, length is too short",
                    "simulation_data_values": {}
                } 
                return ws_response_obj


            orth_simulate(modelica_code, stop_time) 

            check_interval = 2
            check_cnt = 0

            while True:

                if check_cnt >=50:
                    return {"response":"API call timeout"}

                if ws_response_obj["simulation_status"] == "FAILED" or ws_response_obj["simulation_status"] == "SUCCESS":
                    if ws_response_obj["simulation_status"] == "SUCCESS":
                        plot_simulation_data(ws_response_obj)
                    return ws_response_obj  
        
                check_cnt = check_cnt + 1

                logger.debug(f"#### waiting for simulation result, check_cnt: {check_cnt}")
                await asyncio.sleep(check_interval)  
   

        except Exception as e:
            logger.debug ("Error:" + str(e)    )
            return {"response":"error" + str(e)}
 

####  mcp::::::      run --active --with mcp mcp run orthogonal-mcp-main.py    
if __name__ == "__main__":

    mcp.run(transport='stdio')



