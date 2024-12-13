#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# Required to make a seeminglessly switch between deployment_settings and the original settings.
settiings_module = 'backend.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',settiings_module)
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()