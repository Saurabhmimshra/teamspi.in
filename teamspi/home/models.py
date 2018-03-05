# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Member(models.Model):
	name = models.CharField(max_length=100)
	team = models.ManyToManyField(Team)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=500)
	description = models.CharField(max_length= 1000)

	def __str__(self):
		return self.title