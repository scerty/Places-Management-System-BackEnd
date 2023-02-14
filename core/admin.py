from django.contrib import admin
from .models import *






admin.site.register(Restaurant)
admin.site.register(KitchenType)
admin.site.register(ResturantReview)

admin.site.register(Menu)
admin.site.register(MenuCatgory)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(ProductReview)
admin.site.register(Offer)
admin.site.register(OfferUnit)
