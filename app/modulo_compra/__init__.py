from flask import Blueprint


modulo_compra = Blueprint('modulo_compra' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/compra',
                            template_folder='templates'  )

from . import routes
