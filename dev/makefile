IMAGE_NAME ?= "pretty_logger_dev"

VOLUME ?= $(shell pwd)/..:/code

all: image

run: image
	docker run -t -v $(VOLUME) -i $(IMAGE_NAME) bash

build: image
	docker run -t -v $(VOLUME) -i $(IMAGE_NAME) python -m build

upload: build
	docker run -t -v $(VOLUME) -i $(IMAGE_NAME) python -m twine upload --repository testpypi dist/*

release: build
	docker run -t -v $(VOLUME) -i $(IMAGE_NAME) python -m twine upload dist/*

image: Dockerfile ../src/pretty_logger/*.py ../MANIFEST.in ../setup.py ../pyproject.toml
	cp ~/.pypirc ..
	cd .. && docker build -t $(IMAGE_NAME) -f dev/Dockerfile .
	rm ../.pypirc
	touch image