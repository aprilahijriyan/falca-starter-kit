from mongoengine import connect

def setup(app):
    config = app.settings.get("MONGOENGINE", {})
    connect(**config)
