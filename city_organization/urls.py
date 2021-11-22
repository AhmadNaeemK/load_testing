from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(),
         name='index'),
    path('organization/<int:pk>', views.OrganizationDetailView.as_view(),
         name='organization_detail'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(),
         name='project_detail'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(),
         name='delete'),
]
