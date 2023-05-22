from shop.settings import *

DEBUG = False
TEMPLATES_DEBUG = False

SECRET_KEY ='vrnn)&5=8m1qqyhdh&+^b&fgpq7t(5tx$u-in1)epg8&k89v^j'

ALLOWED_HOSTS = [ 'https://mercadona2.herokuapp.com']

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'store/static') ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')