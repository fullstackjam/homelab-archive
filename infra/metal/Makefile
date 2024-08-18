.POSIX:

env ?= prod

default: init

init:
	ansible-playbook \
		--inventory inventories/${env}.yml \
		init.yml
