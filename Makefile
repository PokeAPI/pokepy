.PHONY: clean-pyc clean-build docs

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with pylint"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

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

docs:
	rm -f docs/pokepy.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pokepy
	make -C docs clean
	make -C docs html
	open docs/_build/html/index.html

release: clean sdist
	twine upload dist/*

sdist: clean
	python setup.py sdist bdist_wheel
	ls -l dist
