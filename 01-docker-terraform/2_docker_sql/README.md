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
<runs a postgres container instance with environment variables (-e tag) and volumes (-v). As a volume is being used, the state of a postgres database is maintained in the ny_taxi_postgres_data folder, even when the container is recreated>


docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

```