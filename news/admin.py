# coding = utf-8

from django.contrib import admin
from news.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_time', 'update_time', 'display')
    search_fields = ('title',)
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'

    class Media:
        js = (
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',
        )

admin.site.register(News, NewsAdmin)