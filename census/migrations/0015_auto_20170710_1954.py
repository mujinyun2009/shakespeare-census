# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0014_remove_copy_prov_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='Owner',
            field=models.CharField(max_length=500),
        ),
    ]