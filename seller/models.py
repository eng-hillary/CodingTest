from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_profiles', default='profile.jpg', null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'