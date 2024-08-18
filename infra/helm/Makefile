.POSIX:

export KUBECONFIG = $(shell pwd)/../kubeconfig.yaml

.PHONY: default bootstrap kustomize helm-diff-check wait-metallb-speaker

default: bootstrap kustomize

helm-diff-check:
	@helm plugin list | grep -q diff || helm plugin install https://github.com/databus23/helm-diff

bootstrap: helm-diff-check
	helmfile apply

wait-metallb-speaker:
	@echo "Checking if metallb-speaker Pods exist and are ready..."
	@kubectl get pod -l app.kubernetes.io/component=speaker -n metallb-system > /dev/null 2>&1 || { echo "No metallb-speaker Pods found. Exiting..."; exit 1; }
	@kubectl wait --for=condition=Ready pod -l app.kubernetes.io/component=speaker -n metallb-system --timeout=300s

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

clean-helm:
	helm uninstall metallb -n metallb-system
	kubectl delete ns metallb-system
