#!/usr/bin/env bash
# This script sets up the web servers for the deployment of a web_static

# Update package lists and install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx
# Allow Nginx HTTP through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories if they don't already exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/Index.html
# Create a fake HTML file with simple content
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School and Alx tasks want to kill me!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

# Exit the script successfully
exit 0

