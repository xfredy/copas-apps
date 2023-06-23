from flask import Blueprint

status_blueprint = Blueprint('status', __name__, url_prefix='/api/status')