from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from isbn_field import ISBNField
from datetime import date


class Author(models.Model):
    """
        Author Model
    """
    name            = models.CharField(max_length=60)
    slug            = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('books:author_detail', kwargs={'slug': self.slug})


def upload_location(instance, filename):
    return '%s/%s' % (instance.title, filename)


class Book(models.Model):
    """
        Book Model
    """
    title           = models.CharField(max_length=60)
    slug            = models.SlugField(max_length=80)
    authors         = models.ManyToManyField(Author, related_name='books', blank=False)
    isbn            = ISBNField()
    image           = models.ImageField(upload_to=upload_location, null=True, blank=True)
    price           = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    publish_date    = models.DateField(default=date.today, blank=True)
    created         = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated         = models.DateTimeField(auto_now=False, auto_now_add=True)
    active          = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'slug': self.slug,
                                                    'pk': self.pk
                                                    })


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Book.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_book_receiver(sender, instance, *args, **kwargs):
    if not instance.publish_date:
        instance.publish_date = date.today()
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_book_receiver, sender=Book)


class RequestListener(models.Model):
    request_value      = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return '%s' % self.pk
