# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='credit_code',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u7edf\u4e00\u793e\u4f1a\u4fe1\u7528\u4ee3\u7801'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u804c\u4e1a'),
        ),
    ]
