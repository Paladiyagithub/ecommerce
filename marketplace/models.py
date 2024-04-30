from django.db import models
from accounts.models import *
from menu.models import *
# Create your models here.


class Add_Card(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    food_item = models.ForeignKey(FoodItem,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    # def __str__(self):
    #     return self.quantity 
