# Generated by Django 4.0.4 on 2023-04-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='download_links',
        ),
        migrations.AddField(
            model_name='movie',
            name='download_links',
            field=models.ManyToManyField(blank=True, to='home.downloadlink'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_categories',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
    ]