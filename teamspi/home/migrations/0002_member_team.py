# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ManyToManyField(to='home.Team'),
        ),
    ]
