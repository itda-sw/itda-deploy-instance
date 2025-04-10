#!/bin/bash
set -e

subdomain=${1}

sudo docker cp ${subdomain}:/meta/meta.json /home/ubuntu/${subdomain}/meta/