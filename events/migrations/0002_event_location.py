# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-05 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
