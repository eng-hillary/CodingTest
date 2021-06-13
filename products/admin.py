from django.contrib import admin
from . models import Product, Manufacturer
# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Product)