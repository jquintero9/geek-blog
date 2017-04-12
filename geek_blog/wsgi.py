#!usr/local/bin
# coding: latin-1

"""
WSGI config for geek_post project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

"""
Esta libreria de python whitenoise permite gestionar el almacenamiento
de los archivos estaticos de la aplicación.
"""
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geek_blog.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
