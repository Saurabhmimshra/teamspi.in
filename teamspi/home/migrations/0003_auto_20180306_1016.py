# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_member_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='association',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='hobbies',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='introduction',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='projects',
            field=models.ManyToManyField(to='home.Project'),
        ),
        migrations.AddField(
            model_name='member',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
