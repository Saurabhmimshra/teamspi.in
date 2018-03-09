from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.allProjects, name='allProjects'),
	url(r'^(?P<project_id>[0-9]+)$', views.project, name='project'),
]