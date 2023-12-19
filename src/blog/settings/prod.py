from .base import *



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = BASE_DIR / 'staticfiles'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tomimartinez28$blog_db',
        'USER': 'tomimartinez28',
        'PASSWORD': 'Comision7',
        'HOST': 'tomimartinez28.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
