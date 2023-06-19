.PHONY: style check-style start install develop test load-test
style:
	# apply opinionated styles
	@black api
	@isort api

	# tests are production code too!
	@black tests
	@isort tests

check-style:
	@black api --check
	@flake8 api --count --show-source --statistics --ignore=E203,W503

start:
	@bash sudo docker-compose up -d --build

install:
	@pip install -r requirements.txt

lint:
	@find . -name '*.py' -exec pylint {} \;

test:
	@pytest -v tests

