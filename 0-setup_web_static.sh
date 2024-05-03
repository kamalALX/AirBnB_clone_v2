#!/usr/bin/env bash
#cript that sets up a web servers for the deployment of web_static.

sudo apt-get update

sudo apt install -y nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > sudo tee /data/web_static/releases/test/index.html


ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "
server {
	listen 80 default_server;

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
" > sudo tee /etc/nginx/sites-enabled/default

sudo service nginx restart
