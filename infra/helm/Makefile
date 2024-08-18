.POSIX:

export KUBECONFIG = $(shell pwd)/../kubeconfig.yaml

.PHONY: default bootstrap kustomize helm-diff-check wait-metallb-speaker install-metallb patch_hubble_ui

default: bootstrap kustomize patch_hubble_ui

helm-diff-check:
	@helm plugin list | grep -q diff || helm plugin install https://github.com/databus23/helm-diff

bootstrap: helm-diff-check install-metallb

install-metallb:
	@echo "Installing MetalLB..."
	@helmfile apply

wait-metallb-speaker:
	@echo "Waiting for 10 seconds to allow metallb-speaker Pods to initialize..."
	@sleep 10
	@echo "Checking if metallb-speaker Pods exist and are ready..."
	@kubectl get pod -l app.kubernetes.io/component=speaker -n metallb-system > /dev/null 2>&1 || { echo "No metallb-speaker Pods found. Exiting..."; exit 1; }
	@kubectl wait --for=condition=Ready pod -l app.kubernetes.io/component=speaker -n metallb-system --timeout=300s || (echo "MetalLB speaker Pods are not ready"; exit 1)

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

patch_hubble_ui:
	kubectl patch svc hubble-ui -n kube-system -p '{"spec": {"type": "LoadBalancer"}}'

clean-helm:
	helm uninstall metallb -n metallb-system
	kubectl delete ns metallb-system
