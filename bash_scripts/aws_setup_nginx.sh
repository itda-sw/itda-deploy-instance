#!/bin/bash
set -e

subdomain=${1}

sudo mv /home/ubuntu/${subdomain}/${subdomain}.soc-canvas.com /etc/nginx/sites-available/
sudo rm -rf /etc/nginx/sites-enabled/${subdomain}.soc-canvas.com
sudo ln -s /etc/nginx/sites-available/${subdomain}.soc-canvas.com /etc/nginx/sites-enabled/ || true
sudo systemctl restart nginx

sudo certbot --nginx --email hungry.cho@itdasemi.com --agree-tos --no-eff-email --redirect -d ${subdomain}.soc-canvas.com
sudo systemctl restart nginx
