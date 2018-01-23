# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180123_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='group_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.UserProfile', verbose_name='\u7ec4\u7ba1\u7406\u5458'),
        ),
    ]
