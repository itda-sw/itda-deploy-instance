#!/bin/bash
set -e

subdomain=${1}
docker_image=${2}
aws_region=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)

aws ecr get-login-password --region ${aws_region} | sudo docker login --username AWS --password-stdin ${docker_image}

sudo docker pull ${docker_image}

sudo docker-compose -f ${subdomain}/docker-compose-${subdomain}.yml down 
sudo docker-compose -f ${subdomain}/docker-compose-${subdomain}.yml up -d