from flask import Blueprint, jsonify, render_template, request

from .engine import engine

search_view = Blueprint('search_view', __name__)

def decode_query(query):
    decoded = {}
    for hint in query.split(','):
        splitted = hint.split(':')
        if len(splitted) == 2:
            key, value = splitted
            decoded[key] = value
    return decoded

@search_view.route('/')
def index():
    query = decode_query(request.args.get('query', ''))
    libs = engine.find(query)
    return render_template('index.html', libs=libs)