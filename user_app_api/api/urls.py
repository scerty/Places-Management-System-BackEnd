















from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app_api.api.views import *


urlpatterns = [

  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

















#=================================================================================================================================
                #URL                             VIEW                                #TEST1    PERMISSION        #FRONTEND TEST1
#=================================================================================================================================


    path('login/'                                ,obtain_auth_token,name='login'),       #done=0   #permesion=0      #front_cosmized=0
    path('register/'                             ,registration_view,name='register'),    #done=0   #permesion=0      #front_cosmized=0
   # path('logout/'                               ,Logout_view,name='logout'),            #done=0   #permesion=0      #front_cosmized=0
    
#    path('returants_type_list/'                 ,KitchenTypeAV.as_view()),           
#    path('returant/<int:pk>/'                   ,ResturantDetailAV.as_view()),       
#    path('returants/type/<int:pk>/'             ,ResturantByKitchenTypeAV.as_view()),

#==================================================================================================================================
############################################## LOG IN - LOG OUT - REGISTER ########################################################
#==================================================================================================================================





]


