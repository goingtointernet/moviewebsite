# Generated by Django 4.0.4 on 2023-05-07 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_staticposts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticposts',
            old_name='slug',
            new_name='permalink',
        ),
    ]
