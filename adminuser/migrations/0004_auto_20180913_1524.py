# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0003_auto_20180906_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminfraud',
            name='fraud_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]