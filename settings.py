## File for CPython with DjAngo framework. With secure headers and working code for Microsoft SQL Server.

import os
import posixpath

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '297fea90-a5d0-4b47-b141-4ea6464969ac'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'Herramientas.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'Herramientas.wsgi.application'

DATABASES = {
    "default": {
        "NAME": "", ##Database
        "ENGINE": "sql_server.pyodbc", ##Library pyodbc driver
        "USER": "", ##User of Windows SQL Server
        "PASSWORD": "", ##Password for the Windows SQL Server#
        "HOST": "", ##Let it be 127.0.0.1/NAMEOFINSTANCE
        "PORT": "", ##Port, usually 1433
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server", ##With this driver is enough
        },
    },
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'es-MX'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True
DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET = 'UTF-8'
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
TIMEOUT = 320
VERSION = 2
TIME_FORMAT = 'P'
TIME_INPUT_FORMATS = [
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
]
PASSWORD_HASHERS =  [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]
CACHE_MIDDLEWARE_SECONDS = 7200
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
## more info : https://docs.djangoproject.com/en/2.1/topics/security/
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 3600
CSRF_COOKIE_DOMAIN = "carpo.solar"
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_AGE = 3600
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = [".deimos.me", ".fochoao.com", ".phobos.chat", ".carpo.solar"]
CSRF_COOKIE_NAME = 'io_csrf_data'
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_SAMESITE = 'Strict'
CSRF_USE_SESSIONS = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_NAME = 'io_carpo_session'
SESSION_COOKIE_AGE = 7200
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
LANGUAGE_COOKIE_PATH = '/'
LANGUAGE_COOKIE_DOMAIN = ".phobos.chat, .carpo.solar, .fochoao.work, .fochoao.com"
LANGUAGE_COOKIE_NAME = 'io_lang_tool'
LANGUAGE_COOKIE_AGE = None
USE_X_FORWARDED_HOST = False
USE_X_FORWARDED_PORT = False
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024621440
FILE_UPLOAD_PERMISSIONS = 755
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024621440
