# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminfraud',
            name='fraud_identified_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='adminfraud',
            name='fraud_notified_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
