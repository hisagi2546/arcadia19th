# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0013_auto_20170917_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='delflag',
            field=models.IntegerField(default=0),
        ),
    ]
