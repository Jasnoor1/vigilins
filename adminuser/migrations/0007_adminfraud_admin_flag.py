# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0006_auto_20180913_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminfraud',
            name='admin_flag',
            field=models.CharField(default='0', max_length=7),
        ),
    ]
