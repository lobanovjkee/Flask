from flask import Flask

from blog.articles.views import article
from blog.users.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(article)
    app.register_blueprint(user)
