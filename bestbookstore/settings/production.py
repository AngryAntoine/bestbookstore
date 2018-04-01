import dj_database_url

from .base import *

ALLOWED_HOSTS = ['*']


INSTALLED_APPS += [
    #  third party apps
    'bootstrapform',
    'isbn_field',
    'storages',

    #  local apps
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
] + MIDDLEWARE

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

USE_I18N = True

USE_L10N = True

USE_TZ = True


#  serving static on AWS
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bestbookstore-assets'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'bestbookstore.settings.storage_backends.MediaStorage'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
