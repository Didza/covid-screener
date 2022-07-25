build:
	docker-compose build

dev-up:
	docker-compose up covid-screener-api

prod-up:
	docker-compose up -d covid-screener-api

migrations: prod-up
	docker-compose run --rm --entrypoint=alembic covid-screener-api upgrade head

test: prod-up
	docker-compose run --rm --no-deps --entrypoint=pytest covid-screener-api /tests/unit /tests/integration

down:
	docker-compose down

stop:
	docker-compose stop

prod: stop build prod-up test migrations

dev: down build dev-up test migrations