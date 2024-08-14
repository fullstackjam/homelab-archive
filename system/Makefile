.POSIX:

export KUBECONFIG = $(shell pwd)/../metal/kubeconfig.yaml

.PHONY: default bootstrap kustomize helm-diff-check wait-metallb-speaker patch-longhorn-service

default: bootstrap patch-longhorn-service kustomize

helm-diff-check:
	@helm plugin list | grep -q diff || helm plugin install https://github.com/databus23/helm-diff

bootstrap: helm-diff-check
	helmfile apply

wait-metallb-speaker:
	@echo "Checking if metallb-speaker Pods are ready..."
	@kubectl wait --for=condition=Ready pod -l app.kubernetes.io/component=speaker -n metallb-system --timeout=300s || true

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

patch-longhorn-service:
	@echo "Patching longhorn-frontend service to LoadBalancer..."
	@kubectl patch svc longhorn-frontend -n longhorn-system -p '{"spec": {"type": "LoadBalancer"}}'

clean:
	kubectl -n longhorn-system patch -p '{"value": "true"}' --type=merge lhs deleting-confirmation-flag
	helm uninstall longhorn -n longhorn-system
	helm uninstall metallb -n metallb-system
	kubectl delete ns longhorn-system metallb-system
