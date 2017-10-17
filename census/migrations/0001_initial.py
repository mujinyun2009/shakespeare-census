# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 20:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookPlate_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner', models.CharField(max_length=500)),
                ('thumbnail_URL', models.URLField(max_length=500, null=True)),
                ('NSC', models.IntegerField(default=0, null=True)),
                ('Shelfmark', models.CharField(default=None, max_length=500, null=True)),
                ('Height', models.IntegerField(default=0, null=True)),
                ('Width', models.IntegerField(default=0, null=True)),
                ('Marginalia', models.CharField(max_length=100, null=True)),
                ('Condition', models.CharField(default=None, max_length=200, null=True)),
                ('Binding', models.CharField(default=None, max_length=200, null=True)),
                ('Binder', models.CharField(default=None, max_length=40, null=True)),
                ('Bookplate', models.CharField(default=None, max_length=40, null=True)),
                ('Bookplate_Location', models.CharField(default=None, max_length=100, null=True)),
                ('Bartlett1939', models.IntegerField(default=0, null=True)),
                ('Bartlett1939_Notes', models.CharField(default=None, max_length=1000, null=True)),
                ('Bartlett1916', models.IntegerField(default=0, null=True)),
                ('Bartlett1916_Notes', models.CharField(default=None, max_length=1000, null=True)),
                ('Lee_Notes', models.CharField(default=None, max_length=2000, null=True)),
                ('Library_Notes', models.CharField(default=None, max_length=2000, null=True)),
                ('copynote', models.CharField(default=None, max_length=5000, null=True)),
                ('prov_info', models.TextField(default=None, null=True)),
                ('librarian_validated', models.BooleanField(default=False)),
                ('admin_validated', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitted_copies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'copies',
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edition_number', models.CharField(max_length=20, null=True)),
                ('Edition_format', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STC_Wing', models.CharField(max_length=20)),
                ('ESTC', models.CharField(max_length=20)),
                ('year', models.CharField(default=None, max_length=20)),
                ('start_date', models.IntegerField(default=0)),
                ('end_date', models.IntegerField(default=0)),
                ('DEEP', models.IntegerField(default=0, null=True)),
                ('notes', models.CharField(default=None, max_length=1000, null=True)),
                ('Variant_Description', models.CharField(max_length=1000, null=True)),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Edition')),
            ],
        ),
        migrations.CreateModel(
            name='Provenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('bio', models.CharField(max_length=1000)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('Apocryphal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buyer', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='entity_buyer', to='census.Entity')),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy')),
                ('seller', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='entity_seller', to='census.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bleh', models.CharField(max_length=100)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer_Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=100)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation', models.CharField(max_length=255, null=True)),
                ('edited_copies', models.ManyToManyField(blank=True, null=True, to='census.Copy')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user details',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='edition',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Title'),
        ),
        migrations.AddField(
            model_name='copy',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Issue'),
        ),
        migrations.AddField(
            model_name='copy',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='census.Copy'),
        ),
        migrations.AddField(
            model_name='bookplate_location',
            name='copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy'),
        ),
        migrations.AddField(
            model_name='bookplate',
            name='copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='census.Copy'),
        ),
    ]
