#!/bin/bash
set -e

subdomain=${1}

mkdir -p /home/ubuntu/${subdomain}/ws
mkdir -p /home/ubuntu/${subdomain}/ws/DBs
mkdir -p /home/ubuntu/${subdomain}/ws/configs
mkdir -p /home/ubuntu/${subdomain}/ws/canvas-input
mkdir -p /home/ubuntu/${subdomain}/ws/itda-hwdoc
