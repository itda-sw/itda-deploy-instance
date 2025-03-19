#!/bin/bash
set -e

sudo mv /home/ubuntu/ec2_itda.conf /etc/nginx/conf.d/ && sudo systemctl restart nginx
