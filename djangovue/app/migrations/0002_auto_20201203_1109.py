# Generated by Django 3.1.4 on 2020-12-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='band',
            name='slug',
            field=models.CharField(default='', max_length=64),
        ),
    ]
