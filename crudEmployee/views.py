
from django.contrib import messages
from django.shortcuts import render
from .models import crudEmployee
from crudEmployee.forms import EmpForms
# Create your views here.


def showEmployee(request):
    emps = crudEmployee.objects.all()
    return render(request, 'index.html', {"emps": emps})


def insertEmployee(request):
    if request.method == "POST":
        if request.POST.get('emp_name') != '' and request.POST.get('emp_age') != '' and request.POST.get('emp_phone') != '' and request.POST.get('gender') != '' and request.POST.get('salary') != '':
            model = crudEmployee()
            model.emp_name = request.POST.get('emp_name')
            model.emp_age = request.POST.get('emp_age')
            model.emp_phone = request.POST.get('emp_phone')
            model.gender = request.POST.get('gender')
            model.salary = request.POST.get('salary')
            model.save()
            messages.success(request, 'Employee ' +
                             model.emp_name+' inserted successfully!!')
            return render(request, 'insert.html', {"color": 'green'})
        else:
            print('not fulfilled')
            messages.success(
                request, 'Employee record not inserted -> failed !!')
            return render(request, 'insert.html', {"color": 'red'})
    else:
        print('get')
        return render(request, 'insert.html')


def updateEmployee(request, id):
    emp = crudEmployee.objects.get(id=id)
    return render(request, 'edit.html', {'emp': emp})


def updateform(request, id):
    updateemp = crudEmployee.objects.get(id=id)
    form = EmpForms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully!!')
        return render(request, 'edit.html', {"emp": updateemp, "color": 'green'})
    else:
        messages.warning(request, 'failed to update employee record!!')
        return render(request, 'edit.html', {'emp': updateemp, "color": 'red'})


def deleteEmployee(request, id):
    emp = crudEmployee.objects.get(id=id)
    emp.delete()
    showemp = crudEmployee.objects.all()
    return render(request, 'index.html', {"emps": showemp})
