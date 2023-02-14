from rest_framework import serializers
from core.models import ( 
MenuCatgory,
Offer,
Restaurant,
KitchenType ,
ResturantReview ,
ProductReview,
Menu,
Product
)


class ProductReviewSerializer(serializers.ModelSerializer):
  user=serializers.StringRelatedField(read_only=True)
  class Meta:
    model=ProductReview  
    exclude=('product',)  
class ProductSerializer(serializers.ModelSerializer):
  reviews=ProductReviewSerializer(many=True,read_only=True)
  user=serializers.StringRelatedField(read_only=True) #TODO maby proplem here
  class Meta:  
    model=Product
    exclude=('resturant_menu_catagory',)
class MenuCatgorySerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=MenuCatgory
       # fields="__all__"
        exclude=('resturant_menu',)
class MenuSerializer(serializers.ModelSerializer):    
   # menuserializer=serializers.StringRelatedField(read_only=True)
    menu_catagories=MenuCatgorySerializer(many=True,read_only=True)
    
    class Meta:
        model=Menu
        fields="__all__"
class ResturantReviewSerializer(serializers.ModelSerializer):
  review_user=serializers.StringRelatedField(read_only=True)

  class Meta:  
    model=ResturantReview
    exclude=('restaurant',)
class ResturantSerializer(serializers.ModelSerializer):
    reviews=ResturantReviewSerializer(many=True,read_only=True)
    menu=MenuSerializer(read_only=True)

    class Meta:
        model=Restaurant
        fields="__all__"
class ResturantBKSerializer(serializers.ModelSerializer):
     
    class Meta:
        model=Restaurant
        exclude=("website","cover_iamge", "trip_advisor","rank","manager") 
class KitchenTypeSerializer(serializers.ModelSerializer):
    resturant=ResturantSerializer(many=True,read_only=True)
  #  restu333rant=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=KitchenType
        fields="__all__"
class OfferSerializer(serializers.ModelSerializer):

  class Meta:
        model=Offer
        fields="__all__"









