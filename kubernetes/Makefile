.POSIX:

env ?= prod
KUBECONFIG = $(shell pwd)/kubeconfig.yaml

default: boot

boot:
	python3 bootstrap

clean:
	cd kubespray &&	ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root reset.yml
