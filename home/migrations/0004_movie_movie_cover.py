# Generated by Django 4.0.4 on 2023-04-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_movie_movie_screenshot1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_cover',
            field=models.ImageField(null=True, upload_to='movie_cover'),
        ),
    ]
