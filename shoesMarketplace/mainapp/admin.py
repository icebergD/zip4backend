from django.contrib import admin

from .models import *

class ImageDisabledAdmin(admin.ModelAdmin):
    readonly_fields = ('descriptor', 'histogram')

admin.site.register(ImageShoe, ImageDisabledAdmin)

admin.site.register(Market)
admin.site.register(Shoe)
