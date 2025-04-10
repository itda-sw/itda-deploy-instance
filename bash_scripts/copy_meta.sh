#!/bin/bash
set -e

subdomain=${1}

mkdir -p /home/ubuntu/${subdomain}/meta
sudo docker cp ${subdomain}:/meta/meta.json /home/ubuntu/${subdomain}/meta/