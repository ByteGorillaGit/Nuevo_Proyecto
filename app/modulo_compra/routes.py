from . import modulo_compra
from flask import render_template

@modulo_compra.route("/catalogo")
def listar():
    return render_template("shop.html")

@modulo_compra.route("/registrar")
def crear():
    return render_template("registrar_venta.html")

@modulo_compra.route("/listar")
def inicio():
    return render_template("crud_venta.html")