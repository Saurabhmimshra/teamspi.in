# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import Team, Member, Project
# Create your views here.

def index(request):

	context = 	{ 
					'first_project' : Project.objects.get(title = "Sell My Books"), 
					'second_project' : Project.objects.get(title = 'Noteshub'),
					'android' : Team.objects.get(name = 'Android Deveplopement'),
					'webd' : Team.objects.get(name = 'Web Development'),
					'cloud' : Team.objects.get(name = 'Coud'),
					'java' : Team.objects.get(name = 'Java'),
					'ml' : Team.objects.get(name = 'Machine Learning'),
					'bd': Team.objects.get(name = 'Big Data'),

		 		}	
	return render(request, 'index.html', context)

