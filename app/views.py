from flask import Blueprint


views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def home_page():
    return '<title>Reddit</title>'
