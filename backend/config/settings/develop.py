import logging

from .base import *

DEBUG = True

if SECRET_KEY == '':
    SECRET_KEY = '59@49^1q-ddy3_n_gj4b*rn+h%tsy)qgop3_+ei13*_7&bvo%9'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
    'drf_spectacular',
    'nplusone.ext.django',
    'debug_toolbar',
]

MIDDLEWARE += [
    'nplusone.ext.django.NPlusOneMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _: True
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# N + 1クエリの自動検出ログ
NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
        },
    },
}

DATABASES = {
    # 接続情報は、 `./db/Dockerfile` を参照すること
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_con_django',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_web_con_django'
        }
    }
}
