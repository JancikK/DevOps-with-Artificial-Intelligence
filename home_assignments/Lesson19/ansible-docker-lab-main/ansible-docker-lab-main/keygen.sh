#!/bin/bash

# Generate an SSH keypair using ed25519 format non-interactively
ssh-keygen -t ed25519 -f id_ed25519 -N "" -q

echo "SSH keypair generated. Public key saved as id_ed25519.pub in the current directory."
