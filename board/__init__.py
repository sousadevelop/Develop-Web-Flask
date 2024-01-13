from flask import Flask
from board import pages

# Essa função é a fábrica de aplicativos
def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)