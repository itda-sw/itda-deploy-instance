import sys
import os
import argparse

import utils
import lib

current_folder = os.path.dirname(os.path.abspath(__file__))
script_runner = lib.ScriptRunner(os.path.join(current_folder, "bash_scripts"))

def docker_pull(subdomain:str, tag:str) -> bool:
    print("docker_pull")
    docker_image = script_runner.run(f'get_docker_image.sh {subdomain} {tag}', True)

    if not script_runner.run(f'docker_pull.sh {docker_image}'):
        return False
    return True

def run(subdomain:str, tag: str):    
    if not docker_pull(subdomain, tag):
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    parser.add_argument("-t", "--tag", type=str, help="tag", required=True)
    args = parser.parse_args()

    run(args.subdomain, args.tag)


    


