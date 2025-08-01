from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('add/department/', views.add_department, name='add_department'),
    path('add/user/', views.add_user, name='add_user'),
    path('add/component/', views.add_component, name='add_component'),
    path('add/printer/', views.add_printer, name='add_printer'),
    path('department/<int:pk>/edit/', views.edit_department, name='edit_department'),
    path('department/<int:pk>/delete/', views.delete_department, name='delete_department'),

    path('user/<int:pk>/edit/', views.edit_user, name='edit_user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete_user'),

    path('component/<int:pk>/edit/', views.edit_component, name='edit_component'),
    path('component/<int:pk>/delete/', views.delete_component, name='delete_component'),

    path('printer/<int:pk>/edit/', views.edit_printer, name='edit_printer'),
    path('printer/<int:pk>/delete/', views.delete_printer, name='delete_printer'),
]
