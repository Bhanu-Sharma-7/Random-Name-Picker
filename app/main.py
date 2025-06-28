from flask import Blueprint, render_template, jsonify
from .names import get_random_name

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/random')
def random_name():
    return jsonify({'name': get_random_name()})