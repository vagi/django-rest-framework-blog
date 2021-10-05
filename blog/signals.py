from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

import re
# Importing library for filtering of censored words
from profanity_filter import ProfanityFilter

from .models import Post, Comment


@receiver(pre_save, sender=Post)
def check_spec_symbols_in_post_headline(sender, instance, *args, **kwargs) -> None:
    """
    Before the post is saved in database we will check whether its headline
    contains special symbols, in case it does the symbols will be removed.
    :param sender: object
    :param instance: object
    :param args:
    :param kwargs:
    :return: None
    """
    print(f"Text input: {instance.headline}, author: {instance.author}")    # Printing out Signal
    if re.search(r'[@_!#$%^&*()<>?/\|}{~:.,]', instance.headline):
        instance.headline = re.sub(r'[^\w\s]', '', instance.headline)
        print("The text has been cleaned successfully:", instance.headline)    # Printing out Signal
    else:
        print("The text is clean, there is no need to remove any symbol:", instance.id,
              instance.headline)    # Printing out Signal


@receiver(pre_save, sender=Comment)
def remove_censored_words_in_comment(sender, instance, *args, **kwargs) -> None:
    """
    Check and remove if any censored words from a Comment before the Commment
    is saved in database
    :param sender: object
    :param instance: object
    :param args:
    :param kwargs:
    :return: None
    """
    print(f"Comment input: {instance.comment_text}")    # printing out Signal
    pf = ProfanityFilter()
    instance.comment_text = pf.censor(instance.comment_text)
    print(f"The text is filtered - the output is: {instance.comment_text}")    # printing out Signal


@receiver(pre_delete, sender=Comment)
def blog_comment_cancel_pre_delete(sender, instance, *args, **kwargs) -> None:
    """
    Before deletion of a Comment informs us and cancel that deletion
    :param sender: object
    :param instance: object
    :param args:
    :param kwargs:
    :return: None
    """
    if instance.id:
        print(f"ID {instance.id} is going to be removed!")
        raise Exception(f'Do not delete the Comment with ID:{instance.id}')  # cancel the deletion
        # instance.protected = True
        # instance.save()
        # print(f"ID {instance.id} Its protection status: {instance.protected}")


@receiver(post_delete, sender=Comment)
def blog_comment_post_delete(sender, instance, *args, **kwargs) -> None:
    """
    Informs us that a Comment was deleted
    :param sender: object
    :param instance: object
    :param args:
    :param kwargs:
    :return: None
    """
    print(f"{instance.id} has been removed!")
