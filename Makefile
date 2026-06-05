PYTHON=python3
VENV=venv

.PHONY: help setup migrate run shell docker-up start-dev build-prod deploy

help:
	@echo "Available targets:"
	@echo "  setup     - create venv and install requirements"
	@echo "  migrate   - run Django migrations"
	@echo "  run       - run development server"
	@echo "  shell     - run Django shell (inside venv)"
	@echo "  docker-up - start services with docker-compose"
	@echo "  start-dev - start development services (docker-compose up)"
	@echo "  build-prod - build production images (docker build via compose)"
	@echo "  deploy    - placeholder deploy target"

setup:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

migrate:
	. $(VENV)/bin/activate && python manage.py migrate

run:
	. $(VENV)/bin/activate && python manage.py runserver

shell:
	. $(VENV)/bin/activate && python manage.py shell

docker-up:
	docker compose up --build -d

start-dev:
	docker compose up --build

build-prod:
	docker compose build --parallel

deploy:
	@echo "Deploy target placeholder — implement your deployment steps here"
	@exit 0
