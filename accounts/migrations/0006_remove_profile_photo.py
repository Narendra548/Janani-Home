# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_educational_need'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
    ]
