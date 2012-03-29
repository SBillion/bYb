# Django settings for bYb project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DJANGO_ROOT = os.path.dirname(__file__).replace('\\','/')
SITE_ROOT = os.path.dirname(__file__)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':'43844_byb',                      # Or path to database file if using sqlite3.
        'USER': '43844',                      # Not used with sqlite3.
        'PASSWORD': 'hztijo38',                  # Not used with sqlite3.
        'HOST': 'mysql1.alwaysdata.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


gettext = lambda s: s

LANGUAGES = (
    ('fr', gettext('French')),
    ('en', gettext('English')),
)

DEFAULT_LANGUAGE = 1


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'public/media', '')).replace('\\','/')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'public/static', '')).replace('\\','/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 MEDIA_ROOT, 
   '/home/backup-your-brain/modules/django_blog_zinnia-0.10-py2.6.egg/zinnia/static',
'/usr/local/alwaysdata/python/django/1.3.1/django/contrib/admin/media',    


)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nt5b$z*_mkzd^!j98xpjwe5wv(xykvqj4x@j4_909l0bf0ijw$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
'localeurl.middleware.LocaleURLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'bYb.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',	
	'django.core.context_processors.i18n',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
    'django.core.context_processors.static',
  'zinnia.context_processors.version',
	#'zinnia.context_processors.media',
	'django.contrib.messages.context_processors.messages',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'modeltranslation',
    'localeurl',
    'tagging',
    'mptt',
	'django_bitly',
    'zinnia',	
    'django.contrib.sitemaps',
# Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MODELTRANSLATION_TRANSLATION_REGISTRY = "bYb.translation"

BITLY_LOGIN = 'backupyourbrain'
BITLY_API_KEY = 'R_6b6edd7cb41d694785abe4ab0e9cbaee'
ZINNIA_URL_SHORTENER_BACKEND = 'zinnia.url_shortener.backends.bitly'


TWITTER_CONSUMER_KEY = '2TOne1cCdnG59QiZy6Qtbw'
TWITTER_CONSUMER_SECRET = '2AiXO7n1c7eZrvWvyov3eIvGvWO2xLE8o6Bwzy9URA'
TWITTER_ACCESS_KEY = '538235480-JyznbkMUFqVaxzaeBXTV7gOAEP2R1BTNcjVeZNKL'
TWITTER_ACCESS_SECRET = 'KLrFElBkM5yDiKH2mSFYokvvcf6oZLL3vIQoC89Nh9c'

ZINNIA_USE_TWITTER=True
