.POSIX:

env ?= prod


default: boot prerequisites

boot: ~/.ssh/id_rsa
	ansible-playbook \
		--inventory inventories/${env}.yml \
		boot.yml

init:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		init.yml
