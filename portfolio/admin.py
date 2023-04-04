from django.contrib import admin
from .models import Project


# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'description', 'image', 'url', )


admin.site.register(Project)
