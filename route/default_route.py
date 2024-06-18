from flask import Blueprint, render_template

default_bp = Blueprint('default', __name__)

@default_bp.route('/')
def index():
    """This is default route in case of mismatch above"""
    return render_template('index.html')
