# Generated by Django 4.0.4 on 2023-04-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_sitedata_movie_banner_min_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='latest_post_section_heading',
            field=models.CharField(default='Latest Movies', max_length=100),
        ),
    ]
