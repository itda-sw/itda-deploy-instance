#!/bin/bash
set -e

subdomain=${1}

port=$(grep -oP 'proxy_pass http://localhost:\K[0-9]+' /etc/nginx/sites-available/${subdomain}.soc-canvas.com1)
echo ${port}