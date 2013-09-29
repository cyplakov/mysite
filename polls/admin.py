# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Poll

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,						{'fields' : ['question']}),
		(u'Дата публикации',		{'fields' : ['pub_date'], 'classes': ['collapse']}),
	]

admin.site.register(Poll, PollAdmin)