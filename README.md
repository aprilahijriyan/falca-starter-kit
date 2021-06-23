# falca-starter-kit

Falca Starter Kit

## Usage

Install `cookiecutter`:

```
pip install cookiecutter
```

Clone template:

```
cookiecutter https://github.com/aprilahijriyan/falca-starter-kit
```

## Options

* `project_name` - Project name
* `project_slug` - Your project directory name
* `project_description` - Description of your project
* `application_type` - Your application type (WSGI or ASGI). By default is `WSGI`.
* `database_engine` - ORM / ODM to use (sqlalchemy or mongoengine). By default is `sqlalchemy`.
* `pre_commit` - Added pre-commit hook
