# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20170422_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsemodel',
            name='parentResponse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.ResponseModel', verbose_name='Parent Response'),
        ),
    ]
