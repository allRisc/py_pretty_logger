IMAGE_NAME ?= "pretty_logger_dev"

VOLUME ?= $(shell pwd):/code

all: run

image: Dockerfile
	docker build -t $(IMAGE_NAME) -f Dockerfile .

test:
	docker run -it -v $(VOLUME) $(IMAGE_NAME) /bin/sh -c 'cd /code; pip install -e .[dev]; tox'

flake8:
	docker run -it -v $(VOLUME) $(IMAGE_NAME) /bin/sh -c 'cd /code; pip install -e .[dev]; flake8 src tests'

mypy:
	docker run -it -v $(VOLUME) $(IMAGE_NAME) /bin/sh -c 'cd /code; pip install -e .[dev]; mypy src'

run:
	docker run -it -v $(VOLUME) $(IMAGE_NAME) bash