import sys
import os
import argparse

import utils
import lib

script_runner = lib.ScriptRunner(os.path.join("/home", "itda_deploy_instnace", "bash_scripts"))

def aws_setup_route53(instance:str, subdomain:str):
    print("aws_setup_route53")
    if not script_runner.run(f'aws_setup_route53.sh {instance} {subdomain}'):
        return False

def docker_run_aws(instance:str, subdomain:str, port:str, tag:str):
    print("docker_run_aws")
    aws_account="851725307474"
    aws_region="ap-northeast-2"
    docker_repo_path=f'{aws_account}.dkr.ecr.{aws_region}.amazonaws.com'
    docker_image=f'{docker_repo_path}/{subdomain}:{tag}'

    utils.generate_docker_compose(subdomain, port, docker_image)
    if not script_runner.run(f'docker_run_aws.sh {instance} {subdomain} {docker_image}'):
        return False

def aws_setup_nginx(instance:str, subdomain:str, port:str):
    utils.generate_nginx(subdomain, port)
    if not script_runner.run(f'aws_setup_nginx.sh {instance} {subdomain}'):
        return False

def run(instance: str, subdomain:str, tag: str, port: str):
    if aws_setup_route53(instance, subdomain):
        return

    if docker_run_aws(instance, subdomain, port, tag):
        return

    if aws_setup_nginx(instance, subdomain, port):
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("-s", "--subdomain", type=str, help="subdomain", required=True)
    parser.add_argument("-i", "--instance", type=str, help="instance", required=True)
    parser.add_argument("-t", "--tag", type=str, help="tag", required=True)
    parser.add_argument("-p", "--port", type=str, help="port", required=True)
    args = parser.parse_args()

    run(args.assignment, args.tag, args.port)


    


