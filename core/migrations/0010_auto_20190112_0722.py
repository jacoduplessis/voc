# Generated by Django 2.1.4 on 2019-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190102_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committeemember',
            old_name='email_address',
            new_name='email_address_private',
        ),
        migrations.AddField(
            model_name='committeemember',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]