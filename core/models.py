from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property
from django_countries.fields import CountryField
from versatileimagefield.fields import VersatileImageField


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
    public = models.BooleanField(default=False, help_text='True if it should be displayed on documents page')

    def __str__(self):
        return self.title


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
    content = models.TextField(blank=True, help_text='Content in markdown format')

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
    timeline = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True, help_text='Content in markdown format')

    def __str__(self):
        return self.title

    @cached_property
    def images(self):
        from content.models import Image as ContentImage
        tag = '_' + self._meta.label_lower + '.' + str(self.pk)
        return ContentImage.objects.filter(tags__contains=[tag])

    class Meta:
        ordering = ['-timeline']


class Tour(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateField(blank=True)
    content = models.TextField(blank=True, help_text='Content in markdown format')

    def __str__(self):
        return self.title

    @cached_property
    def images(self):
        from content.models import Image as ContentImage
        tag = '_' + self._meta.label_lower + '.' + str(self.pk)
        return ContentImage.objects.filter(tags__contains=[tag])

    class Meta:
        ordering = ['-date']


class Speaker(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    title = models.CharField(max_length=300)
    place = models.CharField(max_length=300, blank=True)
    date = models.DateField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name + ' ' + self.title

    class Meta:
        ordering = ['-date']


class Medal(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    date = models.DateField(blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @cached_property
    def images(self):
        from content.models import Image as ContentImage
        tag = '_' + self._meta.label_lower + '.' + str(self.pk)
        return ContentImage.objects.filter(tags__contains=[tag])


class Event(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField(blank=True, db_index=True)
    date_to_be_finalised = models.BooleanField(default=False)
    description = models.TextField(blank=True, help_text='Content in markdown format')

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField(db_index=True)
    document = models.FileField(upload_to='newsletters/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
