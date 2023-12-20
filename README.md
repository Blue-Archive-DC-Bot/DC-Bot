# BA Bot
IDK man.

### Developer's Guide

Firstly, make sure you have an installation of Python 3.10 and [install pipenv](https://pipenv.pypa.io/en/latest/installation/).
To do so, you can use the command below:
```
pip install pipenv --user
```

Then, run `pipenv install` to ensure all dependencies are installed. For development, it's recommended to run `pipenv shell` to ensure a sanitized Python environment. Then, run `pre-commit install` to install all the pre-commit hooks, this will add some linting and code checking behavior prior to any commit.

If you want to manually run the hooks, you can type `pre-commit run --all-files`
