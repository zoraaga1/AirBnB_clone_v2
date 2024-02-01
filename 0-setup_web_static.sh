#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Test content..." > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
