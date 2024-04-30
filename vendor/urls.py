from django.urls import path
from accounts import views as aviews
from vendor import views
urlpatterns = [
    path('registerRestaurant/',aviews.registerRestaurant , name='registerRestaurant' ),
    path('vendorprofile/',views.VendorProfile , name='vendorprofile' ),
]