# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180307_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='hobbies_others',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='hobbies_sports',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
