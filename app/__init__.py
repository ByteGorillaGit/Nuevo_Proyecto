from flask import Flask, render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.modulos import modulo_warranty
from app.modulos import modulo_menu
from app.modulos import modulo_begin
from app.modulos import modulo_shop
from app.modulos import modulo_pqr
from app.modulos import modulo_privacy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app=app , db=db)
from .models import Rol


app.register_blueprint(modulo_warranty)
app.register_blueprint(modulo_menu)
app.register_blueprint(modulo_begin)
app.register_blueprint(modulo_shop)
app.register_blueprint(modulo_pqr)
app.register_blueprint(modulo_privacy)



if __name__ == '__main__':
    app.run(port=3000, debug=True)
