Vagrant.configure("2") do |config|
  config.vm.box = "output/ubuntu-20.04-ansible.box"

  # VM 1: DNS, NGINX, JFrog
  config.vm.define "vm1" do |vm1|
    vm1.vm.hostname = "robot1"
    vm1.vm.network "private_network",  ip: "192.168.232.129"
    vm1.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
    vm1.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/playbook_vm1.yml"
    end
  end

  # VM 2: Jenkins
  config.vm.define "vm2" do |vm2|
    vm2.vm.hostname = "robot2"
    vm2.vm.network "private_network",  ip: "192.168.232.129"
    vm2.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
    vm2.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/playbook_vm2.yml"
    end
  end

  # VM 3: Kubernetes (Can be provisioned separately with another playbook if needed)
  config.vm.define "vm3" do |vm3|
    vm3.vm.hostname = "robot3"
    vm3.vm.network "private_network",  ip: "192.168.232.129"
    vm3.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 2
    end
    vm3.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/playbook_vm3.yml"
    end
  end
end
