from django.contrib import admin

# Register your models here.
# 3ashan te2dar tshofha fel admin page bta3t django

# da esmo relative import 3ashan el models.py f nafs el level ma3 product.py
from .models import Product

admin.site.register(Product)