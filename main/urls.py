from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('data_load', views.data_load, name='data_load'),
    path('employee_update', views.employee_update, name='employee-update'),
    path('employee_add', views.employee_add, name='employee-add'),
    path('employee_detail', views.employee_detail, name='employee-detail'),
    path('employee_delete', views.employee_delete, name='employee-delete'),
]
