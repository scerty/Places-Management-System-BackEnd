from django.shortcuts import render
from core.models import *
from rest_framework.views import APIView 
from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .serializers import OfferSerializer, ProductSerializer, ResturantBKSerializer, ResturantSerializer,MenuCatgorySerializer ,KitchenTypeSerializer ,ResturantReviewSerializer ,ProductReviewSerializer
from rest_framework import generics ,mixins , views
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import AddMenuCatagoryByResturantMangerOrReadOnly, AddOfferByResturantMangerOrReadOnly, AddProductByResturantMangerOrReadOnly, AdminOrReadOnly, ProductReviewUserOrReadOnly, ResturantReviewUserOrReadOnly 


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse






class ProductList(generics.ListAPIView):
    serializer_class=ProductSerializer
    # queryset = ResturantReview.objects.all()

    def get_queryset(self):
       pk = self.kwargs['pk']
       #TODO V1 IMPORTNANT try to get ingredints information when you geting product details
       return Product.objects.filter(resturant_menu_catagory=pk)
class MenuCatgoryList(generics.ListAPIView):
    serializer_class=MenuCatgorySerializer
    # queryset = ResturantReview.objects.all()

    def get_queryset(self):
       pk = self.kwargs['pk']
       return MenuCatgory.objects.filter(resturant_menu=pk)
class MenuCatgoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=MenuCatgory.objects.all()
    serializer_class=MenuCatgorySerializer
    permission_classes=[AddMenuCatagoryByResturantMangerOrReadOnly]
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer 
    permission_classes=[AddProductByResturantMangerOrReadOnly]
class ProductCreate(generics.CreateAPIView):
    serializer_class=ProductSerializer

    permission_classes=[AddProductByResturantMangerOrReadOnly]


    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        resturant_menu_catagory=MenuCatgory.objects.get(pk=pk)
        serializer.save(resturant_menu_catagory=resturant_menu_catagory)
class ProductReviewList(generics.ListAPIView):
    serializer_class=ProductReviewSerializer
    # queryset = ResturantReview.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get_queryset(self):
       pk = self.kwargs['pk']
       return ProductReview.objects.filter(product=pk)
class ProductReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductReview.objects.all()
    serializer_class=ProductReviewSerializer
    permission_classes=[ProductReviewUserOrReadOnly]
class ProductReviewCreate(generics.CreateAPIView):
    serializer_class=ProductReviewSerializer
    def get_queryset(self):
        return ProductReview.objects.all()
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        product=Product.objects.get(pk=pk)


        user=self.request.user
        review_queryset= ProductReview.objects.filter(product=product,user=user)

        if review_queryset.exists():
            raise ValidationError('you have alredy reviewed this product!')

        if product.number_of_rating ==0:
            product.avg_rating = serializer.validated_data['rank']
        else:
            product.avg_rating =(product.avg_rating +serializer.validated_data['rank'] )/2


        product.number_of_rating=product.number_of_rating+1
        product.save()    
        serializer.save(product=product,user=user)
class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Offer.objects.all()
    serializer_class=OfferSerializer
    permission_classes=[AddOfferByResturantMangerOrReadOnly]
class OfferList(generics.ListAPIView):
    serializer_class=OfferSerializer
   
    def get_queryset(self):
      
       return Offer.objects.all()
class ResturantReviewList(generics.ListAPIView):
    serializer_class=ResturantReviewSerializer
    # queryset = ResturantReview.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
       pk = self.kwargs['pk']
       return ResturantReview.objects.filter(restaurant=pk)
class ResturantReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ResturantReview.objects.all()
    serializer_class=ResturantReviewSerializer
    permission_classes=[ResturantReviewUserOrReadOnly]
class ResturantReviewCreate(generics.CreateAPIView):
    serializer_class=ResturantReviewSerializer
    def get_queryset(self):
        return ResturantReview.objects.all()
    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        restaurant=Restaurant.objects.get(pk=pk)

        review_user=self.request.user

        review_queryset= ResturantReview.objects.filter(restaurant=restaurant,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError('you have alredy reviewed this resturant!')
        
        if restaurant.number_of_rating ==0:
            restaurant.avg_rating = serializer.validated_data['rating']
        else:
            restaurant.avg_rating =(restaurant.avg_rating +serializer.validated_data['rating'] )/2


        restaurant.number_of_rating=restaurant.number_of_rating+1
        restaurant.save()

        serializer.save(restaurant=restaurant,review_user=review_user)
class ResturantAV(APIView):
    def get(self,request):
        resturants=Restaurant.objects.all() #to get all the resturant in our system
        serializer=ResturantBKSerializer(resturants,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ResturantBKSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             return Response(serializer.errors)

@method_decorator(csrf_exempt, name='dispatch')            
class ResturantDetailAV(APIView):
#------------------------------------------------------------------------------------------------
    def get(self,requeset,pk):
        try:
           resturant=Restaurant.objects.get(pk=pk) 
        except Restaurant.DoesNotExist:
            return Response ({'Eroror':'Resturant not faound!'},status=status.HTTP_404_NOT_FOUND)

        serializer=ResturantSerializer(resturant)
        return Response(serializer.data)
#------------------------------------------------------------------------------------------------
    def put(self,request,pk):
       try:
           resturant=Restaurant.objects.get(pk=pk) 
       except Restaurant.DoesNotExist:
            return Response ({'Eroror':'Resturant not faound!'},status=status.HTTP_404_NOT_FOUND)
       serializer=ResturantSerializer(resturant,data=request.data)
       if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status.HTTP_200_OK)
       else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#------------------------------------------------------------------------------------------------
    def delete(self,request,pk):
        try:
           resturant=Restaurant.objects.get(pk=pk) 
        except Restaurant.DoesNotExist:
            return Response ({'Eroror':'Can not delete. the Resturant is not found!'},status=status.HTTP_404_NOT_FOUND)
        resturant.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)
class ResturantByKitchenTypeAV(APIView):
    def get(self,requeset,pk):
            resturants = Restaurant.objects.filter(Kitchen_type=pk)
            if resturants.count() > 1:
                # Return the entire queryset using the serializer
                serializer = ResturantBKSerializer(resturants, many=True)
                return Response(serializer.data)
            elif resturants.count() == 1:
                # Retrieve the first object in the queryset
                resturant = resturants.first()
                serializer = ResturantBKSerializer(resturant)
                return Response(serializer.data)
            else:
                return Response ({'Error': 'this type of resturant not found!'}, status=status.HTTP_404_NOT_FOUND)
class KitchenTypeAV(APIView): #this class can edit by superadmin only.
    def get(self,request):
        k_types=KitchenType.objects.all() #to get all the resturant in our system
        serializer=KitchenTypeSerializer(k_types,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=KitchenTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             return Response(serializer.errors)    






















#TODO BETA try to display pruduct name and product images with list response















