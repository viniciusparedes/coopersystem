THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: build run stop logs beautify test

run:
	docker-compose --env-file ./src/coopersystem/.env up

stop:
	docker-compose down

logs:
	docker-compose logs -f

build:
	docker-compose --env-file ./src/coopersystem/.env up --force-recreate --build

beautify:
	isort */*.py
	flake8 */*.py

test:
	docker-compose --env-file ./src/coopersystem/.env up -d
	docker exec -it coopersystem_web_1 ./manage.py test produtos.tests
