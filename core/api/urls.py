
from django.urls import path ,include
import core.urls
from core.api.views import  *




urlpatterns = [
#=================================================================================================================================
                #URL                             VIEW                                #TEST1    PERMISSION        #FRONTEND TEST1
#=================================================================================================================================
    path('returants_list/'                      ,ResturantAV.as_view()),             #done=1   #permesion=       #front_cosmized=0
    path('returants_type_list/'                 ,KitchenTypeAV.as_view()),           #done=1   #permesion=       #front_cosmized=0
    path('returant/<int:pk>/'                   ,ResturantDetailAV.as_view()),       #done=1   #permesion=       #front_cosmized=0
    path('returants/type/<int:pk>/'             ,ResturantByKitchenTypeAV.as_view()),#done=1   #permesion=       #front_cosmized=0
#----------------------------------------------------------------------------------------------------------------------------------
    path('resturant/<int:pk>/review'            ,ResturantReviewList.as_view()),                         
    path('resturant/<int:pk>/review-create'     ,ResturantReviewCreate.as_view()),   #done=1   #permesion=1       #front_cosmized=0     
    path('resturant/review/<int:pk>'            ,ResturantReviewDetails.as_view()),  #done=1   #permesion=1       #front_cosmized=0 
#----------------------------------------------------------------------------------------------------------------------------------
    path('product/<int:pk>/review'              ,ProductReviewList.as_view()),       #done=1   #permesion=        #front_cosmized=0
    path('product/<int:pk>/review-create'       ,ProductReviewCreate.as_view()),     #done=1   #permesion=1       #front_cosmized=0
    path('product/review/<int:pk>'              ,ProductReviewDetails.as_view()),    #done=1   #permesion=1       #front_cosmized=0
#----------------------------------------------------------------------------------------------------------------------------------
    path('menu/catagory/<int:pk>'               ,MenuCatgoryDetails.as_view()),      #done=1   #permesion=1       #front_cosmized=0
    path('menu/<int:pk>/catagories'             ,MenuCatgoryList.as_view()),         #done=1   #permesion=0       #front_cosmized=0
    path('menu_catagory/<int:pk>/product'       ,ProductList.as_view()),             #done=1   #permesion=0       #front_cosmized=0
    path('menu_catagory/<int:pk>/product-create',ProductCreate.as_view()),           #done=1   #permesion=#TODO   #front_cosmized=0
    path('menu_catagory/product/<int:pk>'       ,ProductDetails.as_view()),          #done=1   #permesion=1       #front_cosmized=0
#----------------------------------------------------------------------------------------------------------------------------------
    path('offer/<int:pk>'                       ,OfferDetail.as_view()),             #done=1   #permesion=1       #front_cosmized=0
   #TODO BETA Offer create 
    path('offers/'                              ,OfferList.as_view()),              #done=1   #permesion=0        #front_cosmized=0
#==================================================================================================================================





]


