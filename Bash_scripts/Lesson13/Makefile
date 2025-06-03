# Declare phony targets that don't produce files
.PHONY: stop run pull restart logs ps build down

# Define Docker Compose command (can be modified if needed, e.g., with profiles or files)
DOCKER_COMPOSE = docker compose

# Start containers in detached mode
run:
	$(DOCKER_COMPOSE) up -d

# Stop containers
stop:
	$(DOCKER_COMPOSE) stop

# Pull latest images for services
pull:
	$(DOCKER_COMPOSE) pull

# Restart containers
restart:
	$(DOCKER_COMPOSE) restart

# View container logs
logs:
	$(DOCKER_COMPOSE) logs

# View running containers
ps:
	$(DOCKER_COMPOSE) ps

# Bring down the stack and remove containers, networks, volumes (optional)
down:
	$(DOCKER_COMPOSE) down

# Rebuild the Docker images
build:
	$(DOCKER_COMPOSE) build
