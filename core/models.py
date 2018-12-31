from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Member(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    PENDING = 'PENDING'

    STATE_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (PENDING, 'Pending'),
    )

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(blank=True, max_length=20)
    name = models.CharField(max_length=200)
    contact_number = models.CharField(blank=True, max_length=100)
    email_address = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    date_joined = models.DateField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, default=PENDING, max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    date_published = models.DateField()
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title
