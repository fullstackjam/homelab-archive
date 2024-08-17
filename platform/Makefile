.POSIX:

export KUBECONFIG = $(shell pwd)/../bootstrap/kubeconfig.yaml

.PHONY: bootstrap
bootstrap:
	ansible-playbook \
		bootstrap.yml
