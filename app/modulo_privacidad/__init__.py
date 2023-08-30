from flask import Blueprint


modulo_privacidad = Blueprint('modulo_privacidad' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/priv',
                            template_folder='templates'  )

from . import routes