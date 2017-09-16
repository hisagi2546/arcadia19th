# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 21:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0013_remark_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='user_id',
            field=models.ForeignKey(default='system', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
