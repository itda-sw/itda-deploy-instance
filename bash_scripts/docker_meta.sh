#!/bin/bash
set -e

subdomain=${1}

base_dir="/home/ubuntu/${subdomain}/meta"
meta_json="${base_dir}/meta.json"
meta_log="${base_dir}/meta.log"

mkdir -p "${base_dir}"
sudo docker cp "${subdomain}:/meta/meta.json" "${meta_json}"
sudo bash -c "cat '${meta_json}' >> '${meta_log}'; echo >> '${meta_log}'"
