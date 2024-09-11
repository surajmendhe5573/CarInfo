from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse

# Create your views here.

def car_list_view(request):
    cars= Carlist.objects.all()
    data= {'cars': list(cars.values())}
    return JsonResponse(data)