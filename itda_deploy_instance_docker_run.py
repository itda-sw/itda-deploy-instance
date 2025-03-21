import sys
import os
import argparse

import utils
import lib

current_folder = os.path.dirname(os.path.abspath(__file__))
script_runner = lib.ScriptRunner(os.path.join(current_folder, "bash_scripts"))

def docker_init(subdomain:str):
    if not script_runner.run(f'docker_init.sh {subdomain}'):
        return False
    return True

def docker_run(subdomain:str, port:str, tag:str) -> bool:
    print("docker_run")
    docker_image = script_runner.run(f'get_docker_image.sh {subdomain} {tag}', True)

    utils.generate_docker_compose(subdomain, port, docker_image)
    if not script_runner.run(f'docker_run.sh {subdomain} {docker_image}'):
        return False
    return True

def run(subdomain:str, tag: str): 
    
    port = utils.get_nginx_port(subdomain)
    if not port:
        return 

    if not docker_init(subdomain):
        return
    
    if not docker_run(subdomain, port, tag):
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    parser.add_argument("-t", "--tag", type=str, help="tag", required=True)
    args = parser.parse_args()

    run(args.subdomain, args.tag)


    


