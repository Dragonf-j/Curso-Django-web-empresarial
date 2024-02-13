from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields =  ('created', 'update')

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="personal"):
            return ('created', 'update', 'key', 'name')
        else:
            return ('created', 'update')
admin.site.register(Link, LinkAdmin)