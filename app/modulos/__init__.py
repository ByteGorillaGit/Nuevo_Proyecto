from flask import Blueprint


module_shop = Blueprint('module_shop' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/shop',
                            template_folder='templates'  )


module_warranty = Blueprint('module_warranty' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/warranty',
                            template_folder='templates'  )

module_begin = Blueprint('module_begin' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/login',
                            template_folder='templates'  )

module_menu = Blueprint('module_menu' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/menu',
                            template_folder='templates'  )

module_pqr = Blueprint('module_pqr' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/pqr',
                            template_folder='templates'  )

module_privacy = Blueprint('module_privacy' ,
                            __name__ ,
                            static_folder='static',
                            url_prefix='/privacy',
                            template_folder='templates'  )

from . import routes
