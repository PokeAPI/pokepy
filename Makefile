.PHONY: help clean clean-build clean-pyc lint test test-all coverage docs-build docs-test docs-release sdist sdist-test release

help:
	@echo "clean          removes build and python file artifacts"
	@echo "clean-build    removes build artifacts"
	@echo "clean-pyc      removes python file artifacts"
	@echo "lint           checks style with pylint"
	@echo "test           runs tests quickly with the default python version"
	@echo "test-all       runs tests on every python version with tox"
	@echo "coverage       checks code coverage quickly with the default python version"
	@echo "docs-build     builds MkDocs HTML documentation"
	@echo "docs-test      live tests the current documentation"
	@echo "docs-release   pushes built docs to gh-pages branch of github repo (git should exist on PATH)"
	@echo "sdist          packages source distribution package"
	@echo "sdist-test     looks for errors on the source distribution package"
	@echo "release        packages and uploads a release"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	pylint pokepy tests setup.py

test:
	python -m unittest tests.test_pokepy

test-all:
	tox

coverage:
	coverage run --source pokepy -m unittest tests.test_pokepy
	coverage report -m
	coverage html
	open htmlcov/index.html

docs-build:
	mkdocs build
	open site/index.html

docs-test:
	mkdocs serve

docs-release:
	mkdocs gh-deploy --verbose

sdist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

sdist-test:
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: clean sdist
	twine upload dist/*
