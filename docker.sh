#!/bin/bash

#uninstalling old versions
sudo apt-get remove --yes docker docker-engine docker.io containerd runc

#setting up the repository
sudo apt-get update
sudo apt-get --yes --no-install-recommends install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


#installing docker engine
sudo apt-get update
sudo apt-get --yes --no-install-recommends install docker-ce docker-ce-cli containerd.io

#checking if everything works fine
sudo docker run hello-world