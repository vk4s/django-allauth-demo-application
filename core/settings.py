from pathlib import Path
import os

import environ

from core.utils import get_allowed_hosts


# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR/".env")  # path to your ".env" file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env("SECRET_KEY", default="2%(zb7^s@d-mbp1b!=g@(^!$a2#-y)fexa@s(!ex)n_x+s1ypn")
DEBUG = env("DEBUG", default=True)
ENV = env("ENV", default="DEV")  # DEV, PROD

ALLOWED_HOSTS = get_allowed_hosts(env("ALLOWED_HOSTS", default="localhost,127.0.0.1"))
# this setting requires url scheme in the host (e.g. https://)https:// or http://)
CSRF_TRUSTED_ORIGINS = get_allowed_hosts(env("CSRF_TRUSTED_ORIGINS", default=""))

SITE_TITLE = env("SITE_TITLE", default="Django Setup Project")

# Email Settings
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env("EMAIL_PORT", default=465)
EMAIL_USE_SSL = env("EMAIL_USE_SSL", default=True)
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=False)
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)

# Database Settings
DB_LOCATION = env("DB_LOCATION", default="")

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # providers
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]


WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if ENV == "PROD":
    print("In prod")
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(DB_LOCATION) / "db.sqlite3",
    }
    print("DB Location", DATABASES["default"]["NAME"])

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# AUTH Providers Keys
GITHUB_CLIENT_ID = env("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = env("GITHUB_CLIENT_SECRET")
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET")

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': GOOGLE_CLIENT_ID,
            'secret': GOOGLE_CLIENT_SECRET,
            'key': ''
        },
        'AUTH_PARAMS': {
            'access_type': 'offline', #'online/offline
        },
        'OAUTH_PKCE_ENABLED': True,
        'VERIFIED_EMAIL':True,
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
        'APP': {
            'client_id': GITHUB_CLIENT_ID,
            'secret': GITHUB_CLIENT_SECRET,
            'key': ''
        },
        'VERIFIED_EMAIL':True,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "public/"
STATIC_ROOT = os.path.join(BASE_DIR, "public")

# Extra places for collectstatic to find static files.
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "media"), os.path.join(BASE_DIR, "assets"))

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "login"

LOGIN_URL = "login"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
