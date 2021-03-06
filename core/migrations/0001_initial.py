# Generated by Django 2.1.7 on 2019-03-21 14:15

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position_af', models.CharField(max_length=300)),
                ('position_en', models.CharField(max_length=300)),
                ('email_address_private', models.EmailField(blank=True, max_length=254)),
                ('email_address_public', models.EmailField(blank=True, max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=99)),
            ],
            options={
                'verbose_name': 'Committee Member',
                'verbose_name_plural': 'Committee Members',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('date_published', models.DateField(blank=True, help_text='Date on which the document was published', null=True)),
                ('file', models.FileField(blank=True, upload_to='documents/')),
                ('link', models.URLField(blank=True, help_text='Link to document if external file')),
                ('description', models.TextField(blank=True, help_text='Publicly shown text to describe contents of the document')),
                ('notes', models.TextField(blank=True, help_text='Private notes not shown publicly')),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('date', models.DateField(blank=True)),
                ('short_description', models.CharField(blank=True, max_length=300)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('contact_number', models.CharField(blank=True, max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('notes', models.TextField(blank=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
                ('state', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('author', models.CharField(blank=True, max_length=200)),
                ('date_published', models.DateField()),
                ('extract', models.TextField(blank=True, max_length=500)),
                ('content', models.TextField(blank=True, help_text='content in markdown format')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(height_field='height', upload_to='images/', verbose_name='Image', width_field='width')),
                ('caption', models.TextField(blank=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='core.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('timeline', models.CharField(blank=True, max_length=300)),
                ('short_description', models.CharField(blank=True, max_length=500)),
                ('content', models.TextField(blank=True, help_text='content in markdown format')),
            ],
            options={
                'ordering': ['-timeline'],
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('link', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Research Item',
                'verbose_name_plural': 'Research Items',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=300)),
                ('place', models.CharField(blank=True, max_length=300)),
                ('date', models.DateField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('date', models.DateField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
