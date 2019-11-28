from flask import Blueprint, render_template

nomad = Blueprint('nomad', __name__, template_folder='templates')


@nomad.route("/nomad")
def nomad1():
    return render_template("nomad.html")
