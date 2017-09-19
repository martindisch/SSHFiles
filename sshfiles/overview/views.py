from flask import Blueprint, render_template, request

overview_blueprint = Blueprint('overview', __name__, static_folder='static',
                               static_url_path='/overview/static',
                               template_folder='templates')

@overview_blueprint.route('/', methods=['GET'])
def overview_get():
    return render_template('overview.html')
