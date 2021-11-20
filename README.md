Princesse Margot
===

## Installation

Development is done in a virtual environment.

```
$ pip install Flask flask_sqlalchemy mysqlclient Flask-Fixtures flask_bcrypt flask_restful flask-jwt-extended
```

Copy `margot/.env.template` to `margot/.env.dev` and edit it to hold your own private token

## Run

Run task parametered for VSCode

```
$ cd margot
$ ENV_FILE_NAME=./.env.dev flask run
```


## Test & Fixtures

Integrated in VSCode. See `app_test.py`.