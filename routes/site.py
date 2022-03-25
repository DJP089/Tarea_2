from flask import Blueprint, render_template
from models.user import messages
from forms.registerform import userform
from database.db import db
site = Blueprint("site", __name__, url_prefix="/")

@site.route("/")
def home():
    return render_template("home.html")

@site.route("/estadisticas.html")
def Curiosidades():
    return render_template("estadisticas.html")

@site.route("/contacto.html", methods=["GET", "POST"])
def mensajenuevo():
    form = userform()
    if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            message = form.message.data
            newmessage = messages(firstname, lastname, email, message)
            db.session.add(newmessage)
            db.session.commit()
    return render_template("contacto.html", form=form)


@site.route("/mensaje.html")
def messagess():
    messagesList = messages.query.all()
    return render_template("mensaje.html", messagesList=messagesList)

