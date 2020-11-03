from .base import *

DEBUG = True

if SECRET_KEY == '':
    SECRET_KEY = '59@49^1q-ddy3_n_gj4b*rn+h%tsy)qgop3_+ei13*_7&bvo%9'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    # 接続情報は、 `./db/Dockerfile` を参照すること
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_con_django',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'TEST': {
        #     'NAME': 'test_app'
        # }
    }
}
