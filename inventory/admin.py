from django.contrib import admin
from .models import Department, User, Component, Printer

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod_or_authorized_officer', 'date_reported')
    search_fields = ('name', 'hod_or_authorized_officer')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name',)
    list_filter = ('department',)

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('component_type', 'serial_number', 'status', 'user')
    search_fields = ('serial_number',)
    list_filter = ('component_type', 'status')

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('model', 'serial_number', 'status', 'department')
    search_fields = ('serial_number', 'model')
    list_filter = ('department', 'status')
