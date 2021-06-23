{% set app_type = 'WSGI' if cookiecutter.application_type == 'wsgi' else 'ASGI' -%}
from falca.app import {{ app_type }}
{% if cookiecutter.database_engine == 'sqlalchemy' -%}
from extensions import sqla
{% elif cookiecutter.database_engine == 'mongoengine' -%}
from extensions import mongo
{% endif %}

app = {{app_type}}(__name__)
{% if cookiecutter.database_engine == 'sqlalchemy' -%}
sqla.setup(app)
{% elif cookiecutter.database_engine == 'mongoengine' -%}
mongo.setup(app)
{% endif %}
