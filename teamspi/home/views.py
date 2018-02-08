# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import Team, Member, Project
# Create your views here.

def index(request):
	context = 	{ 
					'first_project' : Project.objects.get(title = "Sell My Books"), 
					'second_project' : Project.objects.get(title = 'Noteshub'),
		 		}	
	return render(request, 'index.html', context)
