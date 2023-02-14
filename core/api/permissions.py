from rest_framework import permissions









class AdminOrReadOnly(permissions.IsAdminUser):
   def has_permission(self, request, view):
      admin_permission = bool(request.user and request.user.is_staff)
      return request.method=='GET' or admin_permission      
class ProductReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
          return True

       else:
            return obj.user==request.user
class ResturantReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
          return True

       else:
            return obj.review_user==request.user
class AddProductByResturantMangerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
          return True

       else:
            return obj.resturant_menu_catagory.resturant_menu.resturant.manager==request.user
class AddOfferByResturantMangerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
          return True

       else:
            return obj.product.resturant_menu_catagory.resturant_menu.resturant.manager==request.user
class AddMenuCatagoryByResturantMangerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
          return True

       else:
            return obj.resturant_menu.resturant.manager==request.user