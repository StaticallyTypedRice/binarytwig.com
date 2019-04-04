"""
Django settings.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(SETTINGS_DIR, '..')

# The name of the website.
WEBSITE_NAME = 'BinaryTwig'

# A lower case version of the website name with no spaces.
WEBSITE_NAME_SLUG = 'binarytwig'

# The website name stylized with HTML.
# This setting is optional. If it is not set, the unstylized name will be used.
WEBSITE_NAME_STYLIZED = 'BinaryTwig'

# The paths for configuration file.
# The paths will be searched in order, and the first valid path will be used.
CONFIGURATION_FILE_PATHS = [
    os.path.join(BASE_DIR, '..', 'private', WEBSITE_NAME_SLUG + '.config'),
    os.path.join(BASE_DIR, '..', 'setup', WEBSITE_NAME_SLUG + '.config')
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'crispy_forms',
    'django_cleanup',
    'import_export',
    'cookielaw',
    'analytical',

    # Website apps
    'apps.home',
    'apps.about',
    'apps.blog',
    'apps.utils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Third party middleware classes
    #'htmlmin.middleware.HtmlMinifyMiddleware',
    #'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom context processors
                'apps.utils.context_processors.website_name',
                'apps.utils.context_processors.website_mode',
                'apps.utils.context_processors.google_web_utils',
                'apps.home.context_processors.external_sites'
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'main'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django-htmlmin
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = True
