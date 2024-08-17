.POSIX:

env ?= prod


default: boot prerequisites

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
