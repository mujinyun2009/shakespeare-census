# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0024_auto_20170726_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='Bartlett1916',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='copy',
            name='Bartlett1939',
            field=models.IntegerField(default=0, null=True),
        ),
    ]