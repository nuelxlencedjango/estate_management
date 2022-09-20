"""
Django settings for realestate project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from pickle import TRUE



import django_heroku

#import cloudinary_storage
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=os.environ.get('SECRET_KEY')
print(SECRET_KEY)

import secrets
print(secrets.token_hex(25))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=os.environ.get('DEBUG')


ALLOWED_HOSTS = ['www.wilmotinnovation.com','wilmotinnovation.com','wilmotestate.herokuapp.com']


#Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product.apps.ProductConfig',
    'django_filters',
    'accounts',
    'crispy_forms',
    'fontawesomefree',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realestate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR ,'templates')],
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

WSGI_APPLICATION = 'realestate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'HOST' :os.environ.get('DATABASE_HOST'),
        'PORT':os.environ.get('DATABASE_PORT'),
        'USER' :os.environ.get('DATABASE_USER'),
        'PASSWORD' :os.environ.get('DATABASE_PASSWORD'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'



STATICFILES_DIRS = [os.path.join(BASE_DIR ,'static') ]
STATIC_ROOT =os.path.join(BASE_DIR ,'assets')  

MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR ,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


cloudinary.config( 
   cloud_name=os.environ.get('CLOUD_NAME'),
  api_key=os.environ.get('API_KEY'), 
  api_secret=os.environ.get('API_SECRET'), 
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'





EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT=os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS=os.environ.get('EMAIL_USE_TLS')
EMAIL_BACKEND=os.environ.get('EMAIL_BACKEND')



django_heroku.settings(locals())


DEFAULT_AUTO_FIELD=os.environ.get('DEFAULT_AUTO_FIELD')


if os.getcwd() == '/app':
    SECURE_PROXY_SSL_HEADER =('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT =True
    DEBUG = False
