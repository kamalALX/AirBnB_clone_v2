#!/usr/bin/env bash
#cript that sets up a web servers for the deployment of web_static.

sudo apt-get update

sudo apt install -y nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/

echo "Hello mycvs" > sudo tee /data/web_static/releases/test/index.html > /dev/null


ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "
server {
	listen 80 default_server

	location /hbnb_static {
		alias /data/web_static/current/
	}
}
" sudo tee /etc/nginx/sites-enabled/default > /dev/null

sudo service nginx restart
