Vagrant.configure("2") do |config|
  config.vm.box = "output/ubuntu-20.04-ansible.box"

  # VM 1: DNS, NGINX, JFrog
  config.vm.define "vm1" do |vm1|
    vm1.vm.hostname = "robot1"
    vm1.vm.network "private_network", type: "dhcp"
    vm1.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  end

  # VM 2: Jenkins
  config.vm.define "vm2" do |vm2|
    vm2.vm.hostname = "robot2"
    vm2.vm.network "private_network", type: "dhcp"
    vm2.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  end

  # VM 3: Kubernetes (Can be provisioned separately with another playbook if needed)
  config.vm.define "vm3" do |vm3|
    vm3.vm.hostname = "robot3"
    vm3.vm.network "private_network", type: "dhcp"
    vm3.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 2
    end
  end
end
