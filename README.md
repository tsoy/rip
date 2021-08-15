# rip
docker image build --file Dockerfile.dev -t rip:latest .
docker container run -v $PWD/rip:/app --rm -it -p 8000:8000 --name rip rip:latest

docker image build --file Dockerfile.prod -t rip-prod:latest .

## Running for development

1. create `.env` file based on `.env-example`
2. Run `docker-compose up`

## Optional steps
1. Run `chmod g+s alembic` to be able to edit migration files that are created inside container

### Install new package

```bash
docker container exec -it rip bash
cd /opt/pysetup/
poetry add package-name
```

### Working with migrations

Generate new migration based on SQLAlchemy models
```
docker container exec -it rip bash
alembic revision --autogenerate -m "Add users table"
```

Execute migrations
```
docker container exec -it rip bash
alembic upgrade head
```