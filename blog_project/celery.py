#from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

# Namespace 'CELERY' means all celery-related configuration keys should have
# that prefix
app = Celery('blog_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'change_author_is_notified_to_true': {
        'task': 'blog.tasks.change_author_is_notified_to_true',
        'schedule': crontab(),    # crontab() means 1 min
    },
}
