import os
import dj_database_url  # type: ignore

from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
if SECRET_KEY == '':
    class SecretKeyNotSetException(Exception):
        pass

    # 本番環境では, 必ず環境変数から取得する
    # GENERATOR: https://djecrety.ir/
    raise SecretKeyNotSetException('環境変数にSECRET_KEYを設置してください')

# Allowd Hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'webcon-staging.herokuapp.com'
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# 本番環境用 一時的にコメントアウト
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT'),
#     }
# }

# HEROKU用
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s a',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
