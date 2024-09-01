git pull

docker compose -f compose-production.yaml --env-file="vars/.env" build

docker compose -f compose-production.yaml --env-file="vars/.env" up -d