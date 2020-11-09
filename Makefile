include ./Makefile.constants

# ENV initialization, switch to just virtualenv in the future
init:
	pipenv install --skip-lock

activate:
	pipenv shell

data:
	git submodule init
	git submodule update


# Run tests
test:
	pipenv run python pytest -svv


test.ptw:
	pipenv run ptw -- --testmon


# Docker resource initialization
docker.precache:
	pipenv run python scripts/precache_docker_requirements.py -d
