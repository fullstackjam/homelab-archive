.POSIX:

export KUBECONFIG = $(shell pwd)/../kubeconfig.yaml

.PHONY: default bootstrap kustomize helm-diff-check wait-metallb-speaker install-helmfile patch_svc

default: bootstrap kustomize patch_svc

helm-diff-check:
	@helm plugin list | grep -q diff || helm plugin install https://github.com/databus23/helm-diff

bootstrap: helm-diff-check install-helmfile

install-helmfile:
	@echo "Installing Helmfile..."
	@helmfile apply

wait-metallb-speaker:
	@echo "Waiting for 120 seconds to allow MetalLB speaker Pods to initialize..."
	@sleep 60

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

patch_svc:
	kubectl patch svc hubble-ui -n kube-system -p '{"spec": {"type": "LoadBalancer"}}'
	kubectl patch svc longhorn-frontend -n longhorn-system -p '{"spec": {"type": "LoadBalancer"}}'

clean-helm:
	helm uninstall metallb -n metallb-system
	kubectl delete ns metallb-system
