# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from .forms import ContactForm

from django.shortcuts import render

from home.models import Team, Member, Project
# Create your views here.

def index(request):
	form_class = ContactForm
	error = ''
	msg = ''
	if request.method == 'POST':

		form = form_class(data=request.POST)
		print(form.errors)
		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			}
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"TeamSPI.in" +'',
				['saurabhmimshra@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			msg = "Your response has been saved."

		else:

			error = form.errors

	context = 	{ 
					'first_project' : Project.objects.get(title = "Sell My Books"), 
					'second_project' : Project.objects.get(title = 'Noteshub'),
					'android' : Team.objects.get(name = 'Android Deveplopement'),
					'webd' : Team.objects.get(name = 'Web Development'),
					'cloud' : Team.objects.get(name = 'Cloud'),
					'java' : Team.objects.get(name = 'Java'),
					'ml' : Team.objects.get(name = 'Machine Learning'),
					'bd': Team.objects.get(name = 'Big Data'),
					'form': form_class,
					'error': error,
					'msg' : msg,

		 		}	
	return render(request, 'index.html', context)

# def contact(request):
#     form_class = ContactForm

#     return render(request, 'index.html', {
#         'form': form_class,
#     })
