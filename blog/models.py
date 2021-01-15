from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    published = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


class Meta:
    ordering = ('-publsh',)


def __str__(self):
    return self.title