#!/bin/bash
set -e

aws_access_key=${1}
aws_secret_key=${2}
aws_region=${3}

aws configure set aws_access_key_id ${aws_access_key}
aws configure set aws_secret_access_key ${aws_secret_key}
aws configure set region ${aws_region}
aws configure set output json