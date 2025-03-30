from django.contrib import admin
from .models import Tool, ProjectList,  MyProjects

admin.site.register(Tool)
admin.site.register(ProjectList)


class MyProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'get_project_type')

admin.site.register(MyProjects, MyProjectsAdmin)