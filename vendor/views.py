from django.shortcuts import render ,redirect
from vendor.models import Vendor,UserProfile
from django.contrib.auth.decorators import login_required,user_passes_test
from vendor.forms import *
from django.utils.text import slugify
# Create your views here.

# @login_required(login_url='login')
# def VendorProfile(request):
#     ve_detail  = Vendor.objects.get(user=request.user)
#     userprofile_detail  = UserProfile.objects.get(user=request.user)
#     return render(request  , 'vendor/vprofile.html' , {'ve_detail':ve_detail , 'userprofile_detail' : userprofile_detail} )

@login_required(login_url='login')
def VendorProfile(request):
    user_res = UserProfile.objects.get(user=request.user)
    vendor_res = Vendor.objects.get(user=request.user)
    if request.method == "POST":
        user_form = venProfileForm(instance=user_res)
        vendor_form = vendorForm(instance=vendor_res)
        user_form = venProfileForm(request.POST,request.FILES, instance=user_res)
        vendor_form = vendorForm(request.POST,request.FILES, instance=vendor_res)
        if user_form.is_valid() and vendor_form.is_valid():
            Restaurant_name = vendor_form.cleaned_data['Restaurant_name']
            vendor_form.Restaurant_license = vendor_form.cleaned_data['Restaurant_license']
            user_form.Profile_picture = user_form.cleaned_data['Profile_picture']
            user_form.cover_photo = user_form.cleaned_data['cover_photo']
            vendor_form.slug = slugify(Restaurant_name)
            user_form.save()
            vendor_form.save()
            redirect('vendorprofile')
    
    user_form = venProfileForm(instance=user_res)
    vendor_form = vendorForm(instance=vendor_res)
    return render(request, 'vendor/vProfile.html',{'user_form':user_form,'vendor_form' : vendor_form})