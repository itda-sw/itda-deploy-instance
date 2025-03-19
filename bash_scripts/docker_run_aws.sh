#!/bin/bash
set -e

instance=${1}
subdomain=${2}
docker_image=${3}

key_path=${PWD}/../..

subdomain=${1}
docker_image=${2}

aws ecr get-login-password | sudo docker login --username AWS --password-stdin ${docker_image}

sudo docker pull ${docker_image}

sudo docker-compose -f ${subdomain}/docker-compose-${subdomain}.yml down 
sudo docker-compose -f ${subdomain}/docker-compose-${subdomain}.yml up -d