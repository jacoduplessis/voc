from django.db import models
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField
from django_countries.fields import CountryField


class Document(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300, blank=True)
    author = models.CharField(max_length=200, blank=True)
    date_published = models.DateField(null=True, blank=True, help_text='Date on which the document was published')
    file = models.FileField(upload_to='documents/', blank=True)
    link = models.URLField(blank=True, help_text='Link to document if external file')
    description = models.TextField(blank=True, help_text='Publicly shown text to describe contents of the document')
    notes = models.TextField(blank=True, help_text='Private notes not shown publicly')

    def __str__(self):
        return self.title


# class Image(models.Model):
#     image = VersatileImageField(
#         verbose_name='Image', upload_to='images/', width_field='width',
#         height_field='height')
#     caption = models.TextField(blank=True)
#     height = models.PositiveIntegerField(
#         'Image Height',
#         blank=True,
#         null=True
#     )
#     width = models.PositiveIntegerField(
#         'Image Width',
#         blank=True,
#         null=True
#     )


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
    country = CountryField(blank=True)
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
    extract = models.TextField(max_length=500, blank=True)
    content = RichTextField(blank=True)
    # images = models.ManyToManyField(Image, related_name='posts')
    documents = models.ManyToManyField(Document, related_name='posts')

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
    email_address_private = models.EmailField(blank=True)
    email_address_public = models.EmailField(blank=True)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=99)

    class Meta:
        ordering = ['order']
        verbose_name = 'Committee Member'
        verbose_name_plural = 'Committee Members'

    def __str__(self):
        return self.name


class Project(models.Model):

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    content = RichTextField(blank=True)