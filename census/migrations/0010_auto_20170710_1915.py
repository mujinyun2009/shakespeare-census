# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0009_auto_20170710_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='copynote',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AddField(
            model_name='copy',
            name='prov_info',
            field=models.CharField(default=None, max_length=8000),
        ),
    ]