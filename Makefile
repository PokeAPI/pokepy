.PHONY: help clean clean-build clean-pyc clean-tests clean-docs lint test test-all coverage docs-build docs-test docs-release sdist sdist-test release

help:
	@echo "clean            removes build and python file artifacts"
	@echo "clean-build      removes build artifacts"
	@echo "clean-pyc        removes python file artifacts"
	@echo "clean-tests      removes test and coverage files"
	@echo "clean-docs       removes built docs files"
	@echo "lint             checks style with pylint"
	@echo "test             runs tests quickly with the default python version"
	@echo "test-all         runs tests on every python version with tox"
	@echo "coverage         checks code coverage quickly with the default python version"
	@echo "docs-build       builds MkDocs HTML documentation"
	@echo "docs-test        live tests the current documentation"
	@echo "docs-release     pushes built docs to gh-pages branch of github repo (git should exist on PATH)"
	@echo "sdist            packages source distribution package"
	@echo "sdist-test       looks for errors on the source distribution package"
	@echo "release          packages and uploads a release"

clean: clean-build clean-pyc clean-tests clean-docs

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf pokepy.egg-info/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-tests:
	rm -rf .tox/
	rm -rf  html_coverage/

clean-docs:
	rm -rf site/

lint:
	python -m pylint --ignore=pokepy/fcache pokepy tests setup.py

test:
	python -m unittest tests.test_pokepy

test-all:
	tox

coverage:
	coverage run --source pokepy --omit="pokepy/fcache/*" -m unittest tests.test_pokepy
	coverage report -m
	coverage html -d html_coverage
	open htmlcov/index.html

docs-build:
	mkdocs build
	open site/index.html

docs-test:
	mkdocs serve

docs-release:
	mkdocs gh-deploy --verbose

sdist: clean-build clean-pyc
	python setup.py sdist bdist_wheel

sdist-test:
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: sdist
	twine upload dist/*
