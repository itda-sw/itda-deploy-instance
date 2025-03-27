#!/bin/bash
set -e

subdomain=${1}

sudo docker images --format "{{.ID}} {{.Repository}}:{{.Tag}} {{.CreatedAt}}" | grep ${subdomain}: | sort -r -k3 | tail -n +2 | awk '{print $1}' | xargs -r sudo docker rmi
