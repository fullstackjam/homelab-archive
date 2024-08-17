.POSIX:

env ?= prod
export KUBECONFIG = $(shell pwd)/kubeconfig.yaml

default: boot prerequisites k8s

boot: ~/.ssh/id_rsa
	ansible-playbook \
		--inventory inventories/${env}.yml \
		boot.yml

prerequisites:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		cluster.yml

console:
	ansible-console \
		--inventory inventories/${env}.yml

clean:
	cd kubespray &&	ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root reset.yml

k8s:
	python3 bootstrap
