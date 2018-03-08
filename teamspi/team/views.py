# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import Project, Team, Member 
# Create your views here.

def team(request, team_id):
	try:
		ob = Team.objects.get(pk = team_id)
	except Team.DoesNotExist:
		raise Http404('Team does not exit')

	members = Member.objects.filter(team__pk = team_id)

	context = 	{
					'team': ob,
					'members': members,
			  	}
	return render(request, 'team.html', context)

