# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0018_merge_20170714_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='end_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='issue',
            name='start_date',
            field=models.IntegerField(default=0),
        ),
    ]