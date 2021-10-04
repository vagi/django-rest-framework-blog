from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import re

from .models import Post, Comment


@receiver(pre_save, sender=Post)
def check_spec_symbols_in_post_headline(sender, instance, *args, **kwargs):
    """
    Before the post is saved in database we will check whether its headline
    contains special symbols, in case it does the symbols will be removed.
    """
    print(f"Text input: {instance.headline}, author: {instance.author}")    # Printing out Signal
    if re.search(r'[@_!#$%^&*()<>?/\|}{~:.,]', instance.headline):
        instance.headline = re.sub(r'[^\w\s]', '', instance.headline)
        print("The text has been cleaned successfully:", instance.headline)    # Printing out Signal
    else:
        print("The text is clean, there is no need to remove any symbol:", instance.id,
              instance.headline)    # Printing out Signal
