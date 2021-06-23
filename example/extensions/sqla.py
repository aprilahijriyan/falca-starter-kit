from falcon_sqla import Manager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
manager = Manager(engine)

def setup(app):
    app.add_middleware(manager.middleware)
