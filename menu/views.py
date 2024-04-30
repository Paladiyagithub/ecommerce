from django.shortcuts import render,get_object_or_404,redirect
from vendor.models import Vendor
from menu.models import *
from menu.forms import CategoryForm , FoodItemForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.defaultfilters import slugify
# Create your views here.

@login_required(login_url='login')
def Menu(request):
    vendor = Vendor.objects.get(user=request.user)
    category = Category.objects.filter(vendor=vendor)
    return render(request,'menu/menu.html' , {'category':category})


@login_required(login_url='login')
def FoodItem_by_category(request,pk=None):
    vendor = Vendor.objects.get(user=request.user)
    category = get_object_or_404(Category , pk = pk)
    Food_Item = FoodItem.objects.filter(vendor=vendor,category = category)

    return render(request , 'menu/food_by_category.html',{'food_item':Food_Item,'category':category})


def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor

@login_required(login_url='login')
def Add_Category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.cleaned_data.get('category_name')
            category =  category_form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            category_form.save()
            return redirect('menuitems')
    category_form = CategoryForm()
    return render(request, 'menu/add_category.html',{'category_form':category_form})


@login_required(login_url='login')
def Add_Category_Wise_Item(request):
    FoodItem_form = FoodItemForm()
    category = Category.objects.filter(vendor=get_vendor(request))
    if request.method == "POST":
        FoodItem_form = FoodItemForm(request.POST,request.FILES)
        if FoodItem_form.is_valid():
            food_name = FoodItem_form.cleaned_data['food_name']
            food = FoodItem_form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(food_name)
            FoodItem_form.save()
            return redirect('menuitems')    
    return render(request, 'menu/add_fooditem.html',{'fooditem_form':FoodItem_form,'category':category})



def del_Category(request,pk):
    data = Category.objects.get(pk = pk)
    data.delete()
    return redirect('menuitems')

def Edit_Category(request,pk):
    Category_res = Category.objects.get(pk = pk)
    if request.method == "POST":
        Category_form = CategoryForm(request.POST,instance=Category_res)
        if Category_form.is_valid():    
            Category_name = Category_form.cleaned_data['category_name']
            category = Category_form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(Category_name)
            Category_form.save()
            return redirect('menuitems') 
    Category_form = CategoryForm(instance=Category_res)
    return render(request, 'menu/Edit_category.html', {'category_form':Category_form})    



def del_FoodItem(request,pk):
    data = FoodItem.objects.get(pk = pk)
    data.delete()
    return redirect('menuitems')

def Edit_FoodItem(request,pk):
    FoodItem_res = FoodItem.objects.get(pk = pk)
    if request.method == "POST":
        FoodItem_form = FoodItemForm(request.POST,request.FILES,instance=FoodItem_res)
        if FoodItem_form.is_valid():    
            FoodItem_name = FoodItem_form.cleaned_data['food_name']
            fooditem = FoodItem_form.save(commit=False)
            fooditem.vendor = get_vendor(request)
            fooditem.slug = slugify(FoodItem_name)
            FoodItem_form.save()
            return redirect('menuitems') 
    FoodItem_form = FoodItemForm(instance=FoodItem_res)
    return render(request, 'menu/Edit_category.html',{'fooditem_form':FoodItem_form})    