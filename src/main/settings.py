"""
Django settings for fabric_interface project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&niezm3se6@a2i2n7#o3_^h@qzn_wh!3@1a_w6sg%mfmi8(tr*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'mptt',
    'guardian',
    'bootstrap3',
    'reversion',
    'django_tables2',

    # Application
    'fabric_interface',
    'fabric_interface.projects',
    'fabric_interface.stages',
    'fabric_interface.hosts',
    'fabric_interface.configurations',
    'fabric_interface.formulae',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'fabric_interface.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}

# Cache
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Guardian
ANONYMOUS_USER_ID = -1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Locale
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "main/templates"),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.contrib.messages.context_processors.messages",

    "fabric_interface.context_processors.demo",
    "fabric_interface.context_processors.language",
    "fabric_interface.context_processors.footer",
    "fabric_interface.context_processors.users",
    "fabric_interface.projects.context_processors.projects",
    "fabric_interface.hosts.context_processors.hosts",
)

# Auth
AUTH_USER_MODEL = 'fabric_interface.User'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', _(u"English")),
    ('nl', _(u"Dutch")),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Bootstrap3 using bootstrapper
BOOTSTRAP3 = {
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'base_url': STATIC_URL,
    'theme_url': STATIC_URL + 'ccs/bootstrap-theme.min.css',
}

# Fixtures
#
# admin: admin@example.com
# pass: admin
#
# user: johndoe@example.com
# pass: test
#
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures"),
)

try:
    from local_settings import *
except ImportError:
    pass