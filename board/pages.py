from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

# Aqui ficam os blueprints, que são os módulos que contém visualizações de cada página.
@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")