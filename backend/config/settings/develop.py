from .base import *

DEBUG = True

if SECRET_KEY == '':
    SECRET_KEY = '59@49^1q-ddy3_n_gj4b*rn+h%tsy)qgop3_+ei13*_7&bvo%9'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]
