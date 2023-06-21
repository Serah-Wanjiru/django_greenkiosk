from django.contrib import admin
from .models import Payments

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("name","amount","order","status","method_of_payment","date_created","date_updated")
   

admin.site.register(Payments, PaymentsAdmin)


