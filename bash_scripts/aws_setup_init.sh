#!/bin/bash
set -e

sudo apt update && sudo apt upgrade -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/home/ubuntu/awscliv2.zip"
sudo apt install unzip
unzip -o /home/ubuntu/awscliv2.zip -d /home/ubuntu
sudo /home/ubuntu/aws/install --update
aws --version

sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
docker --version

sudo apt install -y docker-compose

sudo apt-get install -y nginx

sudo apt-get install -y certbot python3-certbot-nginx
