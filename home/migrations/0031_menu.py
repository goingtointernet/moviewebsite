# Generated by Django 4.0.4 on 2023-04-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_rename_stream_movie_title_movie_stream_movie_or_show_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=160)),
            ],
        ),
    ]
