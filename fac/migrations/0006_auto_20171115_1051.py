# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0005_auto_20171114_1249'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Faculty',
        ),
    ]