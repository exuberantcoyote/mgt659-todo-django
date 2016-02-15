# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20160212_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='collaborator1',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='collaborator2',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='collaborator3',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='task',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='isOwner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]