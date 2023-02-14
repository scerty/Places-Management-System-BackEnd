"""
from django.shortcuts import render
from core.models import *
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.





def resturant_list(request):
    restuants=Restaurant.objects.all() #to get all the resturant in our system
    data={'resturants': list(restuants.values())}

    return JsonResponse(data)

def resturant_details(request,pk):
    details=Restaurant.objects.get(pk=pk)
    data={

        'name':details,
        'cover_iamge':details.cover_iamge,
        'avatar':details.avatar,
        'address':details.address,
        'phone':details.phone,
        'website':details.website,
        'Longitude':details.Longitude,
        'latitude':details.latitude,
        'rank':details.rank,
        'Kitchen_type':details.Kitchen_type

          }
    return JsonResponse(data)



   """
