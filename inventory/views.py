from django.shortcuts import render, get_object_or_404
from .models import Department, Printer, User, Component

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'inventory/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    users = department.users.all()
    printers = department.printers.all()

    # Unassigned components: No user, but still relevant to department
    # This assumes components must be related through users
    unassigned_components = Component.objects.filter(user__isnull=True)

    context = {
        'department': department,
        'users': users,
        'printers': printers,
        'unassigned_components': unassigned_components,
    }
    return render(request, 'inventory/department_detail.html', context)


from django.shortcuts import redirect
from .forms import DepartmentForm, UserForm, ComponentForm, PrinterForm

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:department_list')
    else:
        form = DepartmentForm()
    return render(request, 'inventory/add_department.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:department_list')
    else:
        form = UserForm()
    return render(request, 'inventory/add_user.html', {'form': form})

def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:department_list')
    else:
        form = ComponentForm()
    return render(request, 'inventory/add_component.html', {'form': form})


def add_printer(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:department_list')
    else:
        form = PrinterForm()
    return render(request, 'inventory/add_printer.html', {'form': form})

# views.py

from .forms import ComponentForm

def edit_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            messages.success(request, "Component updated successfully.")
            return redirect('inventory:department_detail', pk=component.user.department.pk if component.user else 1)  # fallback
    else:
        form = ComponentForm(instance=component)
    return render(request, 'inventory/edit_component.html', {'form': form})

def delete_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'POST':
        component.delete()
        messages.success(request, "Component deleted successfully.")
        return redirect('inventory:department_detail', pk=component.user.department.pk if component.user else 1)
    return render(request, 'inventory/delete_component_confirm.html', {'component': component})


from .forms import DepartmentForm
from django.contrib import messages

def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully.")
            return redirect('inventory:department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'inventory/edit_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, "Department deleted successfully.")
        return redirect('inventory:department_list')
    return render(request, 'inventory/delete_department_confirm.html', {'department': department})

from .forms import UserForm

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('inventory:department_detail', pk=user.department.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'inventory/edit_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        department_pk = user.department.pk
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('inventory:department_detail', pk=department_pk)
    return render(request, 'inventory/delete_user_confirm.html', {'user': user})

from .forms import PrinterForm

def edit_printer(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            messages.success(request, "Printer updated successfully.")
            return redirect('inventory:department_detail', pk=printer.user.department.pk if printer.user else 1)
    else:
        form = PrinterForm(instance=printer)
    return render(request, 'inventory/edit_printer.html', {'form': form})

def delete_printer(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        department_pk = printer.user.department.pk if printer.user else 1
        printer.delete()
        messages.success(request, "Printer deleted successfully.")
        return redirect('inventory:department_detail', pk=department_pk)
    return render(request, 'inventory/delete_printer_confirm.html', {'printer': printer})
