import os
import json
import fcntl
from flask import Blueprint, render_template, request
from sshfiles.util import indexing

overview_blueprint = Blueprint('overview', __name__, static_folder='static',
                               static_url_path='/overview/static',
                               template_folder='templates')

@overview_blueprint.route('/', methods=['GET'])
def overview_get():
    """Show the overview page."""
    # kvargs for render_template
    args = {}
    # Attempt reading settings
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            args['conf'] = json.load(f)
    # Attempt reading file index
    if os.path.isfile('index.json'):
        with open('index.json', 'r') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            args['files'] = json.load(f)
    return render_template('overview.html', **args)

@overview_blueprint.route('/', methods=['POST'])
def overview_post():
    """Update the file index."""
    # Get settings
    conf = {}
    conf['path'] = request.form['path']
    conf['username'] = request.form['username']
    conf['ip'] = request.form['ip']
    # Save the potentially updated configuration
    with open('config.json', 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        json.dump(conf, f)
    # Get videos
    videos = indexing.get_videos(conf['path'])
    # Dump video index for later use
    with open('index.json', 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        json.dump(videos, f)
    return render_template('overview.html', conf=conf, files=videos)
