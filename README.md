# Walmart challenge - API backend

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

Backend connection for a demo [Lider](https://www.lider.cl/supermercado/) web
app built with [Docker](https://www.docker.com/why-docker),
[FastAPI](https://fastapi.tiangolo.com/) and [mongoDB](https://www.mongodb.com/es)

Here you will find a really nice [Web App](https://github.com/Esequiel378/walmart-challenge-frontend)
to interact with

## Deployment

First you need to get the source code

```shell
git clone https://github.com/Esequiel378/walmart-challenge-backend.git
```

Since the project use docker-compose, you can deploy locally by running

```shell
# build api and database images
docker-compose -f local.yml build
```

```shell
# create api and database containers
docker-compose -f local.yml up
```

Now you can visit http://localhost:5000/docs

## Testing

You can find more about testing with FastAPI [here](https://fastapi.tiangolo.com/tutorial/testing/)

```shell
make test
```

Run coverage

```shell
make coverage
```
