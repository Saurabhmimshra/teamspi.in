# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import Project, Team, Member
# Create your views here.

# def allProjects(request):
# 	try:
# 		bd = Project.objects.filter(team__name = 'Big Data')
# 		ml = Project.objects.filter(team__name = 'Machine Learning')
# 		java = Project.objects.filter(team__name = 'Java')
# 		cloud = Project.objects.filter(team__name = 'Cloud')
# 		android = Project.objects.filter(team__name = 'Android Deveplopement')
# 		webd = Project.objects.filter(team__name = 'Web Development')
# 	except Team.DoesNotExist:
# 		raise Http404('Invalid Page')

# 	context = 	{
# 					'bd': bd,
# 					'ml': ml,
# 					'java': java,
# 					'cloud': cloud,
# 					'android': android,
# 					'webd' : webd,
# 			  	}
# 	return render(request, 'allprojects.html', context)

def allProjects(request):
	try:
		ob = Team.objects.all()
	except Team.DoesNotExist:
		raise Http404('Invalid Page')



	context = 	{
					'teams':ob,
			  	}
	return render(request, 'allprojects.html', context)




def project(request, project_id):
	try:
		ob = Project.objects.get(pk = project_id)
		members = Member.objects.filter(projects__pk = project_id)
	except Team.DoesNotExist:
		raise Http404('Invalid Page')

	context = 	{
					'project': ob,
					'members': members,
			  	}
	return render(request, 'project.html', context)

