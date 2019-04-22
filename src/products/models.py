from django.db import models

# Create your models here.
# backend memory lel product

class Product(models.Model):    # inharate from Model
    #attribute for the class of the products, will be mapped to the databased using models field
    # ay 7aga ba3den shof el fields fel documetation
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()

    
