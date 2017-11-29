from flask import Blueprint


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def hello():
    return 'Hello World! This is Reddit clone'
