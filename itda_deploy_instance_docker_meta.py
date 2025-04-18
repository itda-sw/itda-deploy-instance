import sys
import os
import argparse

import utils
import lib

current_folder = os.path.dirname(os.path.abspath(__file__))
script_runner = lib.ScriptRunner(os.path.join(current_folder, "bash_scripts"))

def run(subdomain:str): 
    script_runner.run(f'docker_meta.sh {subdomain}', True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    args = parser.parse_args()

    run(args.subdomain)


    


