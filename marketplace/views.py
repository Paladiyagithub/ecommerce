from django.shortcuts import render , get_object_or_404 ,redirect
from vendor.models import Vendor
from accounts.models import UserProfile
from menu.models import Category,FoodItem
from django.db.models import Prefetch
from .models import Add_Card
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

def market_view(request):
    if 'S' in request.GET:
        S = request.GET['S']
        print(S)
        vendor = Vendor.objects.filter(Restaurant_name__icontains=S, is_approved=True, user__is_active=True)
    else:
        vendor = Vendor.objects.filter(is_approved=True, user__is_active=True)
    ven_profile = UserProfile.objects.all()
    count = vendor.count()
    print(type(count))
    return render(request, 'marketplace/market.html', {'count': count, 'vendor': vendor, 'ven_profile':ven_profile})


def Restaurant_menu(request,slug):
    vendor = get_object_or_404(Vendor,slug=slug)
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'category',FoodItem.objects.filter(is_available = True)
        )
    )
    ven_profile = UserProfile.objects.get(user=vendor.user)
    cart = Add_Card.objects.all()
    return render(request,'marketplace/restaurantmenu.html',{'categories':categories,'ven_profile':ven_profile,'details_id' : slug , 'cart' : cart})


def Add_To_Cart(request,pk,details_id):
    if request.user.is_authenticated:
        try:
            fooditem = FoodItem.objects.get(id=pk)
            try:
                check_cart = Add_Card.objects.get(user = request.user , food_item = fooditem )
                check_cart.quantity += 1
                check_cart.total = check_cart.quantity * check_cart.food_item.price
                check_cart.save()
                return redirect('restaurantmenu',details_id)
            except:
                check_cart = Add_Card.objects.create(user = request.user , food_item = fooditem , quantity = 1)
                # check_cart.save()
                return redirect('restaurantmenu',details_id)
        except:
            return redirect('restaurantmenu',details_id)
    else:
        return redirect('login')
    
def Remove_Cart(request,pk,details_id):
    if request.user.is_authenticated:
        try:
            fooditem = FoodItem.objects.get(id=pk)
            check_cart = Add_Card.objects.get(user = request.user , food_item = fooditem )
            if check_cart.quantity != 1:
                check_cart.quantity -= 1
                check_cart.total = check_cart.quantity * check_cart.food_item.price
                check_cart.save()
                return redirect('restaurantmenu',details_id)
            else:
                check_cart = Add_Card.objects.get(user = request.user , food_item = fooditem).delete()
                print('success.......')
                return HttpResponseRedirect(reverse('restaurantmenu'))
        except:
            return redirect('restaurantmenu',details_id)
    else:
        return redirect('login')


def Cart(request):
    cart_items = Add_Card.objects.all()
    price = 0
    delivery_fee = 0
    grand_total = 0
    for i in cart_items:
        price += i.quantity*i.food_item.price

    if price>0 and price<250:
        delivery_fee=50
    elif price>=250 and price<500:
        delivery_fee=30
    elif price>=500:
        delivery_fee= 0
    else:
        delivery_fee=0

    gst=price*0.06
    gst=gst.__round__(2)
    grand_total = price+gst*2+delivery_fee
    grand_total=grand_total.__round__(2)

    return render(request,'marketplace/cart.html',{'cart_items':cart_items,'gst':gst,'delivery_fee':delivery_fee,'grand_total':grand_total})