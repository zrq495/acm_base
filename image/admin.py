from django.contrib import admin
from image.models import *

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name',)

admin.site.register(Image, ImageAdmin)