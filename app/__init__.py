import logging
from .api.status import status_blueprint
from .api.profile import profile_blueprint
from flask import Flask

def configure_logging(app: Flask):
    if not app.debug:
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

app = Flask(__name__)

configure_logging(app)

@app.after_request
def add_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response

app.register_blueprint(status_blueprint)
app.register_blueprint(profile_blueprint)