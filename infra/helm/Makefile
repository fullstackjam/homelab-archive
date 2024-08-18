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
	@echo "Waiting for metallb-speaker Pods to be created and initialized..."
	@for i in {1..30}; do \
		if kubectl get pod -l app.kubernetes.io/component=speaker -n metallb-system > /dev/null 2>&1; then \
			echo "MetalLB speaker Pods found. Checking if they are ready..."; \
			kubectl wait --for=condition=Ready pod -l app.kubernetes.io/component=speaker -n metallb-system --timeout=300s; \
			break; \
		else \
			echo "No metallb-speaker Pods found. Retrying in 10 seconds..."; \
			sleep 10; \
		fi; \
	done

kustomize: wait-metallb-speaker
	kubectl apply -k kustomize

patch_hubble_ui:
	kubectl patch svc hubble-ui -n kube-system -p '{"spec": {"type": "LoadBalancer"}}'

clean-helm:
	helm uninstall metallb -n metallb-system
	kubectl delete ns metallb-system
