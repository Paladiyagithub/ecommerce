from django.contrib import admin
from vendor.models import Vendor , OpeningHours
# Register your models here.



class VendorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Restaurant_name',)}


admin.site.register(Vendor,VendorAdmin)
admin.site.register(OpeningHours)