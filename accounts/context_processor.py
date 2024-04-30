from vendor.models import *
from marketplace.models import *
def get_vendor(request):
    
    try:
        vendor = Vendor.objects.get(user = request.user)
        userprofile = UserProfile.objects.get(user = request.user)
    except:
        vendor = None
        userprofile = None

    return dict(vendor = vendor, userprofile = userprofile)


def count_cart_item(request):
    cart_count = 0 
    try:
        cart_item = Add_Card.objects.all()
        for item in cart_item:
            cart_count += item.quantity
    except:
        cart_count = 0
    return dict(cart_count=cart_count)