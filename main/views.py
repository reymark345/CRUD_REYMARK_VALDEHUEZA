from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from main.models import (Employee, GranteeList, ValidatedGrants)
import math
from django.db import IntegrityError
from django.core.serializers import serialize

from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd


def data_load(request):
    employee_data = ValidatedGrants.objects.filter().order_by('-id')
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
        item = {
            'household_no': item.household_no,
            'set': item.set,
            'first_name': item.first_name,
            'middle_name': item.middle_name,
            'last_name': item.last_name,
            'extension_name': item.extension_name,
            'province': item.province,
            'municipality': item.municipality,
            'barangay': item.barangay,
            'sex': item.sex,
            'distribution_status': item.distribution_status,
            'date_of_card_release_actual': item.date_of_card_release_actual,
            'client_status': item.client_status,
            'who_released_cash_card': item.who_released_cash_card,
            'date_of_card_release': item.date_of_card_released,
            'cash_card_number': item.cash_card_number,
            'type_id': item.type_id,
            'id_number': item.id_number,
            'income': item.income,
            'member_status': item.member_status,
            'duplicate_name': item.duplicate_name,
            'verified_barangay': item.verified_barangay,
            'physical_cc_presented': item.physical_cc_presented,
            'overall_remarks': item.overall_remarks,
            'eligible': item.eligible
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

# def data_load(request):
#     employee_data = Employee.objects.filter()
#     total = employee_data.count()

#     _start = request.GET.get('start')
#     _length = request.GET.get('length')
#     if _start and _length:
#         start = int(_start)
#         length = int(_length)
#         page = math.ceil(start / length) + 1
#         per_page = length

#         employee_data = employee_data[start:start + length]

#     data = []

#     for item in employee_data:
#         if item.first_name != "Multiple":
#             item = {
#                 'id': item.id,
#                 'first_name': item.first_name,
#                 'last_name': item.last_name,
#             }
#             data.append(item)

#     response = {
#         'data': data,
#         'page': page,
#         'per_page': per_page,
#         'recordsTotal': total,
#         'recordsFiltered': total,
#     }
#     return JsonResponse(response)


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
def household_details(request):
    household_id = request.POST.get('hh_id')
    grantee_list = GranteeList.objects.filter(hh_id=household_id)
    data = []
    for item in grantee_list:
        list = {
            'id': item.id,
            'hh_set': item.hh_set,
            'first_name': item.first_name,
            'middle_name': item.middle_name,
            'last_name': item.last_name,
            'extension_name': item.extension_name,
            'province': item.province,
            'municipality': item.municipality,
            'barangay': item.barangay,
            'sex': item.sex
        }   
        data.append(list)

    try:
        return JsonResponse({'data': data})
    except IntegrityError as e:
        return JsonResponse({'data': 'error'})
    

@csrf_exempt
def validated_details(request):

    HouseholdNumber =  request.POST.get('HouseholdNumber')
    Set = request.POST.get('Set')
    FirstName = request.POST.get('FirstName')
    MiddleName = request.POST.get('MiddleName')
    LastName = request.POST.get('LastName')
    ExtensionName = request.POST.get('ExtensionName')
    Province = request.POST.get('Province')
    Municipality = request.POST.get('Municipality')
    Barangay = request.POST.get('Barangay')
    Sex = request.POST.get('Sex')
    DistributionStatus = request.POST.get('DistributionStatus')
    DateofCardReleasedActual = request.POST.get('DateofCardReleasedActual')
    WhoReleasedTheCard = request.POST.get('WhoReleasedTheCard')
    WhereTheCashCardReleased = request.POST.get('WhereTheCashCardReleased')
    DateofCardReleased = request.POST.get('DateofCardReleased')
    CashCardNumber = request.POST.get('CashCardNumber')
    TypeId = request.POST.get('TypeId')
    IdNumber = request.POST.get('IdNumber')
    ClientStatus = request.POST.get('ClientStatus')
    Income = request.POST.get('Income')
    MemberStatus = request.POST.get('MemberStatus')
    DuplicateName = request.POST.get('DuplicateName')
    VerifiedBarangay = request.POST.get('VerifiedBarangay')
    PhysicalCashCardPresented = request.POST.get('PhysicalCashCardPresented')
    OverallRemarks = request.POST.get('OverallRemarks')
    Eligible = request.POST.get('Eligible')


    validated = ValidatedGrants(household_no=HouseholdNumber,set=Set,first_name=FirstName,middle_name=MiddleName,last_name=LastName,extension_name = ExtensionName,
                                province = Province, municipality = Municipality, barangay = Barangay, sex = Sex, distribution_status= DistributionStatus,
                                date_of_card_release_actual = DateofCardReleasedActual, who_released_cash_card = WhoReleasedTheCard, where_the_cash_card_released = WhereTheCashCardReleased,
                                date_of_card_released=DateofCardReleased,cash_card_number=CashCardNumber,type_id=TypeId,id_number = IdNumber,
                                client_status= ClientStatus,income =Income,member_status=MemberStatus,duplicate_name=DuplicateName,verified_barangay=VerifiedBarangay,
                                physical_cc_presented=PhysicalCashCardPresented,overall_remarks = OverallRemarks, eligible=Eligible)

    
    try:
        validated.save()
        return JsonResponse({'data': Eligible})
    except IntegrityError as e:
        return JsonResponse({'data': 'error'})



@csrf_exempt
def predict_detail(request):
    model = joblib.load('C:\\laragon\\www\\project\\naive_bayes_model.pkl')
    label_encoders = joblib.load('C:\\laragon\\www\\project\\label_encoders.pkl')
    # Get the request data
    client_status = request.POST.get('ClientStatus').upper()
    income = request.POST.get('Income').upper()  
    member_status = request.POST.get('MemberStatus').upper()  
    duplicate_name_in_other_area = request.POST.get('DuplicateName').upper()  
    verified_by_barangay = request.POST.get('VerifiedBarangay').upper() 
    physical_cash_card_presented = request.POST.get('PhysicalCashCardPresented').upper()
    
    # Encode categorical variables
    data = {
        'client_status': [client_status],
        'income': [income],
        'member_status': [member_status],
        'duplicate_name_in_other_area': [duplicate_name_in_other_area],
        'verified_by_barangay': [verified_by_barangay],
        'physical_cash_card_presented': [physical_cash_card_presented]
    }
    df = pd.DataFrame(data)
    for column in df.columns:
        if column in label_encoders:
            df[column] = label_encoders[column].transform(df[column])
    
    # Make predictions
    result = model.predict(df)
    
    # Decode the prediction
    prediction = 'YES' if result[0] == 1 else 'NO'

    print(prediction)
    print("predictionTest")
    return JsonResponse({'data': prediction})

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

def validation(request):
    return render(request, 'validation.html')
    
    
@csrf_exempt
def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect("landing")
