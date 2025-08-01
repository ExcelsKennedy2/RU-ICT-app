from django import forms
from .models import Department, User, Component, Printer

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'date_reported': forms.DateInput(attrs={'type': 'date'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'
