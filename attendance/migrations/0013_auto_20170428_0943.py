# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20170427_0608'),
        ('attendance', '0012_auto_20170428_0414'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hour',
            unique_together=set([('student', 'created_on', 'code')]),
        ),
    ]
