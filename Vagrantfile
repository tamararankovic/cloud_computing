Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "docker script", type: "shell", path: "./scripts/docker.sh"
  config.vm.provision "docker compose script", type: "shell", path: "./scripts/docker-compose.sh"
  config.vm.provision "app", type: "file", source: "./app", destination: "$HOME"
  config.vm.provision "run script", type: "shell", path: "./scripts/run.sh", run: "always"

  config.vm.network "forwarded_port", guest: 80, host: 8080
end
