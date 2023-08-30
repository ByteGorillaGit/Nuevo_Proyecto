from . import modulo_pqr
from flask import render_template

@modulo_pqr.route("/menu")
def listar():
    return render_template("PQRS.html")

@modulo_pqr.route("/act")
def act():
    return render_template("actualizaryeliminar.html")
