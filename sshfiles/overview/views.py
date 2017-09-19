import os
import json
import fcntl
from flask import Blueprint, render_template, request

overview_blueprint = Blueprint('overview', __name__, static_folder='static',
                               static_url_path='/overview/static',
                               template_folder='templates')

@overview_blueprint.route('/', methods=['GET'])
def overview_get():
    """Show the overview page."""
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            kv = json.load(f)
            return render_template('overview.html', path=kv['path'])
    return render_template('overview.html')

@overview_blueprint.route('/', methods=['POST'])
def overview_post():
    """Update the file index."""
    path = request.form['path']
    with open('config.json', 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        json.dump({'path': path}, f)
    return render_template('overview.html', path=path)
