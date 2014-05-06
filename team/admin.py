from django.contrib import admin
from team.models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_identifier', 'team_year')

    class Media:
        js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',
        )


class TeamListAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_identifier')

admin.site.register(TeamList, TeamListAdmin)
admin.site.register(Team, TeamAdmin)
