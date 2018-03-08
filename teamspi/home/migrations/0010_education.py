# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180307_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=500, null=True)),
                ('institution', models.CharField(max_length=600, null=True)),
                ('cgpa', models.FloatField(max_length=3, null=True)),
                ('passing_year', models.CharField(max_length=4, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Member')),
            ],
        ),
    ]