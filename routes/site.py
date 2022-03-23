from flask import Blueprint, render_template

site = Blueprint("site", __name__, url_prefix="/")

@site.route("/")
def home():
    return render_template("home.html")

@site.route("/estadisticas.html")
def Curiosidades():
    return render_template("estadisticas.html")

@site.route("/contacto.html")
def contacto():
    
    return render_template("contacto.htmL")

        