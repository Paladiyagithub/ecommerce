from django.urls import path
from marketplace import views

urlpatterns = [
    path('marketplace/',views.market_view , name='marketplace' ),
    path('restaurantmenu/<slug:slug>/',views.Restaurant_menu , name='restaurantmenu' ),
    path('add_cart/<int:pk>/<slug:details_id>',views.Add_To_Cart , name='add_cart' ),
    path('remove_cart/<int:pk>/<slug:details_id>',views.Remove_Cart , name='remove_cart' ),
    path('cart',views.Cart , name='cart'),
]