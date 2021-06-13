from django.db import models
from django.db.models.base import Model

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images', default='product.jpg', null=True)

    def __str__(self):
        return f'{self.name}'