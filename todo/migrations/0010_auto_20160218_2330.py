# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20160218_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='user',
            name='hashPassword',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
