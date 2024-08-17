.POSIX:

export KUBECONFIG = $(shell pwd)/../kubernetes/kubeconfig.yaml

.PHONY: bootstrap
bootstrap:
	ansible-playbook \
		bootstrap.yml
