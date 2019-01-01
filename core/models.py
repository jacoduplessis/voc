from django.db import models
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField


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
    slug = models.SlugField()
    author = models.CharField(max_length=200, blank=True)
    date_published = models.DateField()
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', null=True, on_delete=models.SET_NULL)

    image = VersatileImageField(
        verbose_name='Image', upload_to='images/', width_field='width',
        height_field='height')
    caption = models.TextField(blank=True)
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )



class Research(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Research Item'
        verbose_name_plural = 'Research Items'


class CommitteeMember(models.Model):
    name = models.CharField(max_length=200)
    position_af = models.CharField(max_length=300)
    position_en = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=99)

    class Meta:
        ordering = ['order']
        verbose_name = 'Committee Member'
        verbose_name_plural = 'Committee Members'

    def __str__(self):
        return self.name
