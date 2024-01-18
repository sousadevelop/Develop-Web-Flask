import os
from dotenv import load_dotenv
from flask import Flask
from board import pages, posts

from board import (
    database,
    errors,
    pages,
    posts,
)

load_dotenv()

# Essa função é a fábrica de aplicativos
def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.logger.setLevel("INFO")

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)
    app.logger.debug(f"Current Environment: {os.getenv('ENVIRONMENT')}")  # os.getenv -> usado para var em que não comecem com FLASK
    app.logger.debug(f"Using Database: {app.config.get('DATABASE')}")     # app.config.get -> usado para var que começam com FLASK
    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)