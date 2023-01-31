from .base import *
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='django-insecure-csqvn!iydvk(8rz0+nz0uf1a7v835$n7_9lq!!*y0o*!@dq=hz',
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "*"]

