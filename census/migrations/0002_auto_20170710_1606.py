# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]