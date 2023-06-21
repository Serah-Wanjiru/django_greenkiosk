from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","quantity","total","date_created","date_updated")
   

admin.site.register(Order, OrderAdmin)

# Register your models here.
