# Homelab Cleanup
The scripts in this repository are used to clear out existing Cloudflare DNS records, Cloudflare API Keys, Cloudflare Tunnels, ZeroTier Networks, and Terraform Workspaces to make way for a fresh build process of the [Khuedoan Homelab](https://github.com/khuedoan/homelab).

Since Homelab requires python, I built this to use python scripts.

To get started, clone this repo to your controller which is most likely in Ubuntu or Fedora.

Run the following command from within the repo folder and inside make tools nix environment:

```python cleanup.py```

You will have plenty of opportunity to opt out of a change before committing to it. Make sure to fill in all your Environment Variables as the cleanup.py is built to prevent you from leaving anything out.

You can double check your Environment Variables in the .env file to make sure they are correct.

Disclaimer: This is still a work in progress and has only been tested in my own environment.
Disclaimer2: The reason you run this inside the nix container is to make sure all your variable secrets stay safe in an area that can easily be removed. Gitignore does contain .env to help prevent any security leaks.
