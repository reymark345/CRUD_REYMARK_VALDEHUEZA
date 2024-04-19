from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import (AuthUser,Employee)
import math
from django.db import IntegrityError
from django.core.serializers import serialize


def data_load(request):
    # charges_data = Employee.objects.select_related().order_by('-created_at').reverse()
    employee_data = Employee.objects.filter()
    total = employee_data.count()

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1
        per_page = length

        employee_data = employee_data[start:start + length]

    data = []

    for item in employee_data:
        if item.first_name != "Multiple":
            item = {
                'id': item.id,
                'first_name': item.first_name,
                'last_name': item.last_name,
            }
            data.append(item)

    response = {
        'data': data,
        'page': page,
        'per_page': per_page,
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)


@csrf_exempt
def employee_update(request):
    id = request.POST.get('ItemID')
    fname = request.POST.get('FirstName')
    lname = request.POST.get('LastName')

    if Employee.objects.filter(first_name=fname, last_name=lname).exclude(id=id):
        return JsonResponse({'data': 'error', 'message': 'Duplicate Employee'})
    else:
        Employee.objects.filter(id=id).update(first_name=fname,last_name=lname)
        return JsonResponse({'data': 'success'})
    
@csrf_exempt
def employee_add(request):
    fname = request.POST.get('FirstName')
    lname = request.POST.get('LastName')
    employee_add = Employee(first_name=fname,last_name=lname)
    try:
        employee_add.save()
        return JsonResponse({'data': 'success'})
    except IntegrityError as e:
        return JsonResponse({'data': 'error'})
    
@csrf_exempt
def employee_detail(request):
    id = request.GET.get('id')
    items = Employee.objects.get(pk=id)
    data = serialize("json", [items])
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def employee_delete(request):
    id = request.POST.get('id')
    employee = Employee.objects.filter(id=id)
    employee.delete()
    return JsonResponse({'data': 'success'})


def index(request):
    return redirect("crud")
    
def crud(request):
    return render(request, 'crud.html')
    
    
@csrf_exempt
def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect("landing")
