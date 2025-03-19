#!/bin/bash
set -e

subdomain=${1}

instance_ip4=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)

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