# variables
IMAGE_NAME=wikiwikiwrap
CONTAINER_NAME=wikiwikiwrap
EXPOSED_PORT=5100

# build docker image
build:
	docker build -t $(IMAGE_NAME) .

# run tests
test:
	FLASK_ENV=testing coverage run -m pytest

# run flask development server
dev:
	FLASK_ENV=development flask --app wikiwikiwrap run --debug
# run docker container
run:
	@trap 'make clean' ERR; \
	docker run -p $(EXPOSED_PORT):5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# stop and remove docker container
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# run tests and display coverage report
coverage-run:
	FLASK_ENV=testing coverage run -m pytest; \
	coverage report -m

# display coverage report
coverage:
	coverage report -m

setup:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install poetry && \
	poetry install

format:
	ruff format .

lint:
	ruff check .
