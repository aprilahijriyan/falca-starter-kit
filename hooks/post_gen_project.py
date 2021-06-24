import pathlib

cwd = pathlib.Path.cwd()
{% if cookiecutter.database_engine == 'sqlalchemy' -%}
(cwd / "extensions/mongo.py").unlink()
{% elif cookiecutter.database_engine == 'mongoengine' -%}
(cwd / "extensions/sqla.py").unlink()
{% endif %}

{% if cookiecutter.pre_commit|lower != 'y' -%}
(cwd / ".pre-commit-config.yml").unlink()
{% endif %}
