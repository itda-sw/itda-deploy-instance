import sys
import os
import argparse

import utils
import lib

script_runner = lib.ScriptRunner(os.path.join("/home/ubuntu/itda-deploy-instance", "bash_scripts"))

def aws_setup_init(subdomain:str)->bool:
    if not script_runner.run(f'aws_setup_init.sh {subdomain}'):
        return False
    return True

def aws_configure(aws_access_key:str, aws_secret_key:str) -> bool:
    print("aws_configure")
    aws_region="ap-northeast-2"
    if not script_runner.run(f'aws_configure.sh {aws_access_key} {aws_secret_key} {aws_region}'):
        return False
    return True
    
def aws_setup_route53(subdomain:str):
    print("aws_setup_route53")
    if not script_runner.run(f'aws_setup_route53.sh {subdomain}'):
        return False
    return True

def aws_exist_nginx_conf(subdomain:str):
    port = script_runner.run(f'aws_exist_nginx_conf.sh {subdomain}', True)
    return port

def docker_run(subdomain:str, port:str, tag:str) -> bool:
    print("docker_run")
    os.makedirs(f'/home/ubuntu/{subdomain}', exist_ok=True)

    aws_account="851725307474"
    aws_region="ap-northeast-2"
    docker_repo_path=f'{aws_account}.dkr.ecr.{aws_region}.amazonaws.com'
    docker_image=f'{docker_repo_path}/{subdomain}:{tag}'

    utils.generate_docker_compose(subdomain, port, docker_image)
    if not script_runner.run(f'docker_run.sh {subdomain} {docker_image} {aws_region}'):
        return False
    return True


    
def aws_setup_nginx(subdomain:str, port:str) -> bool:
    utils.generate_nginx(subdomain, port)
    if not script_runner.run(f'aws_setup_nginx.sh {subdomain}'):
        return False
    return True

def run(subdomain:str, tag: str, aws_access_key:str, aws_secret_key:str): 
    
    if not aws_setup_init(subdomain):
        return
    
    if not aws_configure(aws_access_key, aws_secret_key):
        return
    
    if not aws_setup_route53(subdomain):
        return

    port = aws_exist_nginx_conf(subdomain)
    if not port:
        port = utils.get_port()

    if not docker_run(subdomain, port, tag):
        return

    if not aws_setup_nginx(subdomain, port):
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    parser.add_argument("-t", "--tag", type=str, help="tag", required=True)
    parser.add_argument("-ak", "--access_key", type=str, help="access_key", required=True)
    parser.add_argument("-sk", "--secert_key", type=str, help="secert_key", required=True)
    args = parser.parse_args()

    run(args.subdomain, args.tag, args.access_key, args.secert_key)


    


