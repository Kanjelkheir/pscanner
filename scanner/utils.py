from typing import Tuple
import argparse


InvalidPortRange = Exception("Invalid port range")
InvalidPort = Exception("Invalid ports")

def return_args() -> Tuple[str, int, int]:
    # Initialize the arg parser
    parser = argparse.ArgumentParser(
        prog="Pscanner (port scanner)",
        description="A port scanner written in python"
        )
    
    parser.add_argument('--host', help="The host or target to scan.", required=True)
    parser.add_argument('--port', help="The range of ports to scan.", required=True)

    args = parser.parse_args()
    host: str = args.host
    port: str = args.port
    first_port = None
    second_port = None


    if len(port.split("/")) != 2:
        print(host.split("/"))
        raise InvalidPortRange 
    else:
        first_port = int(port.split("/")[0])
        second_port = int(port.split("/")[1])
        if first_port > 65535 or first_port < 1 and (second_port < 1 or second_port > 65535):
            raise InvalidPort
        

    return (host, first_port, second_port)
    