from django.db import models


class Payments(models.Model):
    name = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    order = models.PositiveIntegerField()
    status = models.CharField(max_length=32)
    method_of_payment = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
       
    def __str__(self):
        return self.name

# Create your models here.
