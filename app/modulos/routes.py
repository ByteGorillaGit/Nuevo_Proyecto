from flask import Flask, render_template, request, redirect, url_for
from . import module_begin
from . import module_menu
from . import module_shop
from . import module_warranty
from . import module_pqr
from . import module_privacy
import app

# Crear una instancia de Flask
app = Flask(__name__)

@module_shop.route("/catalogue")
def catalogue():
    return render_template("Shop.html")

@module_shop.route("/register_shop")
def register_shop():
    return render_template("RegisterShop.html")

@module_shop.route("/consult_shop")
def consult_shop():
    return render_template("ConsultShop.html")

@module_warranty.route("/consult_warranty")
def consult_warranty():
    return render_template("ConsultWarranty.html")

@module_warranty.route("/register_warranty")
def register_warranty():
    return render_template("RegisterWarranty.html")

@module_warranty.route("/warranty")
def warranty():
    return render_template("Warranty.html")

@module_begin.route("/principle")
def principle():
    return render_template("Login.html")

@module_begin.route("/register_user")
def register_user():
    return render_template("RegisterUser.html")

@module_begin.route("/forgot_password")
def forgot_password():
    return render_template("ForgotPassword.html")

@module_menu.route("/menu", methods=['GET', 'POST'])
def menu():
    return render_template("Index.html")

@module_menu.route("/contact_menu")
def menu_contact():
    return render_template("ContactMenu.html")

@module_pqr.route("/register_pqr")
def register_pqr():
    return render_template("RegisterPQR.html")

@module_pqr.route("/consult_pqr")
def consult_pqr():
    return render_template("ConsultPQR.html")

@module_privacy.route("/legalcy")
def legalcy():
    return render_template("TermsAndConditions.html")

