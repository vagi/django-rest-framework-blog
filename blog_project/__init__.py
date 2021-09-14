from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

# This will start Celery automatically whenever Django starts
__all__ = ('celery_app',)
