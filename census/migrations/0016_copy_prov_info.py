# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0015_auto_20170710_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='prov_info',
            field=models.TextField(default=None, null=True),
        ),
    ]
