from django import forms
from accounts.models import User , UserProfile

class UserRegisterationForm(forms.ModelForm):
    confirm_password =  forms.CharField(widget=forms.PasswordInput)
    password =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email' , 'username' , 'password']
    
    def clean(self):
        cleaned_data = super(UserRegisterationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")