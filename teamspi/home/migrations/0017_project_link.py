# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_project_snap'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
