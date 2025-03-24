#!/bin/bash
set -e

subdomain=${1}

sudo docker-compose -f /home/ubuntu/${subdomain}/docker-compose-${subdomain}.yml down 
sudo docker-compose -f /home/ubuntu/${subdomain}/docker-compose-${subdomain}.yml up -d