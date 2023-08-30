from . import modulo_privacidad
from flask import render_template

@modulo_privacidad.route("/legal")
def listar():
    return render_template("termsAndConditions.html")

