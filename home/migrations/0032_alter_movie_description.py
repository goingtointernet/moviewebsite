# Generated by Django 4.0.4 on 2023-05-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
