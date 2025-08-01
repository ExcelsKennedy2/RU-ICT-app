from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hod_or_authorized_officer = models.CharField(max_length=100)
    date_reported = models.DateField()

    def __str__(self):
        return self.name

class User(models.Model):
    """A person or lab using the equipment, tied to a department."""
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users', blank=True, null=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    COMPONENT_TYPES = [
        ('monitor', 'Monitor'),
        ('system_unit', 'System Unit'),
        ('keyboard', 'Keyboard'),
        ('mouse', 'Mouse'),
        # You can add more types here
    ]
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='components', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='components', null=True, blank=True)
    component_type = models.CharField(max_length=20, choices=COMPONENT_TYPES)
    serial_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    status = models.CharField(max_length=50, default="Working", blank=True, null=True)  # e.g., Working, Faulty
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='components', blank=True, null=True)

    def __str__(self):
        return f"{self.component_type} - {self.serial_number}"

class Printer(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='printers')
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, default="Working")

    def __str__(self):
        return f"{self.model} - {self.serial_number}"
