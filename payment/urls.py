from django.contrib import admin
from django.urls import path
from payment import views
 
urlpatterns = [
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('admin/', admin.site.urls),
]