# Ansible Docker Lab Environment

This project provides a multi-container Docker environment for testing and learning Ansible with different Linux distributions.

## Available Containers

The lab environment includes the following containers:

- Ubuntu (SSH port: 2222)
- Alpine Linux (SSH port: 2223)
- Red Hat (SSH port: 2224)
- Debian (SSH port: 2225)
- Arch Linux (SSH port: 2226)

## Prerequisites

- Docker
- Docker Compose
- SSH client

## Getting Started

1. Start the containers:
```bash
chmod +x keygen.sh
./keygen.sh
docker-compose up -d
```

2. Connect to containers via SSH:

```bash
# Ubuntu container
ssh -p 2222 ansible@localhost

# Alpine container
ssh -p 2223 ansible@localhost

# Red Hat container
ssh -p 2224 ansible@localhost

# Debian container
ssh -p 2225 ansible@localhost

# Arch Linux container
ssh -p 2226 ansible@localhost
```

## Container Details

Each container:
- Runs an SSH server on port 22 (mapped to different host ports)
- Is configured to restart automatically unless stopped manually
- Is built from a custom Dockerfile specific to each distribution

## Directory Structure

```
.
├── alpine/
├── archlinux/
├── debian/
├── redhat/
├── ubuntu/
└── docker-compose.yaml
```

## Stopping the Environment

To stop all containers:

```bash
docker-compose down
```