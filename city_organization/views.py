from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Organization, Project, Employee


class IndexView(generic.ListView):
    paginate_by = 10
    model = Organization
    template_name = 'city_organization/organization_list.html'

    def get_queryset(self):
        return Organization.objects.all().order_by('title')


class OrganizationDetailView(generic.DetailView):
    model = Organization
    template_name = 'city_organization/organization_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_count'] = self.object.employee_set.count()
        context['projects_count'] = self.object.project_organization.count()
        context['project_list'] = self.object.project_organization.all()
        return context


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'city_organization/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_employees_count'] = self.object.employees.all().count()
        context['project_employees'] = self.object.employees.all()
        return context


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'city_organization/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = self.object.project_employee_set.all()
        return context
