from flask import Flask, render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.modulo_garantias import modulo_garantias
from app.modulo_menu import modulo_menu
from app.modulo_inicio import modulo_inicio
from app.modulo_compra import modulo_compra
from app.modulo_pqr import modulo_pqr
from app.modulo_privacidad import modulo_privacidad


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app=app , db=db)
from .models import Rol


app.register_blueprint(modulo_garantias)
app.register_blueprint(modulo_menu)
app.register_blueprint(modulo_inicio)
app.register_blueprint(modulo_compra)
app.register_blueprint(modulo_pqr)
app.register_blueprint(modulo_privacidad)



if __name__ == '__main__':
    app.run(port=3000, debug=True)
