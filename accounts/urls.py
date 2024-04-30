from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registeruser/',views.RegisterUser , name='registeruser' ),
    path('login/',views.Login , name='login'),
    path('myAccounts/',views.myAccounts , name='myAccounts'),
    path('userdashboard/',views.UserDashBoard , name='userdashboard'),
    path('vendordashboard/',views.VendorDashBoard , name='vendordashboard'),
    path('logout/',views.Logout , name='logout'),
    path('activate/<uidb64>/<token>/',views.activate , name='activate')
]