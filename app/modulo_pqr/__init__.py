from flask import Blueprint


modulo_pqr = Blueprint('modulo_pqr' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/pqr',
                            template_folder='templates'  )

from . import routes