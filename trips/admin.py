from django.contrib import admin

from trips.models import *


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
