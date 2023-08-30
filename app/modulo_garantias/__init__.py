from flask import Blueprint


modulo_garantias = Blueprint('modulo_garantias' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/garantias',
                            template_folder='templates'  )

from . import routes
