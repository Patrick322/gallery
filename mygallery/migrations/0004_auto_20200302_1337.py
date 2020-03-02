# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-02 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0003_auto_20200302_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_image',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
    ]
