from django.db import models

class Order(models.Model):
    
    quantity=models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=6,decimal_places=2)
    name = models.CharField(max_length=32)



# Create your models here.
