import os
from flask import Flask
from config import Config


def create_app():
    if not os.path.exists('upload'):
        os.mkdir('upload')

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
