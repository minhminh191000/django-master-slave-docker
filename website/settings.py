"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
from os.path import join, dirname
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


DB_HOST_SLAVE1 = os.environ.get("DB_HOST_SLAVE1")
DB_PORT_SLAVE1 = os.environ.get("DB_PORT_SLAVE1")
DB_NAME_SLAVE1 = os.environ.get("DB_NAME_SLAVE1")
DB_USER_SLAVE1 = os.environ.get("DB_USER_SLAVE1")
DB_PASSWORD_SLAVE1 = os.environ.get("DB_PASSWORD_SLAVE1")

DB_HOST_SLAVE2 = os.environ.get("DB_HOST_SLAVE2")
DB_PORT_SLAVE2 = os.environ.get("DB_PORT_SLAVE2")
DB_NAME_SLAVE2 = os.environ.get("DB_NAME_SLAVE2")
DB_USER_SLAVE2 = os.environ.get("DB_USER_SLAVE2")
DB_PASSWORD_SLAVE2 = os.environ.get("DB_PASSWORD_SLAVE2")



TEMPLATES_DIR = [
            os.path.join(BASE_DIR, "template"),
                 ]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1ty#%1tz7@6we$2kgw$d#80r)9o2ta)5$m4#66b%&wdv2f2wo1'

# RECAPTCHA KEY:

# RECAPTCHA_PUBLIC_KEY = '6Leo140oAAAAABRW8r2IwA9JsKVFYgqG6vNgi68K'
# RECAPTCHA_PRIVATE_KEY = '6Leo140oAAAAAOGFhKc3i68v1EYevue-CtqKYQmO'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # 'captcha',
    'restaurant',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIR,
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    },
    'slave1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME_SLAVE1,
        'USER': DB_USER_SLAVE1,
        'PASSWORD': DB_PASSWORD_SLAVE1,
        'HOST': DB_HOST_SLAVE1,
        'PORT': DB_PORT_SLAVE1,
    },
    'slave2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME_SLAVE2,
        'USER': DB_USER_SLAVE2,
        'PASSWORD': DB_PASSWORD_SLAVE2,
        'HOST': DB_HOST_SLAVE2,
        'PORT': DB_PORT_SLAVE2,
    }
}

DATABASE_ROUTERS = ['website.routers.MasterSlaveRouter']


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics")
]

# Media files (img , svg , png , etc)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom user base 
AUTH_USER_MODEL = 'users.UserModels'

LOGIN_REDIRECT_URL = '/users/login'
LOGOUT_REDIRECT_URL = '/users/login'
