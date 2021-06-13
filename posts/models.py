from django.db import models
from django.utils import timezone
from seller.models import Seller

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

