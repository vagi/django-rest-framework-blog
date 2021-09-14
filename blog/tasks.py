from celery import shared_task, app
from blog_project.celery import app
from .models import Author


@app.task
def change_author_is_notified_to_true():
    author_ids = list(
        Author.objects.filter(
            is_notified=False
        ).values_list('id', flat=True)
    )

    for author_id in author_ids:
        q = Author.objects.get(pk=author_id)
        print("Query before change:", q.is_notified)   # debugging
        print("Author_Id is:", author_id)    # debugging
        q.is_notified = True
        q.save()
        print("Query after change:", q.is_notified)   # debugging

