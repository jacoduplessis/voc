# Generated by Django 2.1.4 on 2019-01-02 08:22

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190102_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
