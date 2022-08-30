"""
WSGI config for silkboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silkboard.settings')

application = get_wsgi_application()

# import smtplib
# import socks    # it is the package SocksiPy or PySocks

# socks.setdefaultproxy(socks.SOCKS5, '192.168.1.5', 8080)
# socks.wrapmodule(smtplib)

