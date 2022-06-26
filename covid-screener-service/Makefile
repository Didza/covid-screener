build:
	docker-compose build

up:
	docker-compose up -d covid-screener-api

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest covid-screener-api /tests/unit /tests/integration

down:
	docker-compose down

all: down build up test