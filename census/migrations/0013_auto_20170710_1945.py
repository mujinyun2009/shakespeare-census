# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0012_auto_20170710_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='prov_info',
            field=models.TextField(null=True),
        ),
    ]
