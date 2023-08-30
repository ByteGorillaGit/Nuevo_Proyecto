from . import modulo_inicio
from flask import render_template

@modulo_inicio.route("/login")
def listar():
    return render_template("login.html")

@modulo_inicio.route("/registro")
def registro():
    return render_template("user.html")

@modulo_inicio.route("/contraseña")
def contraseña():
    return render_template("Form.html")