## Docker commands

```
docker build . <builds an image based on the local Dockerfile>
```

```
docker run IMAGE <starts a container based on an image>
```

```
docker run -it IMAGE <starts a container and enters the terminal>
```

```
docker run -it --entrypoint=bash python:3.9 <start a python 3.9 container and enters directly the bash. Otherwise, without the --entrypoint, it will start a python script>
```

```
docker ps <shows all active containers> 
```

```
docker ps -a <shows all inactive containers>
```

```
<runs a postgres container instance with environment variables (-e tag) and volumes (-v). As a volume is being used, the state of a postgres database is maintained in the ny_taxi_postgres_data folder, even when the container is recthemereated>


docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

```

```
<runs a pgadmin container>


docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4

```

```
<creates a network>
docker network create pg-network 
```

```
<runs both a postgres and a pgadmin container in the same network>

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13


docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin:/var/lib/pgadmin \
  -p 8080:80 \
  --network=pg-network \
  dpage/pgadmin4

```

```
<runs both a postgres and a pgadmin container in the same network>

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

```
```
<building the ingestion script image based on Dockerfile>

docker build -t ingest:v001 .
```

```
<running the ingestion script>
docker run -it \
    --network=pg-network \
    ingest:v001 \
      --user=root \
      --password=root \
      --host=pg-database \
      --port=5432 \
      --db=ny_taxi \
      --table=yellow_taxi_data \
      --color=yellow \
      --period=2021-01
```

```
<creating containers from a docker compose file>
docker compose up
```

```
<stoping and exiting containers from a docker compose file>
docker compose down
```