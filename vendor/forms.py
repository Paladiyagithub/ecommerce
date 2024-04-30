from django import forms
from vendor.models import Vendor,UserProfile,OpeningHours
from accounts.validators import allow_only_images_validator

class vendorForm(forms.ModelForm):
    Restaurant_license = forms.FileField(validators = [allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ['Restaurant_name','Restaurant_license']



class venProfileForm(forms.ModelForm):

    Profile_picture = forms.FileField(validators = [allow_only_images_validator])
    cover_photo = forms.FileField(validators = [allow_only_images_validator])

    latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = UserProfile
        fields = ['Profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude']

class OpeningForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['vendor','days','open_time','close_time','is_opened']
