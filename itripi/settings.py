
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'o3oked48zf_#fd6aah(ie9uitaj6^_5acz=2a+(9n#8=#mm*($'

DEBUG = True
ALLOWED_HOSTS = []

# Template Section
TEMPLATE_DEBUG = True
TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')
TEMPLATE_DIRS = (TEMPLATE_PATH,)


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher'
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'statistics',
    'usermanagement',
    'RideSharing',
    'djauthapp',
    'social.apps.django_app.default',
    # 'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)



ROOT_URLCONF = 'itripi.urls'
WSGI_APPLICATION = 'itripi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',        
#         'NAME': 'itc1',       
#         'USER':'root',
#         'PASSWORD':'banana',  
#         'PORT': '3306',
#         'HOST':'itripi.com'
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',        
#         'NAME': 'itripi',       
#         'USER':'asnim',
#         'PASSWORD':'tmmsolves',  
#         'PORT': '3306',
#         'HOST':'itripi.c82qjw7ako0n.ap-southeast-1.rds.amazonaws.com'
#     }
# }


# DATABASES = {
#     'default': {
#         #'ENGINE': 'mysql.connector.django',
#         'ENGINE': 'django.db.backends.mysql',
        
#         'NAME': 'itc',
#         'USER': 'root',
#         'PASSWORD': 'banana',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


    
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (STATIC_PATH,)

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')





#Social Authentication
FACEBOOK_EXTENDED_PERMISSIONS = ['email','public_profile','user_friends']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}
LOGIN_URL = '/usermanagement/login/'
LOGIN_REDIRECT_URL = 'http://itripi.com/djsite/'
SOCIAL_AUTH_FACEBOOK_KEY = '1765409270345320'
SOCIAL_AUTH_FACEBOOK_SECRET = '10dd7c4887a4393455baaf2ccd6f56c0'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '697226669218-b2mlkbpetn801pogeu8tnghraoia9gs7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'PoPoSsyzCUCda87CfL9lAQNB'
SOCIAL_AUTH_TWITTER_KEY = 'lNx...yQH8u'
SOCIAL_AUTH_TWITTER_SECRET = '8virx...Div4dwB'


# Storage
AWS_STORAGE_BUCKET_NAME = 'itripi'
AWS_ACCESS_KEY_ID = 'AKIAI52YAFLQVJQAM3KA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# AWS_STORAGE_BUCKET_NAME1 = 'itripimedia'
# AWS_S3_CUSTOM_DOMAIN1 = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME1

# STATICFILES_LOCATION = 'static'


# STATICFILES_STORAGE = 'custom_storages.StaticStorage'


# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN1
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage' 

# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "/media/"
MEDIA_ROOT = ""
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'