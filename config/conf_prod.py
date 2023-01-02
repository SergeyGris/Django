import os

from .settings import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "generate_new_valid_key")

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "lms",
        "USER": "postgres",

    }
}

# del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"