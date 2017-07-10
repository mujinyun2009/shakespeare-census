# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('thumbnail_URL', models.URLField()),
                ('NSC', models.IntegerField(default=0)),
                ('Owner', models.CharField(max_length=40)),
                ('Shelfmark', models.IntegerField(default=0)),
                ('Height', models.IntegerField(default=0)),
                ('Width', models.IntegerField(default=0)),
                ('Marginalia', models.CharField(max_length=100, null=True)),
                ('Condition', models.CharField(max_length=200)),
                ('Binding', models.CharField(max_length=200)),
                ('Binder', models.CharField(max_length=40)),
                ('Bookplate', models.CharField(max_length=40)),
                ('Bookplate_Location', models.CharField(max_length=100)),
                ('Barlett1939', models.IntegerField(default=0)),
                ('Barlet1939_Notes', models.CharField(max_length=1000)),
                ('Barlet1916', models.IntegerField(default=0)),
                ('Barlet1916_Notes', models.CharField(max_length=1000)),
                ('Lee_Notes', models.CharField(max_length=2000)),
                ('Library_Notes', models.CharField(max_length=2000)),
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
                ('year', models.IntegerField(default=0)),
                ('Edition_number', models.IntegerField(default=0)),
                ('Edition_format', models.CharField(max_length=10)),
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
                ('STC_Wing', models.IntegerField(default=0)),
                ('DEEP', models.IntegerField(default=0)),
                ('ESTC', models.IntegerField(default=0)),
                ('Variant_Description', models.CharField(max_length=1000)),
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
                ('title', models.CharField(max_length=128)),
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
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editted_copies', models.ManyToManyField(blank=True, null=True, to='census.Copy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user histories',
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
