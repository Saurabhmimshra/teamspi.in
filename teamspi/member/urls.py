from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<member_id>[0-9]+)$', views.member, name='member'),
]