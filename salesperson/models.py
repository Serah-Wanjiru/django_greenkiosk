from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    contacts = models.CharField(max_length=32)
    store_name = models.CharField(max_length=32)
   
    
    def __str__(self):
        return self.name

# Create your models here.
