# Generated by Django 4.0.4 on 2023-04-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_movieslider_delete_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_quality',
            field=models.CharField(default='HD', max_length=80),
        ),
    ]
