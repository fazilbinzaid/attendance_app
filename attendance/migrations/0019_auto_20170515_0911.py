# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_tag_taglevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='supertag',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]