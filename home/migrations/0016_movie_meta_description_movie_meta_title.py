# Generated by Django 4.0.4 on 2023-04-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_sitedata_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='meta_description',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='movie',
            name='meta_title',
            field=models.CharField(default='', max_length=160),
        ),
    ]
