# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0027_remove_qualification_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.FileField(default=b'project/media/profile_image/download.png', upload_to=b'project/media/profile_image'),
        ),
    ]