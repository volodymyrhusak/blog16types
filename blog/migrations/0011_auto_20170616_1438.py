# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170616_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcommentmodel',
            name='createTime',
            field=models.FloatField(default=1497623880.7058303, verbose_name='Comment create time'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='createTime',
            field=models.FloatField(default=1497623880.7041247, verbose_name='Post create time'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='lastMessTime',
            field=models.FloatField(default=1497623880.7042203, verbose_name='Last messege time'),
        ),
    ]
