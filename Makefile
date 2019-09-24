test:
	PYTHONPATH=src pytest

install:
	pip install -r requirements.txt

lint:
	python -m pylint src
