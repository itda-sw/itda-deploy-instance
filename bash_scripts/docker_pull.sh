#!/bin/bash
set -e

docker_image=${1}
aws_region=$(aws configure get region)

aws ecr get-login-password --region ${aws_region} | sudo docker login --username AWS --password-stdin ${docker_image}

sudo docker pull ${docker_image}