from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config["SECRET_KEY"] = "y958G4V5W!Y&E"

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route("/user/<name>")
def hello(name):
    return render_template("user.html", name=name)


# Handle 404 errors (request for unknown route)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Handle 500 errors (unhandled exception in request)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
