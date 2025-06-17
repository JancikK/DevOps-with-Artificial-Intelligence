#!/bin/bash

echo "Running Docker container test..."

# Check SSH service exists
if ! command -v sshd >/dev/null; then
  echo "sshd is not installed"
  exit 1
fi

# Optionally check user exists
if ! id ansible &>/dev/null; then
  echo "user 'ansible' does not exist"
  exit 1
fi

echo "All checks passed"
exit 0
