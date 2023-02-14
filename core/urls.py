"""
from django.urls import path ,include
import core.urls
from core.views import  *

urlpatterns = [

    path('returants_list/',resturant_list.as_view()),
    path('<int:pk>/',resturant_details.as_view())

]
"""