sudo apt update && sudo apt upgrade -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
aws --version

sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
docker --version

sudo apt install -y docker-compose

sudo apt-get install nginx

sudo apt-get install certbot python3-certbot-nginx
