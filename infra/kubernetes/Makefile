.PHONY: bootstrap

env ?= prod

all: bootstrap

bootstrap:
	python3 bootstrap

clean:
	cd kubespray &&	ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root reset.yml
