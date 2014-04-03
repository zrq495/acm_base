from django.contrib import admin

from contest.models import *


class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest_name', 'identifier')

    class Media:
        js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',
        )

admin.site.register(ContestList)
admin.site.register(Contest, ContestAdmin)