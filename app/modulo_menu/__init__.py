from flask import Blueprint


modulo_menu = Blueprint('modulo_menu' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/menu',
                            template_folder='templates'  )

from . import routes