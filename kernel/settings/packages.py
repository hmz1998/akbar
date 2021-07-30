import os

from django.conf import settings

from .base import (
    INSTALLED_APPS,
    STATIC_ROOT, BASE_DIR
)

# ############## #
#   EXTENSIONS   #
# ############## #
INSTALLED_APPS.append('admin_interface')
INSTALLED_APPS.append('colorfield')

INSTALLED_APPS.append('painless')

INSTALLED_APPS.append('rest_framework')
# INSTALLED_APPS.append('markdown')
# INSTALLED_APPS.append('django_filters')
#
INSTALLED_APPS.append('compressor')
#
# INSTALLED_APPS.append('fontawesome-free')
#
INSTALLED_APPS.append('corsheaders')
#
INSTALLED_APPS.append('admin_honeypot')
#
INSTALLED_APPS.append('django.contrib.admindocs')
# INSTALLED_APPS.append('django_extensions')
#

INSTALLED_APPS.append('sorl.thumbnail')
INSTALLED_APPS.append('django.contrib.admin')
INSTALLED_APPS.append('location_field.apps.DefaultConfig')

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

INSTALLED_APPS.append('cms')
# #
# INSTALLED_APPS.append('service')
# #
# INSTALLED_APPS.append('work')
# #
INSTALLED_APPS.append('pages')

# ######################### #
#       RestFramework       #
# ######################### #

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '6/day',
        'user': '6/day'
    }
}

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
#      LOCATION FIELD       #
# ######################### #

LOCATION_FIELD_PATH = settings.STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 13,

    'search.provider': 'nominatim',
    'search.suffix': '',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': '',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',

    # Mapbox
    'provider.mapbox.access_token': '',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': (
            LOCATION_FIELD_PATH + '/js/form.js',
        ),
    },
}
