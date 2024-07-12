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
