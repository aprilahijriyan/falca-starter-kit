from falca.app import WSGI
from falca.responses import HTMLResponse
from extensions import sqla


app = WSGI(__name__)
sqla.setup(app)

@app.route("/")
def index():
    return HTMLResponse("index.html")
