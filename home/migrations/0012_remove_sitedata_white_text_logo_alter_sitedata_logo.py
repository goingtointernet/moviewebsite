# Generated by Django 4.0.4 on 2023-04-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_sitedata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedata',
            name='white_text_logo',
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='logo',
            field=models.CharField(default='Movies', max_length=160),
        ),
    ]
