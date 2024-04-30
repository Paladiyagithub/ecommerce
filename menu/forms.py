from django import forms
from menu.models import Category , FoodItem
from accounts.validators import allow_only_images_validator

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','description']


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['category','food_name','description','images','price','is_available']