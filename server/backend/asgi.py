"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Required to make a seeminglessly switch between deployment_settings and the original settings.
settings_module = "backend.deployment_settings" if "RENDER_EXTERNAL_HOSTNAME" in os.environ else "backend.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()