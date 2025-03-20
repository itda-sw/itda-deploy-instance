#!/bin/bash
set -e

subdomain=${1}
tag=${2}
aws_account=$(aws sts get-caller-identity --query "Account" --output text)
aws_region=$(aws configure get region)
docker_repo_path=${aws_account}.dkr.ecr.${aws_region}.amazonaws.com
docker_image=${docker_repo_path}/${subdomain}:${tag}
echo ${docker_image}