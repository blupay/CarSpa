"""
Django settings for CarSpa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT=os.path.dirname(os.path.realpath(__file__))


ALLOWED_HOSTS = []


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



TIME_ZONE = 'Africa/Accra'



LANGUAGE_CODE = 'en-us'


USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'static/'


STATIC_URL = '/static/'



# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths
    	os.path.join(SITE_ROOT,'assets'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#$tr^9$@jt95f6-zg4gwj08h=99q3lz@*bmnq7#z#l3_4&csjz'




# Application definition



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)




MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
   # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)








ROOT_URLCONF = 'CarSpa.urls'

WSGI_APPLICATION = 'CarSpa.wsgi.application'





TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(SITE_ROOT,'templates'),
)






TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'  # admin app wants this too
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

SUIT_CONFIG = {
    
     'MENU': (
	'sites',
          {'app': 'carspaapp','label': 'Modules', 'icon':'icon-th'},
          
          
         
          
          
    ),
    
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_REQUIRED_ASTERISK': True,
    'SEARCH_URL': '',
    
    'ADMIN_NAME': 'CAR SPA ADMINISTRATION',
    'MENU_OPEN_FIRST_CHILD': True,
    
    
}


INSTALLED_APPS = (
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'CarSpaApp',
    'autocomplete_light',
    'suit',
    'django.contrib.admin',
    
)
