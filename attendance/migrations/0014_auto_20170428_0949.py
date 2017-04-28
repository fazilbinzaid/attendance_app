# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20170427_0608'),
        ('attendance', '0013_auto_20170428_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='hour',
            unique_together=set([('student', 'date', 'code')]),
        ),
    ]