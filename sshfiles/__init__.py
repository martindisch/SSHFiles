from flask import Flask
from sshfiles.overview.views import overview_blueprint

app = Flask(__name__)

app.register_blueprint(overview_blueprint)
