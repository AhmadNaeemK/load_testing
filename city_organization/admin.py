from django.contrib import admin

from .models import Organization, Project, Employee


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'ceo_name')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'organization')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Employee, EmployeeAdmin)
