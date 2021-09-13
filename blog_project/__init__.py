from .celery import app as celery_app
# from __future__ import absolute_import, unicode_literals


# This will start Celery automatically whenever Django starts
__all__ = ('celery_app',)
