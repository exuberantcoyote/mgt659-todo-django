# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 22:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20160215_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.MinLengthValidator(1)]),
        ),
    ]
