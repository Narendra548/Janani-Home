# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0011_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
