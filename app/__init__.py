from flask import Flask, render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.modulos import module_warranty
from app.modulos import module_menu
from app.modulos import module_begin
from app.modulos import module_shop
from app.modulos import module_pqr
from app.modulos import module_privacy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app=app , db=db)

from .models import Rol, Usuario, Contrato, Pqrs, Garantias


app.register_blueprint(module_warranty)
app.register_blueprint(module_menu)
app.register_blueprint(module_begin)
app.register_blueprint(module_shop)
app.register_blueprint(module_pqr)
app.register_blueprint(module_privacy)



if __name__ == '__main__':
    app.run(port=3000, debug=True)
