# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fraud',
            name='flag',
            field=models.CharField(default='0', max_length=7),
        ),
    ]
