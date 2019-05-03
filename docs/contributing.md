# Contributing
Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

### Reporting Bugs
Report bugs in the [issues section](https://github.com/PokeAPI/pokepy/issues).

When reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fixing Bugs
Look through the [issues section](https://github.com/PokeAPI/pokepy/issues) for bugs. Anything tagged with `bug`
is open to whoever wants to implement it.

### Implementing Features
Look through the [issues section](https://github.com/PokeAPI/pokepy/issues) for features. Anything tagged with `feature`
is open to whoever wants to implement it.

When proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

### Writing Documentation
Pokepy could always use more documentation, whether as part of the 
official Pokepy docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submiting Feedback
The best way to send feedback is to file an issue in the [issues section](https://github.com/PokeAPI/pokepy/issues).

Remember that this is a volunteer-driven project, and that contributions
are welcome :)

### Get Started!
Ready to contribute? Here's how to set up `pokepy` for local development.

**1 .** Fork the `pokepy` repo on GitHub.

**2 .** Clone your fork locally. You can use a tool like [Github Desktop](https://desktop.github.com/)
or through the command line with `git`:

```
$ git clone git@github.com:your_name_here/pokepy.git
```

(you can also simply download the project from github as a .zip file)

**3 .** Install your local copy into a virtual environment.
   If you use an IDE, it should have an option to create a new virtual environment.
   Otherwise, and assuming you have `virtualenv` installed, this is how you set up your fork for local development:

```
$ mkdir venv
$ virtualenv venv/pokepy
$ cd venv/pokepy/bin
$ source activate
$ pip install -r requirements.txt -r requirements-dev.txt
```

**4 .** Create a branch for local development (`git`):

```
$ git checkout -b name-of-your-bugfix-or-feature
```
    
Now you can make your changes locally.

**5 .** When you're done making changes, check that your changes pass `pylint` and the `tests`,
including testing other Python versions with `tox`:

```
$ python -m pylint pokepy tests setup.py
$ tox
```

`pylint` and `tox` should already be installed in your virtualenv if you followed step 3 correctly.

**6 .** Commit your changes and push your branch to GitHub (`git`):

```
$ git add .
$ git commit -m "Your detailed description of your changes"
$ git push origin name-of-your-bugfix-or-feature
```

**7 .** Submit a pull request through the GitHub website.

### Pull Request Guidelines
Before submiting a pull request, check that it meets these guidelines:

**1 .** The pull request includes tests (if relevant).

**2 .** If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the
   feature to the list in [README](https://github.com/PokeAPI/pokepy/blob/master/README.md).
   
**3 .** The pull request should work for Python 2.7, 3.4, 3.5, 3.6, and 3.7.

### Tips
To run a subset of tests:

```
$ python -m unittest tests.test_pokepy
```
