#!/bin/bash
set -e

instance=${1}
subdomain=${2}

instance_ip4=$(aws ec2 describe-instances --filters \
		"Name=tag:Name,Values=${instance}" \
		--query 'Reservations[].Instances[].PublicIpAddress' \
		--output text)

## aws_setup_router53
change_batch=$(cat <<EOF
{
  "Changes": [
    {
      "Action": "UPSERT",
      "ResourceRecordSet": {
        "Name": "${subdomain}.soc-canvas.com",
        "Type": "A",
        "TTL": 300,
        "ResourceRecords": [
          {
            "Value": "${instance_ip4}"
          }
        ]
      }
    }
  ]
}
EOF
)

aws route53 change-resource-record-sets \
  --hosted-zone-id Z08473923N105TMHAFCAQ \
  --change-batch "${change_batch}"