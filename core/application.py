from flask import Flask
from core.endpoints import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
