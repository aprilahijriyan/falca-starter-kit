from falca.app import WSGI
from extensions import sqla


app = WSGI(__name__)
sqla.setup(app)

