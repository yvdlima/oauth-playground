# Python implementation

- [Python implementation](#python-implementation)
  - [Install Python](#install-python)
  - [Install dependencies](#install-dependencies)
  - [Preparing you environment](#preparing-you-environment)
  - [Run the app](#run-the-app)

## Install Python

You should have Python 3.9.4+ installed.

I won't bother explaining deeply how to install python, but I recommend using [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

```bash
# In this app root: oauth_playground/python/
pyenv install 3.9.4
# oauth-playground-3.9.4 is the virtualenv name defined in the .python-version file
pyenv virtualenv 3.9.4 oauth-playground-3.9.4
pyenv activate oauth-playground-3.9.4
```

_You don't have to use `activate` if the you added `pyenv virtualenv-init` to your shell_

## Install dependencies

Simply run `pip install .` to have the app installed! If you wish to develop use the editable flag and install the test additional like this:

```bash
pip install -e ".[test]"
```

The `-e` flag allows python to detect file changes without having to run a new install every time.

## Preparing you environment

To use OAuth you will need to configure a few things in the app first. Create a file called `.env` in the app root folder, in there you can find a [.env.example](./.env.example) file that you can use as... example...

You can find you application id and secret in your application `settings` page.

## Run the app

After you add all variables to your `.env` simply execute:

```bash
python -m oauth_playground
```

The application should be running in your localhost:8080
