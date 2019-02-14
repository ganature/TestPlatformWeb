"""
Django settings for TestPlatformWeb project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
import logging
import django.utils.log
import logging.handlers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='-4_o19)(^&*qsm6!k9i_37xc%apo99t7betyn36pvrkq(xuejp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions',
                'django.contrib.messages','django.contrib.staticfiles','apps.users','apps.env_config','apps.project',
                'apps.test_case','apps.test_plan','apps.test_report','apps.test_suite','apps.keywords','xadmin',
                'crispy_forms','reversion','rest_framework']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF='TestPlatformWeb.urls'

TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [os.path.join(BASE_DIR,'templates')],
            'APP_DIRS': True,'OPTIONS': {
        'context_processors': ['django.template.context_processors.debug','django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages',],},},]

WSGI_APPLICATION='TestPlatformWeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR,'db.sqlite3'),}}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS=[{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
                          {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
                          {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
                          {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE='en-us'

TIME_ZONE='UTC'

USE_I18N=True

USE_L10N=True

USE_TZ=True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL='/static/'

PROJECT_PATH=os.path.join(BASE_DIR,'/project/')

AUTH_USER_MODEL="users.UserProfile"

STATICFILES_DIRS=(os.path.join(BASE_DIR,"static"),)

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Rest_framework
REST_FRAMEWORK={# Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly']}

# 设定登录的路由
LOGIN_URL='/login/'

ADMIN_USERNAME='admin'
ADMIN_PASSWORD='admin123'

# 创建日志的路径
LOG_PATH=os.path.join(BASE_DIR,'log')
# 如果地址不存在，则自动创建log文件夹
if not os.path.join(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGING={  # version只能为1,定义了配置文件的版本，当前版本号为1.0
    "version": 1,  # True表示禁用logger
    "disable_existing_loggers": False,  # 格式化
    'formatters': {'default': {'format': '%(levelno)s %(funcName) %(module)s %(asctime)s %(message)s '},
                   'simple': {'format': '%(levelno)s %(module)s %(created)s %(message)s'}},

    'handlers': {'stu_handlers': {'level': 'DEBUG',  # 日志文件指定为5M, 超过5m重新命名，然后写入新的日志文件
                                  'class': 'logging.handlers.RotatingFileHandler',  # 指定文件大小
                                  'maxBytes': 5*1024,  # 指定文件地址
                                  'filename': '%s/log.txt'%LOG_PATH,'formatter': 'default'},
                 'uauth_handlers': {'level': 'DEBUG',  # 日志文件指定为5M, 超过5m重新命名，然后写入新的日志文件
                                    'class': 'logging.handlers.RotatingFileHandler',  # 指定文件大小
                                    'maxBytes': 5*1024*1024,  # 指定文件地址
                                    'filename': '%s/uauth.txt'%LOG_PATH,'formatter': 'simple'}},
    'loggers': {'stu': {'handlers': ['stu_handlers'],'level': 'INFO'},
                'auth': {'handlers': ['uauth_handlers'],'level': 'INFO'}},

    'filters': {

    }}
