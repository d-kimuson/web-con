import os

DEBUG = os.environ.get('DEBUG', 'true') == 'true'

if DEBUG:
    print("Using Config File: config/settings/develop.py")
    from .develop import *
else:
    print("Using Config File: config/settings/product.py")
    from .product import *
