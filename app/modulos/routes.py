from . import module_shop
from . import module_warranty
from . import module_begin
from . import module_menu
from . import module_pqr
from . import module_privacy
from flask import render_template

@module_shop.route("/catalogue")
def catalogue():
    return render_template("Shop.html")

@module_shop.route("/register")
def register():
    return render_template("RegisterShop.html")

@module_shop.route("/consult")
def consult():
    return render_template("ConsultShop.html")

@module_warranty.route("/consult_warranty")
def consult():
    return render_template("ConsultWarranty.html")
    garantia = app.models()
    
@module_warranty.route("/register_warranty")
def register():
    return render_template("RegisterWarranty.html")

@module_warranty.route("/warranty")
def warranty():
    return render_template("Warranty.html")

@module_begin.route("/principle")
def principle():
    return render_template("Login.html")

@module_begin.route("/register_user")
def register():
    return render_template("RegisterUser.html")

@module_begin.route("/forgot_password")
def password():
    return render_template("ForgotPassword.html")

@module_menu.route("/menu")
def menu():
    return render_template("Index.html")

@module_pqr.route("/register_pqr")
def pqr():
    return render_template("RegisterPQRS.html")

@module_pqr.route("/consult_pqr")
def consult():
    return render_template("ConsultPQR.html")

@module_privacy.route("/legalcy")
def consult():
    return render_template("TermsAndConditions.html")
