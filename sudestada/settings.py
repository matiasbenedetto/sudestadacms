"""
Django settings for sudestada project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(xtw50zardq2-07ts_fu$5q6#z6826j*@bexs_(ndqh*nu-6s6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'revista',
    'suit_redactor', # http://django-suit.readthedocs.org/
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    #'debug_toolbar', # http://django-debug-toolbar.readthedocs.org/
    'embed_video', # https://github.com/yetty/django-embed-video
    'sorl.thumbnail', #
    'adminsortable', # https://github.com/jrief/django-admin-sortable2
    'redactor', # https://github.com/douglasmiranda/django-wysiwyg-redactor
    'bootstrapform', #https://django-bootstrap-form.readthedocs.org

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
    "revista.context_processors.secciones",
    "revista.context_processors.articulos_mas_vistos",
    "revista.context_processors.banners",
    "revista.context_processors.lista_colecciones"
)

ROOT_URLCONF = 'sudestada.urls'

WSGI_APPLICATION = 'sudestada.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = ('127.0.0.1',)


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.revistasudestada.com.ar']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'


#http://django-suit.readthedocs.org/en/develop/configuration.html
SUIT_CONFIG = {
    'ADMIN_NAME': 'Revista Sudestada'
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'sudestada_no_responder'
EMAIL_HOST_PASSWORD = 'sudesadmin2015'
DEFAULT_FROM_EMAIL = "no-responder@revistasudestada.com.ar"
SERVER_EMAIL = "no-responder@revistasudestada.com.ar"

try:
    from settings_local import *
except ImportError:
    print u'File settings_local.py is not found. Continuing with production settings.'