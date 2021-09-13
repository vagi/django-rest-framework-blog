from datetime import timedelta
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    'change_author_is_notified_to_true': {
        'task': 'change_author_is_notified_to_true',
        'schedule': crontab(minute=2),
    },
}

