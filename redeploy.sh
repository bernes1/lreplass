#!/bin/bash

# Function to log messages
log() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Pull the latest changes from the repository
log "Pulling latest changes from git..."
if git pull; then
  log "Successfully pulled latest changes."
else
  log "Failed to pull latest changes."
  exit 1
fi

# Build the Docker images
log "Building Docker images..."
if docker compose -f compose-production.yaml --env-file="vars/.env" build; then
  log "Successfully built Docker images."
else
  log "Failed to build Docker images."
  exit 1
fi

# Bring up the Docker containers
log "Starting Docker containers..."
if docker compose -f compose-production.yaml --env-file="vars/.env" up -d; then
  log "Successfully started Docker containers."
else
  log "Failed to start Docker containers."
  exit 1
fi

log "Redeployment completed successfully."