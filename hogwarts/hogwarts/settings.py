"""
Django settings for hogwarts project.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ex629+bp_*v#e8*b2#&%f!z9p_ass74vn^o=wi30jjdp=1kv-*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.request",)

ALLOWED_HOSTS = '*'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marauder',
    'south',
    'django_tables2',
    'haystack'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hogwarts.urls'

WSGI_APPLICATION = 'hogwarts.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': { 'ENGINE': 'mysql.connector.django',
        'NAME': 'domoench$default',
        'USER': 'domoench',
        'PASSWORD': 'lemonsherbert',
        'HOST': 'mysql.server',
        'TEST_NAME': 'domoench$test_default',
    }
}

SOUTH_DATABASE_ADAPTERS = {
   'default': 'south.db.mysql'
}

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

# Haystack Connection to Whoosh Index Directory 
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = '/home/domoench/cs373-idb/hogwarts/marauder/media'
MEDIA_URL = '/media/'
