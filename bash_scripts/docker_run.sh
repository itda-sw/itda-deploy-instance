#!/bin/bash
set -e

subdomain=${1}
docker_image=${2}
aws_region=$(aws configure get region)

aws ecr get-login-password --region ${aws_region} | sudo docker login --username AWS --password-stdin ${docker_image}

sudo docker pull ${docker_image}

sudo docker-compose -f /home/ubuntu/${subdomain}/docker-compose-${subdomain}.yml down 
sudo docker-compose -f /home/ubuntu/${subdomain}/docker-compose-${subdomain}.yml up -d