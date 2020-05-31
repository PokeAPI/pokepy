@echo off

if "%1" == "" goto help
goto %~1

:help
echo.
echo clean            removes build and python file artifacts
echo clean-build      removes build artifacts
echo clean-pyc        removes python file artifacts
echo clean-tests      removes test and coverage files
echo clean-docs       removes built docs files
echo lint             checks style with pylint
echo test             runs tests quickly with the default python version
echo test-all         runs tests on every python version with tox
echo coverage         checks code coverage quickly with the default python version
echo docs-build       builds MkDocs HTML documentation
echo docs-test        live tests the current documentation
echo docs-release     pushes built docs to gh-pages branch of github repo (git should exist on PATH)
echo sdist            packages source distribution package
echo sdist-test       looks for errors on the source distribution package
echo release          packages and uploads a release
goto:eof

:clean
call:clean-build
call:clean-pyc
call:clean-tests
call:clean-docs
goto:eof

:clean-build
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q pokepy.egg-info
goto:eof

:clean-pyc
del /s *.pyc *.pyo *~
goto:eof

:clean-tests
rmdir /s /q .tox
rmdir /s /q html_coverage
goto:eof

:clean-docs
rmdir /s /q site
goto:eof

:lint
python -m pylint --ignore=pokepy\fcache pokepy tests setup.py
goto:eof

:test
python -m unittest tests.test_pokepy
goto:eof

:test-all
tox
goto:eof

:coverage
coverage run --source pokepy --omit="pokepy\fcache\*" -m unittest tests.test_pokepy
coverage report -m
coverage html -d html_coverage
start "" html_coverage/index.html
goto:eof

:docs-build
mkdocs build
start "" site/index.html
goto:eof

:docs-test
mkdocs serve
goto:eof

:docs-release
mkdocs gh-deploy --verbose
goto:eof

:sdist
call:clean-build
call:clean-pyc
python setup.py sdist bdist_wheel
goto:eof

:sdist-test
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
goto:eof

:release
call:sdist
twine upload dist/*
goto:eof
