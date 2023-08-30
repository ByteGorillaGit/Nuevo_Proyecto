from . import modulo_garantias
from flask import render_template

@modulo_garantias.route("/listar")
def listar():
    return render_template("listar.html")
    garantia = app.models()
    

@modulo_garantias.route("/crear")
def crear():
    return render_template("crear.html")

@modulo_garantias.route("/inicio")
def inicio():
    return render_template("warranty.html")