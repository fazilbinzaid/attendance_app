# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hour',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
    ]
