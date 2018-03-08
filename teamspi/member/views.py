# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404

from home.models import Team, Member, Project, Education, Experience, Skill

# Create your views here.
def member(request, member_id):
	
	try:
		ob = Member.objects.get(pk=member_id)
		ob_ed = Education.objects.filter(member__pk = member_id)
		ob_ex = Experience.objects.filter(member__pk = member_id)
		ob_sk = Skill.objects.filter(member__pk = member_id)
	except Member.DoesNotExist:
		raise Http404('Member does not exit')


	context = 	{
					'member': ob,
					'education': ob_ed,
					'experience': ob_ex,
					'skills': ob_sk,
			  	}
	return render(request, 'member.html', context)

