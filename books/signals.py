import logging

from django.db.models.signals import (post_save,
                                      post_delete
                                      )
from django.dispatch import receiver

from .models import Book


@receiver(post_save, sender=Book)
def log_book_updated_added_event(sender, **kwargs):
    """
        Writes information about newly added or updated
        book into log file
    """
    logger = logging.getLogger(__name__)
    book = kwargs['instance']
    if kwargs['created']:
        logger.info("Book added: %s (ID: %d)", book.title, book.id)
    else:
        logger.info("Book updated: %s (ID: %d)", book.title, book.id)


@receiver(post_delete, sender=Book)
def log_book_delete_event(sender, **kwargs):
    """
        Writes information about recently deleted
        book into log file
    """
    logger = logging.getLogger(__name__)
    book = kwargs['instance']
    logger.info("Book deleted: %s (ID: %d)", book.title, book.id)
