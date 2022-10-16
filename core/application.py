from flask import Flask
from core.endpoints import blueprint
from healthcheck import HealthCheck


health = HealthCheck()

app = Flask(__name__)
app.register_blueprint(blueprint)
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
