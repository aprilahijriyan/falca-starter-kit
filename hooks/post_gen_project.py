import pathlib

{% if cookiecutter.database_engine == 'sqlalchemy' -%}
(pathlib.Path.cwd() / "extensions/mongo.py").unlink()
{% elif cookiecutter.database_engine == 'mongoengine' -%}
(pathlib.Path.cwd() / "extensions/sqla.py").unlink()
{% endif %}

{% if cookiecutter.pre_commit|lower != 'y' -%}
(pathlib.Path.cwd() / ".pre-commit-config.yml").unlink()
{% endif %}
