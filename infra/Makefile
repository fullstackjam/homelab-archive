.PHONY: all metal k8s helm

default: metal k8s

# metalialize the system using Ansible playbook
metal:
	make -C metal

# Bootstrap Kubernetes cluster
k8s:
	cd kubernetes && python3 bootstrap

# Deploy Helm charts and Kustomize configurations
helm:
	make -C helm

# Clean up (if necessary)
clean:
	# Add any clean up commands if needed
	@echo "Clean up done."
