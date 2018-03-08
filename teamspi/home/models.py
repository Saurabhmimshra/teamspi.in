# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Team(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=500)
	description = models.CharField(max_length= 1000)


	def __str__(self):
		return self.title


	
		

class Member(models.Model):
	photo = models.ImageField(upload_to = 'members_photo/', blank=True)
	name = models.CharField(max_length=100,null=True)
	tag = models.CharField(max_length = 100,null=True)
	team = models.ManyToManyField(Team)
	introduction = models.CharField(max_length = 1000,null=True)
	projects = models.ManyToManyField(Project)
	association = models.CharField(max_length = 500,null=True)
	email = models.EmailField(max_length = 200,null=True)
	phone = models.CharField(max_length = 10,null=True)
	website = models.CharField(max_length = 500, null=True)
	blog = models.CharField(max_length = 500, null = True)
	hobbies_sports = models.CharField(max_length = 100, null= True)
	hobbies_others = models.CharField(max_length = 200, null= True)



	def __str__(self):
		return self.name + " : " + self.email


# class Secondary_education(models.model):
# 	school = models.CharField(max_length=600, null=true)
# 	cgpa = models.FloatField(max_length=3, null=True)
# 	passing_year = models.CharField(max_length = 4, null=True)

# class sr_sec_education(models.model):
# 	type = models.CharField(max_length = )
# 	school = models.CharField(max_length=600, null=true)
# 	cgpa = models.FloatField(max_length=3, null=True)
# 	passing_year = models.CharField(max_length = 4, null=True)


class Education(models.Model):
	member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
	course = models.CharField(max_length =500, null=True)
	institution = models.CharField(max_length=600, null=True)
	percentage = models.FloatField(max_length=3, null=True)
	passing_year = models.CharField(max_length = 4, null=True)

	def __str__(self):
		return self.member.name + " : " + self.course

class Experience(models.Model):
	member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
	company = models.CharField(max_length = 500, null=True)
	profile = models.CharField(max_length = 500, null=True)
	duration = models.CharField(max_length = 100, null=True)
	description = models.CharField(max_length = 1000, null=True)

class Skill(models.Model):
	member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
    )
	name = models.CharField(max_length=100, null=True)
	experties_percent = models.FloatField(max_length=3, null=True)