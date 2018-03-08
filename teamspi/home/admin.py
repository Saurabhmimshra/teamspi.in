# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import *

# Register your models here.

admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)