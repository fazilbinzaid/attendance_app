# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170425_0740'),
        ('attendance', '0003_auto_20170425_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjecthourmapping',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='subjecthourmapping',
            name='subject',
        ),
        migrations.AddField(
            model_name='hour',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='attendance.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='hour',
            unique_together=set([('student', 'date', 'code')]),
        ),
        migrations.DeleteModel(
            name='SubjectHourMapping',
        ),
    ]