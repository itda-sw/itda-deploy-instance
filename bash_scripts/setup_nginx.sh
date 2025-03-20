#!/bin/bash
set -e

subdomain=${1}

if [ -f "/etc/nginx/sites-available/${subdomain}.soc-canvas.com" ]; then
    echo "파일이 이미 존재합니다. 스킵합니다."
else
  sudo mv /home/ubuntu/${subdomain}.soc-canvas.com /etc/nginx/sites-available/
  sudo rm -rf /etc/nginx/sites-enabled/${subdomain}.soc-canvas.com
  sudo ln -s /etc/nginx/sites-available/${subdomain}.soc-canvas.com /etc/nginx/sites-enabled/ || true
  sudo systemctl restart nginx

  sudo certbot --nginx --email hungry.cho@itdasemi.com --agree-tos --no-eff-email --redirect -d ${subdomain}.soc-canvas.com
  sudo systemctl restart nginx
fi