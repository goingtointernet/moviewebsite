# Generated by Django 4.0.4 on 2023-04-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_movie_stream_episode_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='stream_episode_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='stream_season_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
