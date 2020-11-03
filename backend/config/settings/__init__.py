import os
from dotenv import load_dotenv

load_dotenv(verbose=True)  # pipenv外から実行したときにも `.env` を読み込むため

DEBUG = os.environ.get('DEBUG', 'true') == 'true'

if DEBUG:
    print("Using Config File: config/settings/develop.py")
    from .develop import *
else:
    print("Using Config File: config/settings/product.py")
    from .product import *
