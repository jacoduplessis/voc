"""
Django settings for voc project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '9mk@wi_@j0!-pbej&^0gou4uwk^jzdy=-o0^jz=j#$)53)#c7u')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", False)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
] if DEBUG else [
    '.voc-kaap.org',
    '.svoc.org.za',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    #'minio_storage',


    'crispy_forms',
    'versatileimagefield',
    'django_countries',
    'anymail',
    'core',

    'content',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'voc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'voc.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, default='postgres://postgres:postgres@localhost/postgres')
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

LOG_LEVEL = os.getenv('DJANGO_LOG_LEVEL', 'INFO')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        'django.request': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        'django.server': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'voc': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
    },
}

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ADMINS = [
    ('Jaco du Plessis', 'web@voc-kaap.org'),
]

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY"),
}
if not DEBUG:
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = "Stigting VOC <web@voc-kaap.org>"

# DEFAULT_FILE_STORAGE = 'minio_storage.storage.MinioMediaStorage'

MINIO_STORAGE_ENDPOINT = os.getenv('S3_ENDPOINT')
MINIO_STORAGE_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
MINIO_STORAGE_SECRET_KEY = os.getenv('S3_SECRET_KEY')
MINIO_STORAGE_USE_HTTPS = not DEBUG
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'media'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
