# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0009_auto_20170913_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='user',
            field=models.CharField(max_length=200, verbose_name='ユーザ名'),
        ),
    ]