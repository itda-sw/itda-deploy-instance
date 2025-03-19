import sys
import os
import argparse

sys.path.append(os.getenv("ENV_PATH"))
from lib import ScriptRunner
from itda_dev import init_run, build_run
import utils

def aws_setup_route53(instance:str, subdomain:str):
    print("aws_setup_route53")
    script_path  = os.path.join(os.getenv("DEPLOY_PATH"), "bash_scripts")
    script_runner = ScriptRunner(script_path)

    if script_runner.run(f'aws_setup_route53.sh {instance} {subdomain}'):
        return -1

def docker_run_aws(instance:str, subdomain:str, port:str, tag:str):
    print("docker_run_aws")
    script_path  = os.path.join(os.getenv("DEPLOY_PATH"), "bash_scripts")
    script_runner = ScriptRunner(script_path)

    aws_account="851725307474"
    aws_region="ap-northeast-2"
    docker_repo_path=f'{aws_account}.dkr.ecr.{aws_region}.amazonaws.com'
    docker_image=f'{docker_repo_path}/{subdomain}:{tag}'

    utils.generator_docker_compose(subdomain, port, docker_image)
    if script_runner.run(f'docker_run_aws.sh {instance} {subdomain} {docker_image}'):
        return -1

def aws_setup_nginx(instance:str, subdomain:str, port:str):
    script_path  = os.path.join(os.getenv("DEPLOY_PATH"), "bash_scripts")
    script_runner = ScriptRunner(script_path)

    utils.generator_nginx(subdomain, port)
    if script_runner.run(f'aws_setup_nginx.sh {instance} {subdomain}'):
        return -1

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


    


