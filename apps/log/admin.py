# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Entry, Provider


admin.site.register(Entry, admin.ModelAdmin)
admin.site.register(Provider, admin.ModelAdmin)