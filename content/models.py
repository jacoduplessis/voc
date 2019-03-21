from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models
from versatileimagefield.fields import VersatileImageField

TAG_MAX_LENGTH = 100


def validate_tag(val: str):
    if val.lower() != val:
        raise ValidationError("Only lowercase letters allowed")
    if ' ' in val:
        raise ValidationError("No spaces allowed")


class Image(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, db_index=True)

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

    tags = ArrayField(models.CharField(max_length=TAG_MAX_LENGTH, validators=[validate_tag]), db_index=True, blank=True,
                      null=True)

    def __str__(self):
        return str(self.image)


class Document(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=300, blank=True)
    author = models.CharField(max_length=200, blank=True)
    date_published = models.DateField(null=True, blank=True, help_text='Date on which the document was published')
    file = models.FileField(upload_to='documents/', blank=True)
    link = models.URLField(blank=True, help_text='Link to document if external file')
    description = models.TextField(blank=True, help_text='Text to describe contents of the document')

    tags = ArrayField(models.CharField(max_length=TAG_MAX_LENGTH, validators=[validate_tag]), db_index=True, blank=True,
                      null=True)

    def __str__(self):
        return self.title
