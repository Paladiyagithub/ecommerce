from django.db import models
from accounts.models import User , UserProfile
from accounts.validators import allow_only_images_validator
from django.utils.text import slugify
import datetime as dt
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User ,on_delete = models.CASCADE , blank = True , null = True)
    slug = models.SlugField(max_length = 100)
    userprofile = models.OneToOneField(UserProfile , on_delete = models.CASCADE , blank = True , null = True)
    Restaurant_name = models.CharField(max_length = 200)
    Restaurant_license = models.ImageField(upload_to="licence",blank=False,null=False)
    is_approved = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Restaurant_name



class OpeningHours(models.Model):
    DAYS = [
        (1 , 'SUNDAY'),
        (2 , 'MONDAY'),
        (3 , 'TUESDAY'),
        (4 , 'WEDNESDAY'),
        (5 , 'TUESDAY'),
        (6 , 'FRIDAY'),
        (7 , 'SATURDAY'),
    ]

    HOUR_CHOICES = [(dt.time(h , m).strftime('%I:%M %p'),dt.time(h , m).strftime('%I:%M %p')) for h in range(0,24) for m in (0,30)]

    vendor = models.ForeignKey(Vendor,on_delete = models.CASCADE)
    days = models.CharField(choices=DAYS , max_length=10)
    open_time = models.CharField(choices=HOUR_CHOICES,max_length=100)
    close_time = models.CharField(choices=HOUR_CHOICES ,max_length=100)
    is_opened = models.BooleanField(default=False)
