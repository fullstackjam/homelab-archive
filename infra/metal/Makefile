.POSIX:

env ?= prod

default: boot init

boot:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		boot.yml

init:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		init.yml
