from django.conf import settings
import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECRET_KEY = "2fk6@6o8e$eev$n*28h_@ui7w3)&zc65!n*jp4897wv!ej=w!+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
# DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account.apps.AccountConfig',
    'jobs.apps.JobsConfig',
    'contact.apps.ContactConfig',
    'blog.apps.BlogConfig',
    'faq.apps.FaqConfig',


    'ckeditor',
    'crispy_forms',
    'django_filters',   
]

AUTH_USER_MODEL = 'account.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'job_portal.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'job_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'

LOGIUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '../'



# Third party apps configuration

CRISPY_TEMPLATE_PACK = 'bootstrap4'



# File Based Email
# EMAIL_BACKEND = "django.core.mail.backends.filebase.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_mail")

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER =  config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =  config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'SMARTKTMJOBS Team <noreply@example.com>'



CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline', 'Strikethrough', 'Subscript', 'Superscript',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             '-', 'Font',
             '-', 'Size',
             '-', 'Show Blocks',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             '-', 'NumberedList',
             '-', 'BulletedList',
             '-', 'Outdent',
             '-', 'Indent',
             '-', 'Increase Indent',
             '-', 'Decrease Indent',
             '-', 'JustifyLeft',
             '-', 'JustifyCenter',
             '-', 'JustifyRight',
             '-', 'JustifyBlock',
             '-', 'RemoveFormat',
             '-', 'Source',
             '-', 'Image',
             '-', 'Smiley',
             '-', 'Table',

            ],
        ],
        'height': '100%',
        'width': '100%',
        'toolbarCanCollapse': False,
    },
}


