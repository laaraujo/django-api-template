# Django API Template

Template repo to kickstart API projects

## Features

- [Makefile](./Makefile) with common shorcuts for local development commands
- Authentication ([Djoser](https://djoser.readthedocs.io/))
  - Registration
  - Login
  - Email validation
  - Password reset (w/ email)
  - Password reset confirmation
- Static file serving ([Whitenoise](https://whitenoise.readthedocs.io/))
- [Dockerfile](./Dockerfile)
- [Docker compose for local development](./compose.yml)
- [PostgreSQL](https://www.postgresql.org/)
- Auto Swagger Docs ([DRF Spectacular](https://drf-spectacular.readthedocs.io/))
- [Custom user model](./src/users/models.py) (email, password and name)
- Email via SMTP
- Pre-commit hooks ([Ruff](https://docs.astral.sh/ruff/) and [OTB Pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks))
- Automated testing ([Pytest](https://docs.pytest.org/))
  - [Modal bakery](https://model-bakery.readthedocs.io/)
  - Test run parallelization with (pytest-xdist)[https://pytest-xdist.readthedocs.io/]
  - [Faker](https://faker.readthedocs.io/)
  - [Coverage](https://pytest-cov.readthedocs.io/)

## Make commands

```
build .................... : Build local containers
run ...................... : Run local containers
stop ..................... : Stop local containers
down ..................... : Stop and delete local container
makemigrations ........... : Django makemigrations command
migrate .................. : Django migrate command
createsuperuser .......... : Django createsuperuser command
shell .................... : Django shell command
sh ....................... : SSH into local API container
linter ................... : Run Ruff linter against all files in this repo
```
