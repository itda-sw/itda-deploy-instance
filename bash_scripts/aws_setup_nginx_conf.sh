#!/bin/bash
set -e

sudo mv /home/ubuntu/nginx_conf.conf /etc/nginx/conf.d/
sudo systemctl restart nginx
