# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import Team, Member, Project 

# Create your views here.
def member(request, member_id):
	context = 	{
					'member_id'  : member_id,			
			  	}
	return render(request, 'member.html', context)

