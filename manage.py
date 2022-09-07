#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.mail import send_mail


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
    try:
        from django.core.management import execute_from_command_line
        send_mail('Test', 'This is a test', 'postmaster@sandbox7770466a202f4b4da56cd02ebd768362.mailgun.org',
                  ['laura.schiavulli@outlook.com'])

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
