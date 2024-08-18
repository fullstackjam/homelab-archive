{
  description = "Homelab";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
      in
      with pkgs;
      {
        devShells.default = mkShell {
          packages = [
            ansible
            ansible-lint
            bmake
            diffutils
            docker
            docker-compose_1 # TODO upgrade to version 2
            dyff
            git
            go
            gotestsum
            helmfile
            iproute2
            jq
            k9s
            kube3d
            kubectl
            kubernetes-helm
            kustomize
            libisoburn
            neovim
            openssh
            p7zip
            pre-commit
            shellcheck
            terraform
            yamllint
            yq
            (python3.withPackages (p: with p; [
              jinja2
              kubernetes
              ansible
              mkdocs-material
              netaddr
              pip
              jsonschema
              jmespath
              pexpect
              rich
              requests
              python-dotenv
            ]))
          ];
        };
      }
    );
}
