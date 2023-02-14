from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
import random




class KitchenType(models.Model):
    name=models.CharField(max_length=200)
    icon=models.CharField(max_length=200, null=True)
    image=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    #TODO alpha likes and target

    avatar = models.CharField(max_length=10000, null=True) #
    cover_iamge=models.CharField(max_length=1000, null=True)
    manager=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)                          #
    name = models.CharField(max_length=200)                                                #
    address = models.CharField(max_length=200)                                             #
    phone = models.CharField(max_length=200, null=True)                                               #
    website = models.CharField(max_length=200, null=True)                                             #
    wolt_profile=models.CharField(max_length=200, null=True)                                          #
    fodoora_profile=models.CharField(max_length=200, null=True)   
    trip_advisor=models.CharField(max_length=200, null=True)                                    #
    Longitude=models.DecimalField(max_digits=12, decimal_places=10)                                                        #
    latitude=models.DecimalField(max_digits=12, decimal_places=10)  
                                                           #
    rank=models.DecimalField(max_digits=2, decimal_places=1)
    booking=models.BooleanField(default=False,null=True)


    avg_rating=models.FloatField(default=0)
    number_of_rating=models.PositiveIntegerField(default=0)

    Kitchen_type=models.ManyToManyField(KitchenType, null=True,related_name="kitchentype")                                                  #class

    def __str__(self):
        return self.name
class ResturantReview(models.Model):
    #TODO alpha likes 
    review_user=models.ForeignKey(User,on_delete=models.CASCADE ,default=1)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="reviews") #TODO here i am working now
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=200,null=True)
   # product=models.ForeignKey(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activ=models.BooleanField(default=True)
    
    def __str__(self):
        return self.review_user.first_name +" : "+ self.comment
class Menu(models.Model):

    cover_image=models.CharField(max_length=500,null=True)
    desc=models.CharField(max_length=500,null=True)
    resturant=models.OneToOneField(Restaurant,on_delete=models.CASCADE)
class MenuCatgory(models.Model):
    name=models.CharField(max_length=50,null=True)
    cover_image=models.CharField(max_length=500,null=True)
    desc=models.CharField(max_length=500)
    resturant_menu=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="menu_catagories")
    activ=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Categories(models.Model):
    name=models.CharField(max_length=200)
    icon=models.CharField(max_length=200, null=True)
    image=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    activ=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=255) #
    rank=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])#
    image = models.CharField(max_length=255,default='https://images.pexels.com/photos/376464/pexels-photo-376464.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')#
    icon=models.CharField(max_length=225)#
    description = models.TextField(max_length=1000, null=True)#
    price = models.DecimalField(max_digits=10, decimal_places=2)#

   # category=models.ForeignKey(Categories)
   # ingredients=models.ManyToManyField()
    kitchen_type=models.ManyToManyField(KitchenType)
    resturant_menu_catagory=models.ForeignKey(MenuCatgory,on_delete=models.CASCADE,related_name="product")

    avg_rating=models.FloatField(default=0)
    number_of_rating=models.PositiveIntegerField(default=0)
    
    calories=models.DecimalField(max_digits=10, decimal_places=2)
    is_vegan=models.BooleanField(default=False ,null=True)
    is_vigetar=models.BooleanField(default=False ,null=True)
    is_halal=models.BooleanField(default=False ,null=True)
    contains_pork=models.BooleanField(default=False ,null=True)
    gluten_free=models.BooleanField(default=False ,null=True)
    #TODO add ingredints here or try to find another way to fix this iisue 
   # can_be_halal=models.BooleanField(default=False ,null=True)
    can_be_gluten_free=models.BooleanField(default=False ,null=True)
    organic=models.BooleanField(default=False ,null=True)
    activ=models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Ingredient(models.Model):
    food = models.ManyToManyField(Product)
    name = models.CharField(max_length=200)
    activ=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   #TODO likes=models.PositiveIntegerField()
    rank=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])#TODO V1 TARGET RANK
    comment=models.CharField(max_length=200,null=True)
    product=models.ForeignKey(Product ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activ=models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name+" :  "+self.comment
class Offer(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    percentage=models.PositiveSmallIntegerField()
    Longitude=models.DecimalField(max_digits=12, decimal_places=10)                                                        #
    latitude=models.DecimalField(max_digits=12, decimal_places=10)
    ofer_start=models.DateTimeField() ####
    ofer_end=models.DateTimeField() #TODO handling erors when start date after the end date
   # qr=models.PositiveIntegerField(max_digits=10)
    activ=models.BooleanField(default=True)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.name
class OfferUnit(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Offer=models.ForeignKey(Offer,on_delete=models.CASCADE ,null=True)
    #TODO make another end date

    def __str__(self):
        return self.user.first_name+" "+self.Offer.product.title




























#TODO V2 in version2 we will create ingredents profesional classes 












