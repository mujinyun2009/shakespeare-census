# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('census', '0026_copy_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='group',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitted_copies', to='auth.Group'),
        ),
    ]
