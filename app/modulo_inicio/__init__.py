from flask import Blueprint


modulo_inicio = Blueprint('modulo_inicio' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/login',
                            template_folder='templates'  )

from . import routes
