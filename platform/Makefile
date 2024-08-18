.POSIX:

export KUBECONFIG = $(shell pwd)/../infra/kubeconfig.yaml

.PHONY: bootstrap
bootstrap:
	ansible-playbook \
		bootstrap.yml
