# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('experties_percent', models.FloatField(max_length=3, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Member')),
            ],
        ),
    ]
