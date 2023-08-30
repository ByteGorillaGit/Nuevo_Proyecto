from . import modulo_menu
from flask import render_template

@modulo_menu.route("/menu")
def listar():
    return render_template("index.html")
