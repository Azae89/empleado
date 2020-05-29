from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bdempleado',
        'USER': 'aaspajo',
        'PASSWORD': '112358Root',
        'HOST': 'localhost',
        'PORT': '3360',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]
STATIC_ROOT=BASE_DIR.child('staticfiles')

MEDIA_URL= '/media/'
MEDIA_ROOT=BASE_DIR.child('media')
