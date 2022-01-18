#!/bin/bash

#download the current stable release of Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#apply executable permissions to the binary
sudo chmod +x /usr/local/bin/docker-compose

#test the installation
docker-compose --version