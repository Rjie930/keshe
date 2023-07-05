"""
Django settings for DjangoElementUI project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-23%s4$b5$!xaldu!hjjoh#p04st_sz3rw5%ne7t2wh$%0e6mx+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     
    "tasks",


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DjangoElementUI.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],


        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoElementUI.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",

#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# 更改为中文
LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = False

SIMPLEUI_LOGO = 'https://cdn.pixabay.com/photo/2023/06/14/06/22/cat-8062388_640.jpg'
# 隐藏右侧SimpleUI广告链接和使用分析

SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# STATICFILES_DIRS = [
#     # BASE_DIR / "static",
# os.path.join(BASE_DIR, "static")
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。 空列表[] 为全部不显示.
    'menu_display': ['任务管理', '权限认证'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },

        {
            'name': '任务管理',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': '任务列表',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/tasks/task/',
                    'icon': 'fa fa-tasks'
                },
            ]
        },
    ]
}

# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False

# 修改左侧菜单首页设置
SIMPLEUI_HOME_PAGE = '/tasks/tasks/dashboard/'
SIMPLEUI_HOME_TITLE = '主页'
SIMPLEUI_HOME_ICON = 'fa fa-eye'

# 设置右上角Home图标跳转链接，会以另外一个窗口打开
SIMPLEUI_INDEX = ' http://127.0.0.1:8000/admin'
