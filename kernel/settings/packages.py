import os

from .base import (
    INSTALLED_APPS,
    STATIC_ROOT, BASE_DIR
)

# ############## #
#   EXTENSIONS   #
# ############## #

# INSTALLED_APPS.append('painless')

# INSTALLED_APPS.append('rest_framework')
# INSTALLED_APPS.append('markdown')
# INSTALLED_APPS.append('django_filters')
#
# INSTALLED_APPS.append('compressor')
#
# INSTALLED_APPS.append('fontawesome-free')
#
# INSTALLED_APPS.append('corsheaders')
#
# INSTALLED_APPS.append('admin_honeypot')
#
# INSTALLED_APPS.append('django.contrib.admindocs')
# INSTALLED_APPS.append('django_extensions')
#
# INSTALLED_APPS.append('admin_interface')
# INSTALLED_APPS.append('colorfield', )
# INSTALLED_APPS.append('sorl.thumbnail', )

# #################### #
#     HTML MINIFY      #
# #################### #

HTML_MINIFY = False
KEEP_COMMENTS_ON_MINIFYING = False

# #################### #
#       Compress       #
# #################### #

COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

# ############## #
# CUSTOM PROJECT #
# ############## #

# INSTALLED_APPS.append('cms')
# #
# INSTALLED_APPS.append('service')
# #
# INSTALLED_APPS.append('work')
# #
# INSTALLED_APPS.append('pages')

# ######################### #
#       RestFramework       #
# ######################### #

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny'
#     ],
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'rest_framework.renderers.JSONRenderer',
#     # ),
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle'
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '6/day',
#         'user': '6/day'
#     }
# }

# ######################### #
#       AdminInterface      #
# ######################### #

X_FRAME_OPTIONS = 'SAMEORIGIN'

# ######################### #
#     Django Extensions     #
# ######################### #

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True
}

# ######################### #
#        Translation        #
# ######################### #
#
# USE_I18N = True
#
# if USE_I18N:
#     if not os.path.isdir(os.path.join(BASE_DIR, 'locales/')):
#         os.mkdir(os.path.join(BASE_DIR, 'locales/'))
#
# LANGUAGES = (
#     ('en', 'English'),
#     ('ar', 'Arabic'),
# )
#
# MODELTRANSLATION_LANGUAGES = ('en', 'ar')
# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
# MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'
#
# LOCALE_PATHS = (os.path.join(BASE_DIR, 'locales/'),)
