Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "docker-script", type: "shell", path:"docker.sh"
  config.vm.provision "django-project", type: "file", source: "./app", destination: "app"
end
