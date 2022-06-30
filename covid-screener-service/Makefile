build:
	docker-compose build

up:
	docker-compose up -d covid-screener-api

migrations: up
	docker-compose run --rm --entrypoint=alembic covid-screener-api upgrade head

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest covid-screener-api /tests/unit /tests/integration

down:
	docker-compose down

all: down build up test migrations