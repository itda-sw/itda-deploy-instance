import sys
import os
import argparse

import utils
import lib

current_folder = os.path.dirname(os.path.abspath(__file__))
script_runner = lib.ScriptRunner(os.path.join(current_folder, "bash_scripts"))

def aws_exist_nginx_conf(subdomain:str):
    port = script_runner.run(f'aws_exist_nginx_conf.sh {subdomain}', True)
    return port

def aws_setup_nginx(subdomain:str, port:str) -> bool:
    utils.generate_nginx(subdomain, port)
    if not script_runner.run(f'aws_setup_nginx.sh {subdomain}'):
        return False
    return True

def run(subdomain:str): 
    port = aws_exist_nginx_conf(subdomain)
    if not port:
        port = utils.get_port()

    if not aws_setup_nginx(subdomain, port):
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    args = parser.parse_args()

    run(args.subdomain)


    


