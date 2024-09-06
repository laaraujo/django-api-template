export PYTHONDONTWRITEBYTECODE=1

container_name = 'app-api'
pytest_workers = 3

help:
	@echo
	@echo build .................... : Build local containers
	@echo run ...................... : Run local containers
	@echo stop ..................... : Stop local containers
	@echo down ..................... : Stop and delete local container
	@echo makemigrations ........... : Django makemigrations command
	@echo migrate .................. : Django migrate command
	@echo createsuperuser .......... : Django createsuperuser command
	@echo shell .................... : Django shell command
	@echo sh ....................... : SSH into local API container
	@echo linter ................... : Run Ruff linter against all files in this repo
	@echo


build: down
	docker compose build --no-cache

run:
	docker compose up

stop:
	docker compose stop

down: stop
	docker compose down --remove-orphans --rmi all

makemigrations:
	docker compose run app python manage.py makemigrations

migrate:
	docker compose run app python manage.py migrate

createsuperuser:
	docker compose run app python manage.py createsuperuser --no-input

shell:
	docker compose run app python manage.py shell -i ipython

sh:
	docker exec -it $(container_name) /bin/sh

linter:
	pre-commit run --all-files

test:
	pytest -n $(pytest_workers) --cov=src/ --import-mode=importlib
