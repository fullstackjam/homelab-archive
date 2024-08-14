.POSIX:

env ?= prod
export KUBECONFIG = $(shell pwd)/kubeconfig.yaml

default: boot prerequisites kubespray

boot: ~/.ssh/id_rsa
	ansible-playbook \
		--inventory inventories/${env}.yml \
		boot.yml

prerequisites:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		cluster.yml

kubespray:
	cd ../kubespray && ansible-playbook -i inventory/mycluster/hosts.yaml -u root -b cluster.yml

console:
	ansible-console \
		--inventory inventories/${env}.yml
