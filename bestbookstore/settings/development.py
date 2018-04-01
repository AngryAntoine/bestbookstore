from .base import *

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += [
    #  third party apps
    'bootstrapform',
    'debug_toolbar',
    'isbn_field',
    'storages',

    #  local apps
    'books',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'bestbookstore',
#         'USER': 'bestbookstore_user',
#         'PASSWORD': config('DATABASE_PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
