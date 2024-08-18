.POSIX:

export KUBECONFIG = $(shell pwd)/../kubeconfig.yaml

.PHONY: default bootstrap kustomize helm-diff-check wait-metallb-speaker patch-longhorn-service

default: bootstrap kustomize

helm-diff-check:
	@helm plugin list | grep -q diff || helm plugin install https://github.com/databus23/helm-diff

bootstrap: helm-diff-check
	helmfile apply

wait-metallb-speaker:
	@echo "Checking if metallb-speaker Pods exist and are ready..."
	@kubectl get pod -l app.kubernetes.io/component=speaker -n metallb-system
	@kubectl wait --for=condition=Ready pod -l app.kubernetes.io/component=speaker -n metallb-system --timeout=300s

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

patch-longhorn-service:
	@echo "Patching longhorn-frontend service to LoadBalancer..."
	@kubectl patch svc longhorn-frontend -n longhorn-system -p '{"spec": {"type": "LoadBalancer"}}'

clean-helm:
	helm uninstall metallb -n metallb-system
	kubectl delete ns metallb-system
