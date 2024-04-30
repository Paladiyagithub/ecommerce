from django.shortcuts import render , redirect , HttpResponse
from accounts.forms import *
from django.contrib import messages
from vendor.forms import vendorForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from accounts.utils import detectUser,send_verification_email
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode 
from django.contrib.auth.tokens import default_token_generator 
from vendor.models import Vendor
# Create your views here.


def check_role_user(user):
    if user.role == 2:
        return True
    else :
        raise PermissionDenied

def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


@login_required(login_url='login')
def myAccounts(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
@user_passes_test(check_role_user)
def UserDashBoard(request):
    return render(request,'dashboard/userdashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def VendorDashBoard(request):
    return render(request,'dashboard/vendordashboard.html')


def index(request):
    return render(request , 'index.html')

def RegisterUser(request):
    if request.user.is_authenticated:
        messages.warning(request , 'You are already loggedin...!')
        return redirect('myAccounts')
    elif request.method == 'POST':
        form = UserRegisterationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name'] 
            last_name =  form.cleaned_data['last_name']
            username =  form.cleaned_data['username']
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name = first_name,last_name = last_name , username = username , email = email , password = password)
            user.set_password(password)
            user.role = user.CUSTOMER
            user.save()
            # Send verification email
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request , 'hey Thanks For Register')
            return redirect('registeruser')
        else :
            print('Error Accrued')
            print(form.errors) 

    else :
        form = UserRegisterationForm()
    return render(request , 'accounts/registeruser.html' , {'form':form})



def registerRestaurant(request):
    if request.user.is_authenticated:
        messages.warning(request , 'You are already loggedin...!')
        return redirect('myAccounts')
    elif request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        v_form = vendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name'] 
            last_name =  form.cleaned_data['last_name']
            username =  form.cleaned_data['username']
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name = first_name,last_name = last_name , username = username , email = email , password = password)
            user.set_password(password)
            user.role = user.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            User_Profile = UserProfile.objects.get(user=user)
            vendor.User_Profile = User_Profile
            vendor.save()
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request , 'hey Thanks For Register')
            messages.success(request , 'hey Thanks For Register')
            return redirect('registerRestaurant')

    else:
        form = UserRegisterationForm()
        v_form = vendorForm()
    return render(request , 'accounts/registerrestaurant.html' , {'form' : form , 'v_form' : v_form})



def Login(request):
    if request.user.is_authenticated:
        messages.warning(request , 'You are already loggedin...!')
        return redirect('myAccounts')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = authenticate(request , email = email , password = password)
        if user:
            if user.is_active:
                login(request , user)
                messages.success(request , 'Login successfully..')
                return redirect('myAccounts')
            else :
                messages.warning(request , 'user is not active')
                return redirect('login')
        else :
            messages.warning(request , 'Please check your credentials....!')
            return redirect('login')
    return render(request , 'accounts/login.html')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('index')


def activate(request, uidb64 , token ):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError , ValueError ,OverflowError ,User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user , token):
        user.is_active = True
        user.save()
        messages.success(request , 'Congratulation! Your Account is Activated')
        return redirect('myAccounts')
    else :
        messages.error(request,'Invalid activation link')
        return redirect('myAccounts')
    

