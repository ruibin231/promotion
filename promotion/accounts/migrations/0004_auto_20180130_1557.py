# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-30 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180123_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='alias_name',
            field=models.CharField(max_length=15, unique=True, verbose_name='\u7ec4\u522b\u540d'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='group_name',
            field=models.CharField(max_length=15, unique=True, verbose_name='\u7ec4\u540d\u79f0'),
        ),
    ]
