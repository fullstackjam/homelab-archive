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
            bash
            bmake
            diffutils
            docker
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
            zsh
            oh-my-zsh
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
              jsonschema
              jmespath
              pexpect
              rich
            ]))
          ];

          shellHook = ''
            export SHELL=$(which zsh)
            if [ -t 1 ]; then
              exec zsh
            fi
            ZSH=$HOME/.oh-my-zsh
            if [ -d "$ZSH" ]; then
              export ZSH="$ZSH"
              source $ZSH/oh-my-zsh.sh
            fi
          '';
        };
      }
    );
}
