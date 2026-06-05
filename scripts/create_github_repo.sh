#!/usr/bin/env bash
# Helper script to create a GitHub repo and push the current code.
# Requires: GitHub CLI (`gh`) authenticated and git configured.

set -euo pipefail

REPO_NAME=${1:-crm}
REMOTE=${2:-origin}

echo "Creating GitHub repo: $REPO_NAME"
gh repo create "$REPO_NAME" --public --source=. --remote-name "$REMOTE" --push

echo "Repository created and code pushed to GitHub as $REPO_NAME"
