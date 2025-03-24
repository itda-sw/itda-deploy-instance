#!/bin/bash
set -e

subdomain=${1}

  sudo certbot --nginx --email hungry.cho@itdasemi.com --agree-tos --no-eff-email --redirect -d ${subdomain}.soc-canvas.com
  sudo systemctl restart nginx