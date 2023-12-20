from .base import *



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'USER': 'root',
        'PASSWORD': 'abcdefgh',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
