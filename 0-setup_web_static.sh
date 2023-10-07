#!/usr/bin/env bash
# this script for Prepare my webservers (web-01 & web-02)

# this uncomment for easy debugging
#for set -x

# for colors
blue='\e[1;34m'
#brown='\e[0;33m'
green='\e[1;32m'
reset='\033[0m'

echo -e "${blue}Updating and doing some minor checks...${reset}\n"

# this for install nginx if not present
if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y -qq && \
	     sudo apt-get install -y nginx
fi

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

# for Create directories...
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# for create index.html for test directory
echo "<h1>Welcome to th3gr00t.tech <\h1>" | sudo dd status=none of=/data/web_static/releases/test/index.html

# for create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# for give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# for backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# for Set-up the content of /data/web_static/current/ to redirect
# for to domain.tech/hbnb_static
sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

echo -e "${green}Completed${reset}"
