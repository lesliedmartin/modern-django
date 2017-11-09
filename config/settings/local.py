from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default="@yq*o%44p5$+&+-q#0)yl$-!_24g0kzo=nbuc_kl#5pl15b3(z'")

DEBUG = env.bool('DJANGO_DEBUG', default=True)

