# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='affiliation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
